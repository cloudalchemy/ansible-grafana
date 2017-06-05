<p><img src="https://pbs.twimg.com/profile_images/806984496381886464/F7LUp1W2.jpg" alt="grafana logo" title="grafana" align="right" height="60" /></p>

Ansible Role: grafana
===================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/grafana/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fgrafana/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18266.svg)](https://galaxy.ansible.com/SoInteractive/grafana/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Grafana - platform for analytics and monitoring

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.grafana
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
