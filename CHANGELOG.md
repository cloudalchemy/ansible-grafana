# Change Log

## [**Next release**](https://galaxy.ansible.com/cloudalchemy/grafana)

**Merged pull requests:**

- extending regex to match multiple subsequent words in datasource placeholder [\#53](https://github.com/cloudalchemy/ansible-grafana/pull/53) ([aman0019](https://github.com/aman0019))
- Use newer test filter schema to get rid of some deprecation warnings. [\#52](https://github.com/cloudalchemy/ansible-grafana/pull/52) ([swesterveld](https://github.com/swesterveld))
- change way releases work; update license year [\#51](https://github.com/cloudalchemy/ansible-grafana/pull/51) ([paulfantom](https://github.com/paulfantom))

## [0.8.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-04-13)
**Merged pull requests:**

- Make grafana.ini template compatible with both Python 2 and 3 [\#50](https://github.com/cloudalchemy/ansible-grafana/pull/50) ([nikosgraser](https://github.com/nikosgraser))

## [0.8.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-04-03)
**Merged pull requests:**

- Add ability to generate API keys [\#49](https://github.com/cloudalchemy/ansible-grafana/pull/49) ([odyssey4me](https://github.com/odyssey4me))

## [0.7.16](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-26)
**Closed issues:**

- plugins don't work if grafana\_data\_dir != "/var/lib/grafana" [\#38](https://github.com/cloudalchemy/ansible-grafana/issues/38)

**Merged pull requests:**

- ansible 2.5 [\#48](https://github.com/cloudalchemy/ansible-grafana/pull/48) ([paulfantom](https://github.com/paulfantom))

## [0.7.15](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-25)
**Merged pull requests:**

- fix plugins installation in non-default directory [\#47](https://github.com/cloudalchemy/ansible-grafana/pull/47) ([paulfantom](https://github.com/paulfantom))

## [0.7.14](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-25)
**Merged pull requests:**

- dashboards: Make the regex much more specific [\#45](https://github.com/cloudalchemy/ansible-grafana/pull/45) ([odyssey4me](https://github.com/odyssey4me))

## [0.7.13](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-23)
**Merged pull requests:**

- datasources: Allow additional datasources to be created later [\#46](https://github.com/cloudalchemy/ansible-grafana/pull/46) ([odyssey4me](https://github.com/odyssey4me))

## [0.7.12](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-22)
**Merged pull requests:**

- vars: Handle the use of grafana\_version='latest' properly [\#44](https://github.com/cloudalchemy/ansible-grafana/pull/44) ([odyssey4me](https://github.com/odyssey4me))

## [0.7.11](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-22)
**Merged pull requests:**

- local task should be ran only once [\#43](https://github.com/cloudalchemy/ansible-grafana/pull/43) ([paulfantom](https://github.com/paulfantom))

## [0.7.10](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-22)
**Merged pull requests:**

- Add fedora support/testing [\#42](https://github.com/cloudalchemy/ansible-grafana/pull/42) ([odyssey4me](https://github.com/odyssey4me))

## [0.7.9](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-22)
**Merged pull requests:**

- travis: Automatically use the latest Ansible patch releases [\#41](https://github.com/cloudalchemy/ansible-grafana/pull/41) ([odyssey4me](https://github.com/odyssey4me))
- Improve efficiency and resiliency for the installation [\#40](https://github.com/cloudalchemy/ansible-grafana/pull/40) ([odyssey4me](https://github.com/odyssey4me))

## [0.7.8](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-22)
**Closed issues:**

- systemd for grafana [\#36](https://github.com/cloudalchemy/ansible-grafana/issues/36)

**Merged pull requests:**

- Add Ubuntu Bionic support/testing [\#39](https://github.com/cloudalchemy/ansible-grafana/pull/39) ([odyssey4me](https://github.com/odyssey4me))

## [0.7.7](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-11)
**Fixed bugs:**

- Start grafana-server [\#37](https://github.com/cloudalchemy/ansible-grafana/pull/37) ([bngsudheer](https://github.com/bngsudheer))

## [0.7.6](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-03-07)
**Closed issues:**

- Additional quote is breaking password authentications [\#32](https://github.com/cloudalchemy/ansible-grafana/issues/32)

**Merged pull requests:**

- Upgrade to 5.0 [\#35](https://github.com/cloudalchemy/ansible-grafana/pull/35) ([paulfantom](https://github.com/paulfantom))

## [0.7.5](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-02-21)
**Merged pull requests:**

- Removed additional quotes that broke password auth [\#33](https://github.com/cloudalchemy/ansible-grafana/pull/33) ([D3N14L](https://github.com/D3N14L))

## [0.7.4](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-02-13)
**Merged pull requests:**

- Make Grafana-server restart with sudo privileges. [\#31](https://github.com/cloudalchemy/ansible-grafana/pull/31) ([swesterveld](https://github.com/swesterveld))

## [0.7.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-01-14)
**Merged pull requests:**

- More operating systems and cleanup [\#29](https://github.com/cloudalchemy/ansible-grafana/pull/29) ([paulfantom](https://github.com/paulfantom))

## [0.7.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-01-11)
**Merged pull requests:**

- support plugin installation [\#28](https://github.com/cloudalchemy/ansible-grafana/pull/28) ([paulfantom](https://github.com/paulfantom))

## [0.7.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-01-05)
**Merged pull requests:**

- Remove unneeded apostrophes in grafana\_datasources [\#27](https://github.com/cloudalchemy/ansible-grafana/pull/27) ([swesterveld](https://github.com/swesterveld))
- docs [\#26](https://github.com/cloudalchemy/ansible-grafana/pull/26) ([paulfantom](https://github.com/paulfantom))

## [0.7.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-01-02)
**Implemented enhancements:**

- support multiple grafana versions [\#13](https://github.com/cloudalchemy/ansible-grafana/issues/13)
- Support passing datasources as YAML files [\#9](https://github.com/cloudalchemy/ansible-grafana/issues/9)

**Merged pull requests:**

- Update generatetag.sh [\#25](https://github.com/cloudalchemy/ansible-grafana/pull/25) ([paulfantom](https://github.com/paulfantom))
- support selecting grafana version [\#24](https://github.com/cloudalchemy/ansible-grafana/pull/24) ([paulfantom](https://github.com/paulfantom))
- support older raspberry pi [\#23](https://github.com/cloudalchemy/ansible-grafana/pull/23) ([paulfantom](https://github.com/paulfantom))

## [0.6.4](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-01-01)
**Merged pull requests:**

- add datasources in yaml file [\#21](https://github.com/cloudalchemy/ansible-grafana/pull/21) ([paulfantom](https://github.com/paulfantom))

## [0.6.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-12-29)
**Closed issues:**

- Readme [\#14](https://github.com/cloudalchemy/ansible-grafana/issues/14)

**Merged pull requests:**

- WIP: preflight checks [\#20](https://github.com/cloudalchemy/ansible-grafana/pull/20) ([paulfantom](https://github.com/paulfantom))

## [0.6.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-12-27)
**Merged pull requests:**

- Readme refactoring [\#22](https://github.com/cloudalchemy/ansible-grafana/pull/22) ([paulfantom](https://github.com/paulfantom))

## [0.6.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-12-15)
**Implemented enhancements:**

- Support all configuration options [\#7](https://github.com/cloudalchemy/ansible-grafana/issues/7)

**Merged pull requests:**

- change duplicate parsing of security section [\#19](https://github.com/cloudalchemy/ansible-grafana/pull/19) ([bolek2000](https://github.com/bolek2000))

## [0.6.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-12-09)
**Merged pull requests:**

- support almost every grafana configuration option \(apart from "log"\) [\#15](https://github.com/cloudalchemy/ansible-grafana/pull/15) ([paulfantom](https://github.com/paulfantom))

## [0.5.6](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-12-06)
**Merged pull requests:**

- Debian support in Ansible Galaxy [\#17](https://github.com/cloudalchemy/ansible-grafana/pull/17) ([paulfantom](https://github.com/paulfantom))

## [0.5.5](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-12-06)
**Implemented enhancements:**

- Testinfra new fixtures [\#10](https://github.com/cloudalchemy/ansible-grafana/issues/10)

**Merged pull requests:**

- Stop pipeline on any error [\#18](https://github.com/cloudalchemy/ansible-grafana/pull/18) ([paulfantom](https://github.com/paulfantom))

## [0.5.4](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-12-03)
**Merged pull requests:**

- remove deprecated fixtures [\#16](https://github.com/cloudalchemy/ansible-grafana/pull/16) ([paulfantom](https://github.com/paulfantom))

## [0.5.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-12-01)
**Merged pull requests:**

- Fix tagging [\#6](https://github.com/cloudalchemy/ansible-grafana/pull/6) ([paulfantom](https://github.com/paulfantom))

## [0.5.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-11-30)
**Merged pull requests:**

- Ansible 2.4.2 [\#5](https://github.com/cloudalchemy/ansible-grafana/pull/5) ([paulfantom](https://github.com/paulfantom))

## [0.5.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-11-30)
**Merged pull requests:**

- jsonify datasources [\#4](https://github.com/cloudalchemy/ansible-grafana/pull/4) ([paulfantom](https://github.com/paulfantom))

## [0.5.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-11-29)
**Merged pull requests:**

- Major cleanup [\#3](https://github.com/cloudalchemy/ansible-grafana/pull/3) ([paulfantom](https://github.com/paulfantom))

## [0.4.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-11-28)
**Merged pull requests:**

- fix CI; remove company from role description [\#2](https://github.com/cloudalchemy/ansible-grafana/pull/2) ([paulfantom](https://github.com/paulfantom))

## [0.4.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-11-28)
**Merged pull requests:**

- Old [\#1](https://github.com/cloudalchemy/ansible-grafana/pull/1) ([paulfantom](https://github.com/paulfantom))

## [0.4.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-10-16)
## [0.3.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-27)
## [0.3.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-27)
## [0.3.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-27)
## [0.3.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-21)
## [0.2.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-13)
## [0.2.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-13)
## [0.1.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-13)
## [0.1.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-06-14)
## [0.1.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-06-14)
## [0.1.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-06-05)
## [0.0.4](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-05-15)
## [0.0.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-05-05)
## [0.0.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-05-05)
## [0.0.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-03-31)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*