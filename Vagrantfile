# -*- mode: ruby -*-
# vi: set ft=ruby :

PROJECT_NAME = "iban_app"
PROJECT_SRC_DIR = "/var/iban_app/src"

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 9000, host: 9000
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 35729, host: 35729
  config.vm.network "private_network", ip: "192.168.10.10"

  config.vm.synced_folder "./src", PROJECT_SRC_DIR

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    vb.name = PROJECT_NAME
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
    ansible.extra_vars = {
      V_PROJECT_NAME: PROJECT_NAME,
      V_PROJECT_SRC_DIR: PROJECT_SRC_DIR,
    }
  end
end
