#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017, Thierry Sallé (@tsalle)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

ANSIBLE_METADATA = {
    'status': ['preview'],
    'supported_by': 'community',
    'metadata_version': '1.1'
}

DOCUMENTATION = '''
---
module: grafana_datasource
author:
  - "Thierry Sallé (@tsalle)"
version_added: "2.5"
short_description: Manage grafana datasources
description:
  - Create/update/delete grafana datasources via API
options:
  grafana_url:
    required: true
    description:
      - Grafana url
  name:
    required: true
    description:
      - Name of the datasource
  ds_type:
    required: true
    choices: [graphite,prometheus,elasticsearch,influxdb,opentsdb,mysql,postgres]
    description:
     - Type of the datasource
  url:
    required: true
    description:
      - Url of the datasource
  access:
    required: false
    default: proxy
    choices: [proxy,direct]
    description:
      - Access mode for this datasource
  grafana_user:
    required: false
    default: admin
    description:
      - Grafana API user
  grafana_password:
    required: false
    default: admin
    description:
      - Grafana API password
  grafana_api_key:
    required: false
    description:
      - Grafana API key
      - If set, grafana_user and grafana_password will be ignored
  database:
    required: false
    description:
      - Name of the database for the datasource.
      - This options is required when the ds_type is influxdb, elasticsearch (index name), mysql or postgres
  user:
    required: false
    description:
      - Datasource login user for influxdb datasources
  password:
    required: false
    description:
      - Datasource password
  basic_auth_user:
    required: false
    description:
      - Datasource basic auth user.
      - Setting this option with basic_auth_password will enable basic auth.
  basic_auth_password:
    required: false
    description:
      - Datasource basic auth password, when basic auth is true
  with_credentials:
    required: false
    default: false
    description:
      - Whether credentials such as cookies or auth headers should be sent with cross-site requests.
  tls_client_cert:
    required: false
    description:
      - client tls certificate.
      - If tls_client_cert and tls_client_key are set, this will enable tls auth.
      - begins with ----- BEGIN CERTIFICATE -----
  tls_client_key:
    required: false
    description:
      - client tls private key
      - befins with ----- BEGIN RSA PRIVATE KEY -----
  tls_ca_cert:
    required: false
    description:
      - tls ca certificate for self signed certificates.
      - only used when tls_client_cert and tls_client_key are set
  is_default:
    required: false
    default: false
    description:
      - Make this datasource the default one
  org_id:
    required: false
    description:
      - Grafana Organisation ID in which the datasource should be created
      - Not used when grafana_api_key is set, because the grafana_api_key only belong to one organisation.
    default: 1
  state:
    required: false
    default: present
    choices: [present, absent]
    description:
      - Status of the datasource
  es_version:
    required: false
    default: 5
    choices: [2, 5, 56]
    description:
      - Elasticsearch version (for ds_type = elasticsearch only)
      - Version 56 is for elasticsearch 5.6+ where tou can specify the max_concurrent_shard_requests option.
  max_concurrent_shard_requests:
    required: false
    default: 256
    description:
      - Starting with elasticsearch 5.6, you can specify the max concurrent shard per requests.
  time_field:
    required: false
    default: timestamp
    description:
      - Name of the time field in elasticsearch ds
      - For example C(@timestamp)
  time_interval:
    required: false
    description:
      - Minimum group by interval for influxdb or elasticsearch datasources
      - for example '>10s'
  interval:
    required: false
    choices: ['', 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Yearly']
    description:
      - for elasticsearch ds_type, this is the index pattern used.
  tsdb_version:
    required: false
    choices: [1, 2, 3]
    description:
      - opentsdb version (1 for <= 2.1, 2 for ==2.2, 3 for ==2.3)
    default: 1
  tsdb_resolution:
    required: false
    choices: [second, millisecond]
    description:
      - opentsdb time resolution
    default: 1
  sslmode:
    choices: ['disable','require','verify-ca','verify-full']
    description:
      - SSL mode for postgres datasoure type.
  validate_certs:
    required: false
    default: True
    description:
      - Validate or not grafana certificate
'''

