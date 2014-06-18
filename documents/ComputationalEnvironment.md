# Computational Environment

## Docker

## VirtualBox / Vagrant / Ansible

VirtualBox, Vagrant, and Ansible are required. Follow the steps below:

### Linux / Ubuntu  

> sudo apt-get install vagrant  
> sudo apt-get install ansible  

### MacOS and Windows

Install vagrant from here: http://www.vagrantup.com/downloads.html  

-------------

Once installed, open a new console and change directory to  
scipy-tutorial-2014/scripts/vagrant. 

> cd scipy-tutorial-2014/scripts/vagrant
> vagrant box add hashicorp/precise64 https://vagrantcloud.com/hashicorp/precise64/version/2/provider/virtualbox.box
> vagrant up

## Manual

Run the *check_env.py* script to ensure that all required Python packages and executables are installed.




