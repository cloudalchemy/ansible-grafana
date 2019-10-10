# Change Log


## [**Next release**](https://galaxy.ansible.com/cloudalchemy/grafana)

**Closed issues:**

- Add new auth configuration options [\#165](https://github.com/cloudalchemy/ansible-grafana/issues/165)
- playbook fails to starts the grafana server [\#163](https://github.com/cloudalchemy/ansible-grafana/issues/163)
- Support for installing plugins [\#159](https://github.com/cloudalchemy/ansible-grafana/issues/159)
- documentation example missing admin user requirement [\#156](https://github.com/cloudalchemy/ansible-grafana/issues/156)
- Importing dashboards will fail if datadir != /var/lib/grafana [\#147](https://github.com/cloudalchemy/ansible-grafana/issues/147)

**Merged pull requests:**

- Using tests as filters is deprecated. Changed to "result is search". [\#176](https://github.com/cloudalchemy/ansible-grafana/pull/176) ([lossos](https://github.com/lossos))
- Synchronize files from cloudalchemy/skeleton [\#172](https://github.com/cloudalchemy/ansible-grafana/pull/172) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Synchronize files from cloudalchemy/skeleton [\#171](https://github.com/cloudalchemy/ansible-grafana/pull/171) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Update minimum required ansible version [\#170](https://github.com/cloudalchemy/ansible-grafana/pull/170) ([cloudalchemybot](https://github.com/cloudalchemybot))
- add default serve\_from\_sub\_path option [\#169](https://github.com/cloudalchemy/ansible-grafana/pull/169) ([paulfantom](https://github.com/paulfantom))
- Moving to python 3 and dropping support for python 2.x \(on deployer host\) [\#168](https://github.com/cloudalchemy/ansible-grafana/pull/168) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Add new auth configuration options. [\#166](https://github.com/cloudalchemy/ansible-grafana/pull/166) ([leitgab](https://github.com/leitgab))
- Synchronize files from cloudalchemy/skeleton [\#164](https://github.com/cloudalchemy/ansible-grafana/pull/164) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Add support for running in socket mode [\#161](https://github.com/cloudalchemy/ansible-grafana/pull/161) ([RichardHeelin](https://github.com/RichardHeelin))
- Add documentation for var `grafana\_plugins` [\#160](https://github.com/cloudalchemy/ansible-grafana/pull/160) ([thescouser89](https://github.com/thescouser89))
- Update the playbook example \(\#156\) [\#157](https://github.com/cloudalchemy/ansible-grafana/pull/157) ([andrasbabos](https://github.com/andrasbabos))
- Add GnuPG2 as a dependency on Debian/Ubuntu  [\#154](https://github.com/cloudalchemy/ansible-grafana/pull/154) ([FinweVI](https://github.com/FinweVI))
- Synchronize files from cloudalchemy/skeleton [\#152](https://github.com/cloudalchemy/ansible-grafana/pull/152) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Add tag `grafana\_run` to give flexibility [\#151](https://github.com/cloudalchemy/ansible-grafana/pull/151) ([bryanspears](https://github.com/bryanspears))
- Correct package source for ARM in README. [\#149](https://github.com/cloudalchemy/ansible-grafana/pull/149) ([jcoleman](https://github.com/jcoleman))

## [0.14.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2019-03-25)
**Merged pull requests:**

- Replace hardcoded paths with data dir variable [\#148](https://github.com/cloudalchemy/ansible-grafana/pull/148) ([boutetnico](https://github.com/boutetnico))
- Synchronize files from cloudalchemy/skeleton. [\#146](https://github.com/cloudalchemy/ansible-grafana/pull/146) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.14.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2019-03-24)
**Merged pull requests:**

- default to only coping dashboards and not removing them [\#145](https://github.com/cloudalchemy/ansible-grafana/pull/145) ([paulfantom](https://github.com/paulfantom))

## [0.14.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2019-03-23)
**Implemented enhancements:**

- Use `tempfile` for `/tmp/dashboards` [\#90](https://github.com/cloudalchemy/ansible-grafana/issues/90)

**Fixed bugs:**

- WTF bug with grafana\_dashboards\_dir == dashboards [\#136](https://github.com/cloudalchemy/ansible-grafana/issues/136)
- Dashboard provisioning is interactive [\#128](https://github.com/cloudalchemy/ansible-grafana/issues/128)

**Closed issues:**

- 500 internal server error with packagecloud.io [\#133](https://github.com/cloudalchemy/ansible-grafana/issues/133)

**Merged pull requests:**

- Add logging configuration options [\#142](https://github.com/cloudalchemy/ansible-grafana/pull/142) ([boutetnico](https://github.com/boutetnico))
- Allow to override enabled parameter in auth block [\#141](https://github.com/cloudalchemy/ansible-grafana/pull/141) ([Igorshp](https://github.com/Igorshp))
- Add option to disable alert execution [\#139](https://github.com/cloudalchemy/ansible-grafana/pull/139) ([Duologic](https://github.com/Duologic))
- Remove files/dashboards directory [\#137](https://github.com/cloudalchemy/ansible-grafana/pull/137) ([amarao](https://github.com/amarao))
- Refactor dashboard provisioning [\#134](https://github.com/cloudalchemy/ansible-grafana/pull/134) ([paulfantom](https://github.com/paulfantom))
- Become root to import dashboards [\#129](https://github.com/cloudalchemy/ansible-grafana/pull/129) ([nikosmeds](https://github.com/nikosmeds))

## [0.13.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2019-01-08)
**Closed issues:**

- Problem installing on debian. Problems with repo and it's gpg key. [\#124](https://github.com/cloudalchemy/ansible-grafana/issues/124)

**Merged pull requests:**

- Replaced packagecloud repo with official Grafana repo [\#125](https://github.com/cloudalchemy/ansible-grafana/pull/125) ([wiktor2200](https://github.com/wiktor2200))
- Fixed quotation marks to backtick in README.md [\#123](https://github.com/cloudalchemy/ansible-grafana/pull/123) ([wvh-github](https://github.com/wvh-github))
- Enable the use of ports below 1024 [\#122](https://github.com/cloudalchemy/ansible-grafana/pull/122) ([wvh-github](https://github.com/wvh-github))
- Feature provisioning dashboards [\#121](https://github.com/cloudalchemy/ansible-grafana/pull/121) ([mxbossard](https://github.com/mxbossard))
- dashboard check should run on localhost [\#119](https://github.com/cloudalchemy/ansible-grafana/pull/119) ([wvh-github](https://github.com/wvh-github))
- Add support for multi-line ansible\_managed strings [\#116](https://github.com/cloudalchemy/ansible-grafana/pull/116) ([etcet](https://github.com/etcet))
- Fix \(\#99\) : allow custom yum repo template [\#105](https://github.com/cloudalchemy/ansible-grafana/pull/105) ([rockandska](https://github.com/rockandska))

## [0.12.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-12-04)
**Fixed bugs:**

- Preflight "tags: always" conflicts with --tags option [\#101](https://github.com/cloudalchemy/ansible-grafana/issues/101)

**Closed issues:**

- Dashboard title cannot be empty [\#108](https://github.com/cloudalchemy/ansible-grafana/issues/108)
- grafana\_admin ldap config template not handling boolean correctly [\#103](https://github.com/cloudalchemy/ansible-grafana/issues/103)

**Merged pull requests:**

- Allow disabling of Grafana alerts [\#115](https://github.com/cloudalchemy/ansible-grafana/pull/115) ([dominik-bln](https://github.com/dominik-bln))
- Only set alerting if variable is false [\#112](https://github.com/cloudalchemy/ansible-grafana/pull/112) ([wvh-github](https://github.com/wvh-github))
- Few smaller improvements, backward compatible [\#110](https://github.com/cloudalchemy/ansible-grafana/pull/110) ([krzyzakp](https://github.com/krzyzakp))
- Replaced tag always, which colidate when including role.  [\#109](https://github.com/cloudalchemy/ansible-grafana/pull/109) ([krzyzakp](https://github.com/krzyzakp))
- Fix: make curl fail when we encounter a 404 [\#107](https://github.com/cloudalchemy/ansible-grafana/pull/107) ([till](https://github.com/till))

## [0.11.4](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-10-11)
**Merged pull requests:**

- fixes for handling LDAP template booleans in grafana groups section \(issue \#103\) [\#104](https://github.com/cloudalchemy/ansible-grafana/pull/104) ([madeinoz67](https://github.com/madeinoz67))

## [0.11.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-10-07)
**Fixed bugs:**

- wrong file perm for datasources/ansible.yml [\#94](https://github.com/cloudalchemy/ansible-grafana/issues/94)

**Closed issues:**

- Enable jsonData in grafana\_datasources [\#100](https://github.com/cloudalchemy/ansible-grafana/issues/100)

**Merged pull requests:**

- move to ansible 2.7 [\#102](https://github.com/cloudalchemy/ansible-grafana/pull/102) ([paulfantom](https://github.com/paulfantom))
- use `become` where needed [\#98](https://github.com/cloudalchemy/ansible-grafana/pull/98) ([paulfantom](https://github.com/paulfantom))

## [0.11.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-09-12)
**Fixed bugs:**

- import grafana dashboards failed [\#77](https://github.com/cloudalchemy/ansible-grafana/issues/77)

**Merged pull requests:**

- Add become:yes to allow this module to be used in include\_role task [\#97](https://github.com/cloudalchemy/ansible-grafana/pull/97) ([jdbaldry](https://github.com/jdbaldry))
- Add vars file for openSUSE 42.x [\#96](https://github.com/cloudalchemy/ansible-grafana/pull/96) ([kaiokmo](https://github.com/kaiokmo))
- fixing issue \#94 [\#95](https://github.com/cloudalchemy/ansible-grafana/pull/95) ([nicosto](https://github.com/nicosto))

## [0.11.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-08-24)
**Closed issues:**

- Config for Elasticsearch datasource [\#89](https://github.com/cloudalchemy/ansible-grafana/issues/89)
- Pass variables through playbook [\#88](https://github.com/cloudalchemy/ansible-grafana/issues/88)
- Issue with grafana restart when including one or more datasources [\#85](https://github.com/cloudalchemy/ansible-grafana/issues/85)

**Merged pull requests:**

- Fixed syntax in default/main.yml to avoid unmarshal errors [\#93](https://github.com/cloudalchemy/ansible-grafana/pull/93) ([Dreeg](https://github.com/Dreeg))
- Use curl instead of get\_url to download dashboards [\#92](https://github.com/cloudalchemy/ansible-grafana/pull/92) ([paulfantom](https://github.com/paulfantom))
- cheat ansible idempotency when downloading dashboards [\#87](https://github.com/cloudalchemy/ansible-grafana/pull/87) ([paulfantom](https://github.com/paulfantom))
- Adding possibility to get right ownership on configuration files [\#86](https://github.com/cloudalchemy/ansible-grafana/pull/86) ([zonArt](https://github.com/zonArt))

## [0.11.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-08-10)
**Implemented enhancements:**

- Issues provisioning datasources on Grafana in private subnet [\#70](https://github.com/cloudalchemy/ansible-grafana/issues/70)
- Provision dashboards from file in addition to Grafana Dashboards [\#54](https://github.com/cloudalchemy/ansible-grafana/issues/54)
- Provisioning folders [\#30](https://github.com/cloudalchemy/ansible-grafana/issues/30)

**Fixed bugs:**

- \[Question\] Dashboard add is done twice [\#68](https://github.com/cloudalchemy/ansible-grafana/issues/68)

**Closed issues:**

- Use official repository for ARM builds [\#82](https://github.com/cloudalchemy/ansible-grafana/issues/82)
- Datasource provision does not specify the apiVersion [\#73](https://github.com/cloudalchemy/ansible-grafana/issues/73)
- adding datasource fails  [\#72](https://github.com/cloudalchemy/ansible-grafana/issues/72)
- preflight checks [\#8](https://github.com/cloudalchemy/ansible-grafana/issues/8)

**Merged pull requests:**

- repeat plugin installation on network failure [\#84](https://github.com/cloudalchemy/ansible-grafana/pull/84) ([paulfantom](https://github.com/paulfantom))
- simplify installation and use official ARM builds [\#83](https://github.com/cloudalchemy/ansible-grafana/pull/83) ([paulfantom](https://github.com/paulfantom))
- use grafana\_datasource [\#81](https://github.com/cloudalchemy/ansible-grafana/pull/81) ([paulfantom](https://github.com/paulfantom))
- allow importing local dashboards [\#80](https://github.com/cloudalchemy/ansible-grafana/pull/80) ([paulfantom](https://github.com/paulfantom))
- Drop ansible 2.4 support [\#78](https://github.com/cloudalchemy/ansible-grafana/pull/78) ([paulfantom](https://github.com/paulfantom))
- datasource format fix [\#76](https://github.com/cloudalchemy/ansible-grafana/pull/76) ([XooR](https://github.com/XooR))
- Add separate grafana\_api\_url variable [\#71](https://github.com/cloudalchemy/ansible-grafana/pull/71) ([thejchap](https://github.com/thejchap))

## [0.10.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-07-07)
**Merged pull requests:**

- Use 'provisioning' capability when possible [\#69](https://github.com/cloudalchemy/ansible-grafana/pull/69) ([rockandska](https://github.com/rockandska))

## [0.10.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-07-01)
**Merged pull requests:**

- use tox, ansible 2.6, and allow using remote docker host [\#67](https://github.com/cloudalchemy/ansible-grafana/pull/67) ([paulfantom](https://github.com/paulfantom))
- Add examples for datasource and dashboard configs [\#66](https://github.com/cloudalchemy/ansible-grafana/pull/66) ([bitfag](https://github.com/bitfag))

## [0.9.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-06-16)
**Closed issues:**

- Dashboard datasource regex does not match for some dashboards [\#59](https://github.com/cloudalchemy/ansible-grafana/issues/59)
- Add LDAP configuration support [\#11](https://github.com/cloudalchemy/ansible-grafana/issues/11)

**Merged pull requests:**

- Add LDAP configuration tasks [\#65](https://github.com/cloudalchemy/ansible-grafana/pull/65) ([lae](https://github.com/lae))
- add tags [\#64](https://github.com/cloudalchemy/ansible-grafana/pull/64) ([paulfantom](https://github.com/paulfantom))
- fix non-informative task name [\#62](https://github.com/cloudalchemy/ansible-grafana/pull/62) ([paulfantom](https://github.com/paulfantom))
- add ability to define notification channels [\#61](https://github.com/cloudalchemy/ansible-grafana/pull/61) ([sarphram](https://github.com/sarphram))

## [0.8.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2018-05-22)
**Fixed bugs:**

- Incorrect location for datasources provisioning directory [\#55](https://github.com/cloudalchemy/ansible-grafana/issues/55)

**Merged pull requests:**

- Update datasource regex match to include dashes and numbers [\#60](https://github.com/cloudalchemy/ansible-grafana/pull/60) ([odyssey4me](https://github.com/odyssey4me))
- upgrade to molecule 2.x [\#57](https://github.com/cloudalchemy/ansible-grafana/pull/57) ([paulfantom](https://github.com/paulfantom))
- fix incorrect provisioning directory placing [\#56](https://github.com/cloudalchemy/ansible-grafana/pull/56) ([paulfantom](https://github.com/paulfantom))
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
## [0.3.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-27)
## [0.3.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-27)
## [0.3.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-27)
## [0.3.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-21)
## [0.1.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-13)
## [0.2.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-13)
## [0.2.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-07-13)
## [0.1.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-06-14)
## [0.1.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-06-14)
## [0.1.0](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-06-05)
## [0.0.4](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-05-15)
## [0.0.3](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-05-05)
## [0.0.2](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-05-05)
## [0.0.1](https://galaxy.ansible.com/cloudalchemy/grafana) (2017-03-31)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*
