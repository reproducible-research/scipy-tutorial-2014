#!/bin/sh
set -e

### "build-reproducible"
docker build -t reproducible/base .

### "build-dexy"
docker build -t reproducible/dexy - < ./Dockerfile-dexy

### "build-ipython"
docker build -t reproducible/ipython - < ./Dockerfile-ipython

### "run-dexy"
docker run --rm -v $PWD/../../dexy:/home/repro reproducible/dexy

### "start-ipython"
docker run -d -P -v $PWD/../../notebooks:/home/reproducible --name ipython reproducible/ipython

### "ipython-ps"
docker ps
docker port ipython 8888

### "ipython-stop"
docker stop ipython
docker rm ipython
