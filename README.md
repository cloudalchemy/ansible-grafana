<p><img src="https://grafana.com/blog/assets/img/blog/timeshift/grafana_release_icon.png" alt="grafana logo" title="grafana" align="right" height="60" /></p>

# Ansible Role: grafana

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-grafana.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-grafana)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.grafana-blue.svg)](https://galaxy.ansible.com/cloudalchemy/grafana/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-grafana.svg)](https://github.com/cloudalchemy/ansible-grafana/tags)
[![IRC](https://img.shields.io/badge/irc.freenode.net-%23cloudalchemy-yellow.svg)](https://kiwiirc.com/nextclient/#ircs://irc.freenode.net/#cloudalchemy)

Provision and manage [grafana](https://github.com/grafana/grafana) - platform for analytics and monitoring

## Requirements

- Ansible >= 2.3
- libselinux-python on deployer host (only when deployer machine has SELinux)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `grafana_system_user` | grafana | Grafana server system user |
| `grafana_system_group` | grafana | Grafana server system group |
| `grafana_version` | latest | Grafana package version |
| `grafana_instance` | {{ ansible_fqdn \| default(ansible_host) \| default(inventory_hostname) }} | Grafana instance name |
| `grafana_logs_dir` | /var/log/grafana | Path to logs directory |
| `grafana_data_dir` | /var/lib/grafana | Path to database directory |
| `grafana_address` | 0.0.0.0 | Address on which grafana listens |
| `grafana_port` | 3000 | port on which grafana listens |
| `grafana_url` | "http://{{ grafana_address }}:{{ grafana_port }}" | Full URL used to access Grafana from a web browser |
| `grafana_domain` | "{{ ansible_fqdn \| default(ansible_host) \| default('localhost') }}" | setting is only used in as a part of the `root_url` option. Useful when using GitHub or Google OAuth |
| `grafana_server` | { protocol: http, enforce_domain: false, socket: "", cert_key: "", cert_file: "", enable_gzip: False, static_root_path: public, router_logging: false } | [server](http://docs.grafana.org/installation/configuration/#server) configuration section |
| `grafana_security` | { admin_user: admin, admin_password: "" } | [security](http://docs.grafana.org/installation/configuration/#security) configuration section |
| `grafana_database` | { type: sqlite3 } | [database](http://docs.grafana.org/installation/configuration/#database) configuration section |
| `grafana_welcome_email_on_sign_up` | False | Send welcome email after signing up |
| `grafana_users` | { allow_sign_up: False, auto_assign_org_role: Viewer, default_theme: dark } | [users](http://docs.grafana.org/installation/configuration/#users) configuration section |
| `grafana_auth` | {} | [authorization](http://docs.grafana.org/installation/configuration/#auth) configuration section |
| `grafana_session` | {} | [session](http://docs.grafana.org/installation/configuration/#session) management configuration section |
| `grafana_analytics` | {} | Google [analytics](http://docs.grafana.org/installation/configuration/#analytics) configuration section |
| `grafana_smtp` | {} | [smtp](http://docs.grafana.org/installation/configuration/#smtp) configuration section |
| `grafana_alerting` | True | [alerting](http://docs.grafana.org/installation/configuration/#alerting) configuration section |
| `grafana_metrics` | {} | [metrics](http://docs.grafana.org/installation/configuration/#metrics) configuration section |
| `grafana_tracing` | {} | [tracing](http://docs.grafana.org/installation/configuration/#tracing) configuration section |
| `grafana_snapshots` | {} | [snapshots](http://docs.grafana.org/installation/configuration/#snapshots) configuration section |
| `grafana_image_storage` | {} | [image storage](http://docs.grafana.org/installation/configuration/#external-image-storage) configuration section |
| `grafana_dashboards` | [] | List of dashboards which should be imported |
| `grafana_datasources` | [] | List of datasources which should be configured |

## Supported CPU Architectures

Detection is done automatically and packages are taken from different channels according to CPU architecture:

- amd64 - via official grafana packages ([1](http://docs.grafana.org/installation/debian/#installing-on-debian-ubuntu), [2](http://docs.grafana.org/installation/rpm/))
- armv6/armv7 and aarch64/arm64 - via [unofficial packages distributed by fg2it](https://github.com/fg2it/grafana-on-raspberry)

## Example

### Playbook

```yaml
- hosts: all
  become: true
  roles:
    - cloudalchemy.grafana
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on [DigitalOcean](https://digitalocean.com).

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible 'ansible-lint>=3.4.15' 'molecule>2.13.0' docker 'testinfra>=1.7.0' jmespath
```
This should be similar to one listed in `.travis.yml` file in `install` section.
After installing test suit you can run test by running
```sh
molecule test --all
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix (42 parallel role executions in case of [ansible-prometheus](https://github.com/cloudalchemy/ansible-prometheus)) which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
