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

## Build the Docker Images


We need to build the Docker *images*, our reproducible computational
environments. Docker images are built from a set of instructions, the
[Dockerfile](http://docs.docker.com/reference/builder/).
After changing to the current directory,
`scipy-tutorial-2014/environement/docker`, build the base image:

{{ d['build-and-run.sh|idio']['build-reproducible'] }}

At the end of the build process, you should see output like this:

```
Successfully built 0bce0a1b0cf0
```

We can also build two other convenience images built on top of our
*reproducible* image. These will be used to run just the `dexy` command
or to start up the IPython notebook.

{{ d['build-and-run.sh|idio']['build-convenience'] }}

At the end of the build processes, you should set output like these:

```
Successfully built e396018d878e
```

```
Successfully built a276b59c9c8d
```


## Running Docker

To enter the *image*,

{{ d['enter-environment.sh|idio']['enter'] }}

You are now in a Docker *container*. The *-i -t* flags tells docker to start
up a pseudo-terminal and keep stdin open. Enter `exit` to exit the shell.

To start the IPython notebook,

{{ d['build-and-run.sh|idio']['start-ipython'] }}

This runs the Docker *container* in the background, makes the ports listening
available on the host, mounts the current working directory, and gives the
container the name *ipython*.

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

To stop and remove the container,

{{ d['build-and-run.sh|idio']['ipython-stop'] }}

For a full list of docker commands or docker subcommand help, enter *docker*
or *docker subcommand* with no arguments.

{{ d['build-and-run.sh|idio']['docker-help'] }}

It is also possible to [share your Docker images](https://hub.docker.com/)
with the [push](https://docs.docker.com/reference/commandline/cli/#push)
and [export](https://docs.docker.com/reference/commandline/cli/#export) commands.
