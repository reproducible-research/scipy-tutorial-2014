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
sudo apt-get install ffmpeg
sudo apt-get install imagej

sudo easy_install SimpleITK


#
# Installing dexy
#
sudo pip install dexy


#
# Notebook scripts
#
sudo adduser notebook
su notebook
cd
mkdir reproducible-research
cd    reproducible-research
git clone https://github.com/reproducible-research/scipy-tutorial-2014.git
cd scipy-tutorial-2014/notebooks
ipython notebook --ip=*  --pylab=inline

#
# Girder
#
# http://girder.readthedocs.org/en/latest/prerequisites.html#ubuntu
#
sudo apt-get install mongodb
sudo apt-get install python-software-properties
sudo apt-get install libffi-dev

sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs

sudo adduser girder
su girder
cd
mkdir dataStore

git clone https://github.com/girder/girder.git
cd girder
sudo pip install -r requirements.txt
sudo npm install -g grunt grunt-cli
npm install
grunt init
grunt

mkdir /home/girder/mongodb

mongod --setParameter textSearchEnabled=true --dbpath=/home/girder/mongodb &

python -m girder
