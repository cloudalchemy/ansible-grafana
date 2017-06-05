from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/etc/grafana",
        "/var/log/grafana",
        "/var/lib/grafana",
        "/var/lib/grafana/dashboards",
        "/var/lib/grafana/plugins"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/grafana/grafana.ini"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "grafana-server"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled


def test_packages(Package):
    present = [
        "grafana"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed


def test_socket(Socket):
    present = [
        # "tcp://0.0.0.0:3000"
        "tcp://127.0.0.1:3000"
    ]
    for socket in present:
        s = Socket(socket)
        assert s.is_listening
