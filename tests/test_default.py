from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    present = [
        "/etc/grafana",
        "/var/log/grafana",
        "/var/lib/grafana",
        "/var/lib/grafana/dashboards",
        "/var/lib/grafana/plugins",
        "/var/lib/grafana/plugins/raintank-worldping-app"
    ]
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists


def test_files(host):
    present = [
        "/etc/grafana/grafana.ini"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_service(host):
    present = [
        "grafana-server"
    ]
    if present:
        for service in present:
            s = host.service(service)
            assert s.is_enabled


def test_packages(host):
    present = [
        "grafana"
    ]
    if present:
        for package in present:
            p = host.package(package)
            assert p.is_installed


def test_socket(host):
    present = [
        # "tcp://0.0.0.0:3000"
        "tcp://127.0.0.1:3000"
    ]
    for socket in present:
        s = host.socket(socket)
        assert s.is_listening
