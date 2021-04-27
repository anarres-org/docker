import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "package",
    [
        ("docker-ce"),
        ("python3-pip"),
    ],
)
def test_required_packages_exist(host, package):
    pkg = host.package(package)
    assert pkg.is_installed


@pytest.mark.parametrize(
    "pip_package",
    [
        ("docker"),
    ],
)
def test_required_pip_packages_exist(host, pip_package):
    pip_packages = host.pip_package.get_packages()
    assert pip_package in pip_packages


def test_gpg_through_key_apt_repository_file(host):
    fd = host.file("/etc/apt/sources.list.d/download_docker_com_linux_debian.list")
    fu = host.file("/etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list")
    assert fd.exists or fu.exists
    assert fd.user == "root" or fu.user == "root"
    assert fd.group == "root" or fu.group == "root"
    assert fd.contains("https://download.docker.com/linux/debian") or fu.contains(
        "https://download.docker.com/linux/ubuntu"
    )
