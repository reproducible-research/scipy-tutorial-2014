#!/bin/sh
set -e

### "build-reproducible"
docker build -t reproducible/base .

### "build-dexy"
docker build -t reproducible/dexy dexy

### "build-ipython"
docker build -t reproducible/ipython ipython

### "run-dexy"
docker run --rm -v $PWD/../../notebooks/dexy:/home/repro reproducible/dexy

### "start-ipython"
docker run -d -P -v $PWD/../../notebooks:/home/repro --name ipython reproducible/ipython

### "ipython-ps"
docker ps
docker port ipython 8888

### "ipython-stop"
docker stop ipython
docker rm ipython
