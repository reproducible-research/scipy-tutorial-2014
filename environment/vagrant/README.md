Vagrant Computational Environment Creation
==========================================

[VirtualBox](https://www.virtualbox.org), [Vagrant](http://www.vagrantup.com) >= 1.1,
and [Ansible](http://www.ansible.com/) are required. Follow the steps below:

Installation
------------

### Linux / Ubuntu

```
sudo apt-get install vagrant
sudo apt-get install ansible
```

### MacOS and Windows

Install vagrant from [here](http://www.vagrantup.com/downloads.html)

Generation
----------

Once installed, open a new console and change directory to
scipy-tutorial-2014/environment/vagrant.

```
cd scipy-tutorial-2014/environment/vagrant
vagrant box add hashicorp/precise64 https://vagrantcloud.com/hashicorp/precise64/version/2/provider/virtualbox.box
vagrant up
```

To connect to the machine:

```
vagrant ssh
```

To shutdown the virtual machine:

```
vagrant halt
```
