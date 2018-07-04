import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_install_vim(host):
    if host.system_info.distribution == 'debian':
        assert host.package("vim").is_installed
    if host.system_info.distribution == 'centos':
        assert host.package("vim-enhanced").is_installed


def test_configure_vim(host):
    assert host.file("/etc/vim/supportedvimrc").exists


def test_install_docker(host):
    if host.system_info.distribution == 'debian':
        assert host.package("docker.io").is_installed
    if host.system_info.distribution == 'centos':
        assert host.package("docker").is_installed


# TODO: Enable Docker service
def test_docker_service(host):
    assert host.service("docker").is_running
    assert host.service("docker").is_enabled


def test_install_git(host):
    assert host.package("git").is_installed


def test_install_virtualbox(host):
    # TODO: Check repo added
    if host.system_info.distribution == 'debian':
        assert host.package("virtualbox").is_installed
    if host.system_info.distribution == 'centos':
        assert host.package("VirtualBox-5.1").is_installed


def test_install_tmux(host):
    assert host.package("tmux").is_installed


# TODO: Test tmux config
# def test_config_tmux(host):
#    assert host.file("/etc/tmux.conf").exists


def test_install_vscode(host):
    # TODO: Check repo added
    assert host.package("code").is_installed


# TODO: Install VSCode Plugins

# TODO: Install Sublime
# def test_install_sublime(host):
#     assert host.package("docker").is_installed

# TODO: Sublime plugins

# TODO: Install ZSH and OhMyZSH

# TODO: Configure ZSH/OhMyZSH