EXAMPLES = '''
---
- name: create elasticsearch datasource
  grafana_datasource:
    name: my_elastic
    grafana_url: http://grafana.company.com
    type: elasticsearch
    url: https://elasticsearch.company.com:9200
    database: my-index_*
    basic_auth: true
    basic_auth_user: grafana
    basic_auth_password: xxxxxxxx
    json_data: '{"esVersion":5, "timeField": "@timestamp"}'
    state: present
'''

RETURN = '''
---
name:
  description: name of the datasource created.
  returned: success
  type: string
  sample: test-ds
id:
  description: Id of the datasource
  returned: success
  type: int
  sample: 42
before:
  description: datasource returned by grafana api
  returned: changed
  type: dict
  sample: { "access": "proxy",
        "basicAuth": false,
        "database": "test_*",
        "id": 1035,
        "isDefault": false,
        "jsonData": {
            "esVersion": 5,
            "timeField": "@timestamp",
            "timeInterval": "1m",
        },
        "name": "grafana_datasource_test",
        "orgId": 1,
        "type": "elasticsearch",
        "url": "http://elastic.company.com:9200",
        "user": "",
        "password": "",
        "withCredentials": false }
after:
  description: datasource updated by module
  returned: changed
  type: dict
  sample: { "access": "proxy",
        "basicAuth": false,
        "database": "test_*",
        "id": 1035,
        "isDefault": false,
        "jsonData": {
            "esVersion": 5,
            "timeField": "@timestamp",
            "timeInterval": "10s",
        },
        "name": "grafana_datasource_test",
        "orgId": 1,
        "type": "elasticsearch",
        "url": "http://elastic.company.com:9200",
        "user": "",
        "password": "",
        "withCredentials": false }
'''

import base64
import json
import os
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url

__metaclass__ = type


class GrafanaAPIException(Exception):
    pass


def grafana_switch_organisation(module, grafana_url, org_id, headers):
    r, info = fetch_url(module, '%s/api/user/using/%d' % (grafana_url, org_id), headers=headers, method='POST')
    if info['status'] != 200:
        raise GrafanaAPIException('Unable to switch to organization %s : %s' % (org_id, info))


def grafana_datasource_exists(module, grafana_url, name, headers):
    datasource_exists = False
    ds = {}
    r, info = fetch_url(module, '%s/api/datasources/name/%s' % (grafana_url, name), headers=headers, method='GET')
    if info['status'] == 200:
        datasource_exists = True
        ds = json.loads(r.read())
    elif info['status'] == 404:
        datasource_exists = False
    else:
        raise GrafanaAPIException('Unable to get datasource %s : %s' % (name, info))

    return datasource_exists, ds


