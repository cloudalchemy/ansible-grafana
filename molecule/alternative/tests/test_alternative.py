import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/etc/grafana",
        "/var/log/grafana",
        "/var/lib/grafana",
        "/var/lib/grafana/dashboards",
        "/var/lib/grafana/plugins",
        "/var/lib/grafana/plugins/raintank-worldping-app"
    ]
    files = [
        "/etc/grafana/grafana.ini"
    ]
    for directory in dirs:
        d = host.file(directory)
        assert d.is_directory
        assert d.exists
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    s = host.service("grafana-server")
    assert s.is_enabled
    assert s.is_running


def test_packages(host):
    p = host.package("grafana")
    assert p.is_installed
    assert p.version == "5.0.0"


def test_socket(host):
    assert host.socket("tcp://127.0.0.1:3000").is_listening
