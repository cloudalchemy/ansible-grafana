<p><img src="https://grafana.com/blog/assets/img/blog/timeshift/grafana_release_icon.png" alt="grafana logo" title="grafana" align="right" height="60" /></p>

# Ansible Role: grafana

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-grafana.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-grafana) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.grafana-blue.svg)](https://galaxy.ansible.com/cloudalchemy/grafana/) [![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-grafana.svg)](https://github.com/cloudalchemy/ansible-grafana/tags)

Provision and manage Grafana server - platform for analytics and monitoring

## Requirements

This role installs everything it can by itself. It won't install or configure 3rd party apps (ex. nginx for reverse proxy).

## Role Variables

All variables with sane examples are defined in [defaults/main.yml](defaults/main.yml). Take a look there.
Those variables easily map to [grafana configuration](http://docs.grafana.org/installation/configuration/#configuration). For example variable `grafana_server` is responsible for section `server` in INI configuration file.

## Dependencies

None

## Example usage

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - cloudalchemy.grafana
```

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
