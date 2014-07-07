#!/bin/sh
set -e

### "install-vagrant-ansible"
sudo apt-get install vagrant
sudo apt-get install ansible

### "generate-vagrant"
cd scipy-tutorial-2014/environment/vagrant
vagrant box add hashicorp/precise64 https://vagrantcloud.com/hashicorp/precise64/version/2/provider/virtualbox.box
vagrant up

### "vagrant-shutdown"
vagrant halt
