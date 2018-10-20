#!/usr/bin/env python
from ansible.errors import AnsibleError, AnsibleFilterError
import json

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

class FilterModule(object):
    def filters(self):
        return {
            'grafana_missing_orgs': grafana_missing_orgs
        }
