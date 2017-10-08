import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_gpg_through_key_apt_repository_file(host):
    f = host.file('/etc/apt/sources.list.d/download_docker_com_linux_debian.li'
                  'st')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'
    assert f.contains('https://download.docker.com/linux/debian')
