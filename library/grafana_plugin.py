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
module: grafana_plugin
author:
  - "Thierry Sallé (@tsalle)"
version_added: "2.5"
short_description: Manage Grafana plugins via grafana-cli
description:
  - Install and remove Grafana plugins.
options:
  name:
    required: true
    description:
      - Name of the plugin.
  version:
    description:
      - Version of the plugin to install.
      - Default to latest
  grafana_plugins_dir:
    description:
      - Directory where Grafana plugin will be installed.
  grafana_repo:
    description:
      - Grafana repository. If not set, gafana-cli will use the default value C(https://grafana.net/api/plugins).
  grafana_plugin_url:
    description:
      - Custom Grafana plugin URL
      - Require grafana 4.6.x or later
  state:
    default: present
    choices: [present, absent]
    description:
      - Status of the Grafana plugin.
      - If latest is set, the version parameter will be ignored.
'''

EXAMPLES = '''
---
- name: install - update Grafana piechart panel plugin
  grafana_plugin:
    name: grafana-piechart-panel
    version: latest
    state: present
'''

RETURN = '''
---
version:
  description: version of the installed / removed plugin.
  type: string
  returned: allways
'''

import base64
import json
import os
from ansible.module_utils.basic import AnsibleModule

__metaclass__ = type


class GrafanaCliException(Exception):
    pass


def grafana_cli_bin(params):
    '''
    Get the grafana-cli binary path with global options.
    Raise a GrafanaCliException if the grafana-cli is not present or not in PATH

    :param params: ansible module params. Used to fill grafana-cli global params.
    '''
    program = 'grafana-cli'
    grafana_cli = None

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            grafana_cli = program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                grafana_cli = exe_file
                break

    if grafana_cli is None:
        raise GrafanaCliException('grafana-cli binary is not present or not in PATH')
    else:
        if 'grafana_plugin_url' in params and params['grafana_plugin_url']:
            grafana_cli = '{} {} {}'.format(grafana_cli, '--pluginUrl', params['grafana_plugin_url'])
        if 'grafana_plugins_dir' in params and params['grafana_plugins_dir']:
            grafana_cli = '{} {} {}'.format(grafana_cli, '--pluginsDir', params['grafana_plugins_dir'])
        if 'grafana_repo' in params and params['grafana_repo']:
            grafana_cli = '{} {} {}'.format(grafana_cli, '--repo', params['grafana_repo'])
        if 'validate_certs' in params and params['validate_certs'] is False:
            grafana_cli = '{} {}'.format(grafana_cli, '--insecure')

        return '{} {}'.format(grafana_cli, 'plugins')


def get_grafana_plugin_version(module, params):
    '''
    Fetch grafana installed plugin version. Return None if plugin is not installed.

    :param module: ansible module object. used to run system commands.
    :param params: ansible module params.
    '''
    grafana_cli = grafana_cli_bin(params)
    rc, stdout, stderr = module.run_command('{} ls'.format(grafana_cli))
    stdout_lines = stdout.split("\n")
    for line in stdout_lines:
        if line.find(' @ ') != -1:
            line = line.rstrip()
            plugin_name, plugin_version = line.split(' @ ')
            if plugin_name == params['name']:
                return plugin_version
    return None


def grafana_plugin(module, params):
    '''
    Install update or remove grafana plugin

    :param module: ansible module object. used to run system commands.
    :param params: ansible module params.
    '''
    grafana_cli = grafana_cli_bin(params)

    if params['state'] == 'present':
        grafana_plugin_version = get_grafana_plugin_version(module, params)
        if grafana_plugin_version is not None:
            if 'version' in params and params['version']:
                if params['version'] == grafana_plugin_version:
                    return {'msg': 'Grafana plugin already installed',
                            'changed': False,
                            'version': grafana_plugin_version}
                else:
                    if params['version'] == 'latest' or params['version'] is None:
                        cmd = '{} update {}'.format(grafana_cli, params['name'])
                    else:
                        cmd = '{} install {} {}'.format(grafana_cli, params['name'], params['version'])
            else:
                return {'msg': 'Grafana plugin already installed',
                        'changed': False,
                        'version': grafana_plugin_version}
        else:
            if 'version' in params:
                if params['version'] == 'latest' or params['version'] is None:
                    cmd = '{} install {}'.format(grafana_cli, params['name'])
                else:
                    cmd = '{} install {} {}'.format(grafana_cli, params['name'], params['version'])
            else:
                cmd = '{} install {}'.format(grafana_cli, params['name'])
    else:
        cmd = '{} uninstall {}'.format(grafana_cli, params['name'])

    rc, stdout, stderr = module.run_command(cmd)
    if rc == 0:
        stdout_lines = stdout.split("\n")
        for line in stdout_lines:
            if line.find(params['name']):
                plugin_name, plugin_version = line.split(' @ ')
                return {'msg': 'Grafana plugin {} installed : {}'.format(params['name'], cmd),
                        'changed': True,
                        'version': plugin_version}
    else:
        raise GrafanaCliException("'{}' execution returned an error : [{}] {} {}".format(cmd, rc, stdout, stderr))


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True,
                      type='str'),
            version=dict(type='str'),
            grafana_plugins_dir=dict(type='str'),
            grafana_repo=dict(type='str'),
            grafana_plugin_url=dict(type='str'),
            state=dict(choices=['present', 'absent'],
                       default='present')
        ),
        supports_check_mode=False
    )

    try:
        result = grafana_plugin(module, module.params)
    except GrafanaCliException as e:
        module.fail_json(
            failed=True,
            msg="{}".format(e)
        )
        return
    except Exception as e:
        module.fail_json(
            failed=True,
            msg="{} : {} ".format(type(e), e)
        )
        return

    module.exit_json(
        failed=False,
        **result
    )
    return

if __name__ == '__main__':
    main()