def grafana_create_datasource(module, data):

    # define data payload for grafana API
    payload = {'orgId': data['org_id'],
               'name': data['name'],
               'type': data['ds_type'],
               'access': data['access'],
               'url': data['url'],
               'database': data['database'],
               'withCredentials': data['with_credentials'],
               'isDefault': data['is_default'],
               'user': data['user'],
               'password': data['password']}

    # define basic auth
    if 'basic_auth_user' in data and data['basic_auth_user'] and 'basic_auth_password' in data and data['basic_auth_password']:
        payload['basicAuth'] = True
        payload['basicAuthUser'] = data['basic_auth_user']
        payload['basicAuthPassword'] = data['basic_auth_password']
    else:
        payload['basicAuth'] = False

    # define tls auth
    json_data = {}
    if data.get('tls_client_cert') and data.get('tls_client_key'):
        json_data['tlsAuth'] = True
        if data.get('tls_ca_cert'):
            payload['secureJsonData'] = {
                'tlsCACert': data['tls_ca_cert'],
                'tlsClientCert': data['tls_client_cert'],
                'tlsClientKey': data['tls_client_key']
            }
            json_data['tlsAuthWithCACert'] = True
        else:
            payload['secureJsonData'] = {
                'tlsClientCert': data['tls_client_cert'],
                'tlsClientKey': data['tls_client_key']
            }
    else:
        json_data['tlsAuth'] = False
        json_data['tlsAuthWithCACert'] = False

    # datasource type related parameters
    if data['ds_type'] == 'elasticsearch':
        json_data['esVersion'] = data['es_version']
        json_data['timeField'] = data['time_field']
        if data.get('interval'):
            json_data['interval'] = data['interval']
        if data['es_version'] >= 56:
            json_data['maxConcurrentShardRequests'] = data['max_concurrent_shard_requests']

    if data['ds_type'] == 'elasticsearch' or data['ds_type'] == 'influxdb':
        if data.get('time_interval'):
            json_data['timeInterval'] = data['time_interval']

    if data['ds_type'] == 'opentsdb':
        json_data['tsdbVersion'] = data['tsdb_version']
        if data['tsdb_resolution'] == 'second':
            json_data['tsdbResolution'] = 1
        else:
            json_data['tsdbResolution'] = 2

    if data['ds_type'] == 'postgres':
        json_data['sslmode'] = data['sslmode']

    payload['jsonData'] = json_data

    # define http header
    headers = {'content-type': 'application/json; charset=utf8'}
    if 'grafana_api_key' in data and data['grafana_api_key'] is not None:
        headers['Authorization'] = "Bearer %s" % data['grafana_api_key']
    else:
        auth = base64.encodestring('%s:%s' % (data['grafana_user'], data['grafana_password'])).replace('\n', '')
        headers['Authorization'] = 'Basic %s' % auth
        grafana_switch_organisation(module, data['grafana_url'], data['org_id'], headers)

    # test if datasource already exists
    datasource_exists, ds = grafana_datasource_exists(module, data['grafana_url'], data['name'], headers=headers)

    result = {}
    if datasource_exists is True:
        del ds['typeLogoUrl']
        if ds['basicAuth'] is False:
            del ds['basicAuthUser']
            del ds['basicAuthPassword']
        if 'jsonData' in ds:
            if 'tlsAuth' in ds['jsonData'] and ds['jsonData']['tlsAuth'] is False:
                del ds['secureJsonFields']
            if 'tlsAuth' not in ds['jsonData']:
                del ds['secureJsonFields']
        payload['id'] = ds['id']
        if ds == payload:
            # unchanged
            result['name'] = data['name']
            result['id'] = ds['id']
            result['msg'] = "Datasource %s unchanged." % data['name']
            result['changed'] = False
        else:
            # update
            r, info = fetch_url(module, '%s/api/datasources/%d' % (data['grafana_url'], ds['id']), data=json.dumps(payload), headers=headers, method='PUT')
            if info['status'] == 200:
                res = json.loads(r.read())
                result['name'] = data['name']
                result['id'] = ds['id']
                result['before'] = ds
                result['after'] = payload
                result['msg'] = "Datasource %s updated %s" % (data['name'], res['message'])
                result['changed'] = True
            else:
                raise GrafanaAPIException('Unable to update the datasource id %d : %s' % (ds['id'], info))
    else:
        # create
        r, info = fetch_url(module, '%s/api/datasources' % data['grafana_url'], data=json.dumps(payload), headers=headers, method='POST')
        if info['status'] == 200:
            res = json.loads(r.read())
            result['msg'] = "Datasource %s created : %s" % (data['name'], res['message'])
            result['changed'] = True
            result['name'] = data['name']
            result['id'] = res['id']
        else:
            raise GrafanaAPIException('Unable to create the new datasource %s : %s - %s.' % (data['name'], info['status'], info))

    return result


