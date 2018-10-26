#!/usr/bin/env python
from ansible.errors import AnsibleError, AnsibleFilterError
from collections import OrderedDict
import json

def grafana_ordered_dict(od, reverse=False, sort_key=None):
    """Sort nested ordered dict recursively.

    sort_key
    - sort by dict key case insensitively:
        sort_key = lambda (k, v): k.lower()
    """
    if not isinstance(od, OrderedDict):
        od = OrderedDict(od)

    res = OrderedDict()
    for k, v in sorted(od.items(), reverse=reverse, key=sort_key):
        if isinstance(v, dict):
            res[k] = grafana_ordered_dict(v)
        else:
            res[k] = v
    return res

def grafana_missing_orgs(actual_orgs, expected_orgs):
    '''
    1st : fact returned by uri module on grafana api/orgs
    2nd : a list of organisations dict
    return: a list of organisations dict missing in the json
    '''

    if not actual_orgs['json']:
        raise AnsibleFilterError('Missing or empty json key into grafana fact')

    if not isinstance(actual_orgs['json'],list):
        raise AnsibleFilterError('Invalid json key format into grafana fact')

    try:
        json_data = json.dumps(actual_orgs['json'])
    except Exception as e:
        raise AnsibleFilterError("Invalid json string into grafana fact: %s, Error: %s" % (actual_orgs['json'], e))

    if not isinstance(expected_orgs,list):
        raise AnsibleFilterError('Expected grafana orgs provided is not a list')

    missing = []
    for dict_expected in expected_orgs:
        for dict_actual in actual_orgs['json']:
            if ( 'name', dict_expected['name'] ) in dict_actual.items():
                break
        else:
           missing.append(dict_expected.copy()) 

    return missing

def grafana_orgs2update(actual_orgs, expected_orgs):
    '''
    1st : fact returned by uri module on grafana api/orgs
    2nd : a list of organisations dict
    return: a list of organisations dict who need to be updated
    '''

    if not actual_orgs['json']:
        raise AnsibleFilterError('Missing or empty json key into grafana fact')

    if not isinstance(actual_orgs['json'],list):
        raise AnsibleFilterError('Invalid json key format into grafana fact')

    try:
        json_data = json.dumps(actual_orgs['json'])
    except Exception as e:
        raise AnsibleFilterError("Invalid json string into grafana fact: %s, Error: %s" % (actual_orgs['json'], e))

    if not isinstance(expected_orgs,list):
        raise AnsibleFilterError('Expected grafana orgs provided is not a list')

    orgs2update = []
    for dict_expected in expected_orgs:
        for dict_actual in actual_orgs['json']:
            if ( 'name', dict_expected['name'] ) in dict_actual.items():
                dict_expected['id'] = dict_actual['id']
                if grafana_ordered_dict(dict_expected.items()) != grafana_ordered_dict(dict_actual.items()):
                    orgs2update.append(dict_expected.copy())

    return orgs2update

class FilterModule(object):
    def filters(self):
        return {
            'grafana_missing_orgs': grafana_missing_orgs,
            'grafana_orgs2update': grafana_orgs2update
        }
