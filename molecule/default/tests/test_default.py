import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_install_vim(host):
    if host.system_info.distribution == 'debian':
        assert host.package("vim").is_installed
    if host.system_info.distribution == 'centos':
        assert host.package("vim-enhanced").is_installed


def test_install_docker(host):
    assert host.package("docker").is_installed


def test_install_git(host):
    assert host.package("git").is_installed


def test_install_virtualbox(host):
    if host.system_info.distribution == 'debian':
        assert host.package("virtualbox").is_installed
    if host.system_info.distribution == 'centos':
        assert host.package("VirtualBox-5.1").is_installed


def test_install_tmux(host):
    assert host.package("tmux").is_installed


def test_install_vscode(host):
    assert host.package("code").is_installed


# def test_install_sublime(host):
#     assert host.package("docker").is_installed
