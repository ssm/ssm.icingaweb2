import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    p = host.package("icingaweb2")
    assert p.is_installed


def test_service(host):
    s = host.service('icingaweb2')
    assert s.is_running
    assert s.is_enabled