def grafana_delete_datasource(module, data):

    # define http headers
    headers = {'content-type': 'application/json'}
    if 'grafana_api_key' in data and data['grafana_api_key']:
        headers['Authorization'] = "Bearer %s" % data['grafana_api_key']
    else:
        auth = base64.encodestring('%s:%s' % (data['grafana_user'], data['grafana_password'])).replace('\n', '')
        headers['Authorization'] = 'Basic %s' % auth
        grafana_switch_organisation(module, data['grafana_url'], data['org_id'], headers)

    # test if datasource already exists
    datasource_exists, ds = grafana_datasource_exists(module, data['grafana_url'], data['name'], headers=headers)

    result = {}
    if datasource_exists is True:
        # delete
        r, info = fetch_url(module, '%s/api/datasources/name/%s' % (data['grafana_url'], data['name']), headers=headers, method='DELETE')
        if info['status'] == 200:
            res = json.loads(r.read())
            result['msg'] = "Datasource %s deleted : %s" % (data['name'], res['message'])
            result['changed'] = True
            result['name'] = data['name']
            result['id'] = 0
        else:
            raise GrafanaAPIException('Unable to update the datasource id %s : %s' % (ds['id'], info))
    else:
        # datasource does not exists : do nothing
        result = {'msg': "Datasource %s does not exists" % data['name'],
                  'changed': False,
                  'id': 0,
                  'name': data['name']}

    return result


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            state=dict(choices=['present', 'absent'],
                       default='present'),
            grafana_url=dict(required=True, type='str'),
            ds_type=dict(choices=['graphite',
                                  'prometheus',
                                  'elasticsearch',
                                  'influxdb',
                                  'opentsdb',
                                  'mysql',
                                  'postgres']),
            url=dict(required=True, type='str'),
            access=dict(default='proxy', choices=['proxy', 'direct']),
            grafana_user=dict(default='admin'),
            grafana_password=dict(default='admin', no_log=True),
            grafana_api_key=dict(type='str', no_log=True),
            database=dict(type='str'),
            user=dict(default='', type='str'),
            password=dict(default='', no_log=True, type='str'),
            basic_auth_user=dict(type='str'),
            basic_auth_password=dict(type='str', no_log=True),
            with_credentials=dict(default=False, type='bool'),
            tls_client_cert=dict(type='str', no_log=True),
            tls_client_key=dict(type='str', no_log=True),
            tls_ca_cert=dict(type='str', no_log=True),
            is_default=dict(default=False, type='bool'),
            org_id=dict(default=1, type='int'),
            es_version=dict(type='int', default=5, choices=[2, 5, 56]),
            max_concurrent_shard_requests=dict(type='int', default=256),
            time_field=dict(default='@timestamp', type='str'),
            time_interval=dict(type='str'),
            interval=dict(type='str', choices=['', 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Yearly'], default=''),
            tsdb_version=dict(type='int', default=1, choices=[1, 2, 3]),
            tsdb_resolution=dict(type='str', default='second', choices=['second', 'millisecond']),
            sslmode=dict(default='disable', choices=['disable', 'require', 'verify-ca', 'verify-full']),
            validate_certs=dict(type='bool', default=True)
        ),
        supports_check_mode=False,
        required_together=[['grafana_user', 'grafana_password', 'org_id'], ['tls_client_cert', 'tls_client_key']],
        mutually_exclusive=[['grafana_user', 'grafana_api_key']],
        required_if=[
            ['ds_type', 'opentsdb', ['tsdb_version', 'tsdb_resolution']],
            ['ds_type', 'influxdb', ['database']],
            ['ds_type', 'elasticsearch', ['database', 'es_version', 'time_field', 'interval']],
            ['ds_type', 'mysql', ['database']],
            ['ds_type', 'postgres', ['database', 'sslmode']],
            ['es_version', 56, ['max_concurrent_shard_requests']]
        ],
    )

    try:
        if module.params['state'] == 'present':
            result = grafana_create_datasource(module, module.params)
        else:
            result = grafana_delete_datasource(module, module.params)
    except GrafanaAPIException as e:
        module.fail_json(
            failed=True,
            msg="error %s : %s " % (type(e), e)
        )
        return

    module.exit_json(
        failed=False,
        **result
    )
    return

if __name__ == '__main__':
    main()
