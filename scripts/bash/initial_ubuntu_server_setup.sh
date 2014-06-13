#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install apt-file
sudo apt-file update
sudo apt-get install apache2
sudo apt-get install git
sudo apt-get install build-essential
sudo apt-get install nodejs
sudo apt-get install npm
sudo npm update
sudo apt-get install tmux
sudo apt-get install ipython
sudo apt-get install ipython-notebook
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install python-numpy
sudo apt-get install python-matplotlib

sudo easy_install SimpleITK

sudo adduser notebook
su notebook
cd
mkdir reproducible-research
cd    reproducible-research
git clone https://github.com/reproducible-research/scipy-tutorial-2014.git
cd scipy-tutorial-2014/notebooks
ipyton notebook --ip=*  --pylab=inline
