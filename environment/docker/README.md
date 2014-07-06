# Docker Compute Environment

![Docker logo](https://pbs.twimg.com/profile_images/378800000124779041/fbbb494a7eef5f9278c6967b6072ca3e_400x400.png)

In this hands-on exercise, we will learn how to create and use a reproducible
computational environment with Docker.

[TOC]

## Installing Docker

You must already have [Docker](http://docker.io) installed. See the [Docker
installation documention](http://docs.docker.com/installation/#installation)
for more information.

In general this means having a properly configure kernel and the docker client
and daemon installed on a Linux distribution. On Mac or Windows, the
installation installation instructions will install a `boot2docker` utility to
manage a VirtualBox virtual machine running the docker client and daemon.

## Build the Docker Base Image

We need to build the Docker *images*, our reproducible computational
environments. Docker images are built from a set of instructions, the
[Dockerfile](http://docs.docker.com/reference/builder/).

After changing to the current directory `scipy-tutorial-2014/environement/docker`,
build the base image via:

{{ d['build-and-run.sh|idio']['build-reproducible'] }}

It's also possible to use the pregenerated Docker image from the Docker Hub, via:

{{ d['hub-docker-image.sh|idio']['remove'] }}

## Running Docker

To launch the base image and open a shell:

{{ d['enter-environment.sh|idio']['enter'] }}

You are now in a Docker *container*. The *-i -t* flags tells docker to start
up a pseudo-terminal and keep stdin open. Enter `exit` to exit the shell.

This runs the Docker *container* in the background, makes the ports listening
available on the host, mounts the current working directory, and gives the
container the name *ipython*.


## Non-Interactive Containers

We can also configure containers to perform unattended tasks.

### Dexy Image

We can build other images on top of `reproducible/base` to handle common tasks.

{% set dimg = "Dockerfile-dexy" %}

The `{{ dimg }}` image is used to run the `dexy` command.

Here's the Dockerfile:

{{ d[dimg + "|idio"] }}

It's built via:

{{ d['build-and-run.sh|idio']['build-dexy'] }}

And run via:

{{ d['build-and-run.sh|idio']['run-dexy'] }}

This mounts the `scipy-tutorial-2014/dexy` directory within the container and
then runs dexy. The dexy-generated output files are present on your local file
system after the container exits because of the volume mounting.

### IPython Image

{% set dimg = "Dockerfile-ipython" %}

The `{{ dimg }}` image is used to launch the IPython notebook server.

Here's the Dockerfile:

{{ d[dimg + "|idio"] }}

It's built via:

{{ d['build-and-run.sh|idio']['build-ipython'] }}

To launch a non-interactive container which will run the IPython notebook
server and forward the port IPython is running on, do:

{{ d['build-and-run.sh|idio']['start-ipython'] }}

To get information on the containers running and the ports available from a
given container,

{{ d['build-and-run.sh|idio']['ipython-ps'] }}

If this returns *0.0.0.0:49153*, we will use the *49153* port.  On Linux, point
your browser to [http://localhost:49153](http://localhost:49153). On Mac on
Windows, use `boot2docker` to find the correct IP address,

```
boot2docker ip
```

If this returns *192.168.59.103*, then point your browser to
[http://192.168.59.103:49153](http://192.168.59.103:49153).

To stop and remove the container:

{{ d['build-and-run.sh|idio']['ipython-stop'] }}

## Docker Help

For a full list of docker commands or docker subcommand help, enter *docker*
or *docker subcommand* with no arguments.

{{ d['help.sh|idio|shint|pyg']['main-help'] }}

{{ d['help.sh|idio|shint|pyg']['subcommand-help'] }}
