# Docker Compute Environment

![Docker logo](http://www.docker.com/static/img/nav/docker-logo-loggedout.png)

In this hands-on exercise, we will learn how to create and use a reproducible
computational enviroment with Docker.

[TOC]

## Installing Docker

You must already have [Docker](http://docker.io) installed. See the [Docker
installation documention](http://docs.docker.com/installation/#installation)
for more information.

In general this means having a properly configure kernel and the docker client
and daemon installed on a Linux distribution. On Mac or Windows, the
installation installation instructions will install a `boot2docker` utility to
manage a VirtualBox virtual machine running the docker client and daemon.

## Build the Docker Images

We need to build the Docker *images*, our reproducible computational
environments. Docker images are built from a set of instructions, the
[Dockerfile](http://docs.docker.com/reference/builder/).
After changing to the current directory,
`scipy-tutorial-2014/environement/docker`, build the base image:

{{ d['build-and-run.sh|idio']['build-reproducible'] }}

At the end of the build process, you should see output like this:

```
Successfully built 7b7bc4cbc144
```

We can also build two other convenience images built on top of our
*reproducible* image. These will be used to run just the `dexy` command
or to start up the IPython notebook.

{{ d['build-and-run.sh|idio']['build-convenience'] }}


## Running Docker

To enter the *image*,

{{ d['enter-environment.sh|idio']['enter'] }}

You are now in a Docker *container*. The *-i -t* flags tells docker to start
up a pseudo-terminal and keep stdin open. Enter `exit` to exit the shell.

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
