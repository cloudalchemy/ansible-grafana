<p><img src="https://pbs.twimg.com/profile_images/806984496381886464/F7LUp1W2.jpg" alt="grafana logo" title="grafana" align="right" height="60" /></p>

Ansible Role: grafana
===================

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-grafana.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-grafana) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.grafana-blue.svg)](https://galaxy.ansible.com/cloudalchemy/grafana/) [![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-grafana.svg)](https://github.com/cloudalchemy/ansible-grafana/tags)

Grafana - platform for analytics and monitoring

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - cloudalchemy.grafana
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
