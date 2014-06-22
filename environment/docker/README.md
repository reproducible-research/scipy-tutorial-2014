Docker Computational Environment Creation
=========================================

Installing Docker
-----------------

You must already have [docker](http://docker.io) installed. See http://docker.io for more information.

Build the Docker Images
-----------------------

We need to build the Docker images, our reproducible computational
environments.  First, build the base image.

```bash
docker build -t reproducible .
```

At the end of the build process, you should see output like this:

```
Successfully built 7b7bc4cbc144
```

We can also build two other convenience images built on top of our
*reproducible* image.

```bash
docker build -t reproducible/dexy - < ./Dockerfile-dexy
docker build -t reproducible/ipython - < ./Dockerfile-ipython
```


Running Docker
--------------

To enter the *image* with your HOME directory mounted as a *volume*

```bash
docker run -v $HOME:/home/reproducible -i -t reproducible /bin/bash
```

You are now in a Docker *container*. The *-i -t* tells docker to
start up a pseudo-terminal and keep stdin open. Enter *exit* to
exit the shell.

To run dexy,

```bash
cd ../../../scipy-tutorial-2014/dexy
docker run -v $PWD:/home/reproducible reproducible/dexy
```

To start the IPython notebook,

```bash
cd ../../scipy-tutorial-2014/notebooks
docker run -d -P -v $PWD:/home/reproducible --name ipython reproducible/ipython
```

This runs the Docker *container* in the background, makes the ports listening
available on the host, mounts the current working directory, and gives the
container the name *ipython*.

To get information on the containers running and the ports available from a
given container,

```bash
docker ps
docker port ipython 8888
```

If this returns *0.0.0.0:49155*, for example, point your browser to
http://localhost:49155.

To stop and remove the container,
```bash
docker stop
docker rm
```

For a full list of docker commands or docker subcommand help, enter *docker*
or *docker <subcommand>* with no arguments.

```bash
docker
docker start
```

It is also possible to share your Docker images on the web and archive them
with the *push* and *export* commands.
