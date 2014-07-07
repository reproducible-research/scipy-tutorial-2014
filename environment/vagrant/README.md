Vagrant Computational Environment Creation
==========================================

[VirtualBox](https://www.virtualbox.org), [Vagrant](http://www.vagrantup.com) >= 1.1,
and [Ansible](http://www.ansible.com/) are required. Follow the steps below:

Installation
------------

### Linux / Ubuntu

{{ d['install-and-generate.sh|idio']['install-vagrant-ansible'] }}

### MacOS and Windows

Install vagrant from [here](http://www.vagrantup.com/downloads.html)

Generation
----------

Once installed, open a new console and change directory to
scipy-tutorial-2014/environment/vagrant.

{{ d['install-and-generate.sh|idio']['generate-vagrant'] }}

To connect to the machine:

    vagrant ssh

To shutdown the virtual machine:

{{ d['install-and-generate.sh|idio']['vagrant-shutdown'] }}
