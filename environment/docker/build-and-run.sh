#!/bin/sh

### "build-reproducible"
docker build -t reproducible .

### "build-convenience"
docker build -t reproducible/dexy - < ./Dockerfile-dexy
docker build -t reproducible/ipython - < ./Dockerfile-ipython

### "run-dexy"
cd ../../../scipy-tutorial-2014/dexy
#docker run -v $PWD:/home/reproducible reproducible/dexy

### "start-ipython"
cd ../../../scipy-tutorial-2014/notebooks
docker run -d -P -v $PWD:/home/reproducible --name ipython reproducible/ipython

### "ipython-ps"
docker ps
docker port ipython 8888

### "ipython-stop"
docker stop ipython
docker rm ipython

### "docker-help"
docker
docker start
