import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    s = host.service("grafana-server")
    # assert s.is_enabled
    assert s.is_running


def test_socket(host):
    assert host.socket("tcp://127.0.0.1:3000").is_listening
