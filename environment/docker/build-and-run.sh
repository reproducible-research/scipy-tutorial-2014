#!/bin/sh

### "build-reproducible"
docker build -t reproducible .

### "build-convenience"
docker build -t reproducible/dexy - < ./Dockerfile-dexy
docker build -t reproducible/ipython - < ./Dockerfile-ipython
