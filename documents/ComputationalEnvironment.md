# Computational Environment

Even though computers are often considered deterministic, computational
software is a rapidly evolving and changing landscape. Libraries are constantly
adding new features and fixing issues. Even libraries with the strictest
backwards-compatibility policies can change in significant ways. As computer
hardware evolves, software is forced to adapt accordingly.

A reproducible computational environment is sufficiently consistent for the
computational task at hand. For example, this can consist of a similar CPU
instruction set, libraries and executables available with a specific version
and configuration options, a specific operating system version, etc.

## Docker

<img alt="Docker stack" src="http://tiewei.github.io/images/docker-filesystems-multilayer.png" width="350">

Docker is an open-source engine that automates the deployment of any
application as a lightweight, portable, self-sufficient container that will run
virtually anywhere.

<img alt="Container vs VMs" src="http://tiewei.github.io/images/docker_vm.jpg" width="350">

Docker works with images that consume minimal disk space, versioned, archiveable, and shareable.
Executing applications in these images does not require dedicated resources and is high performance.
For more information on Docker [please visit this page](http://www.docker.com/whatisdocker).

## Virtual Machines

As the name suggests, a Virtual Machine (VM) emulates a physical computer. In
the last few years, VM's have become very popular because of their scalability,
ease of maintenance, and reproducibility. 

Vagrant is a software that defines and controls the virtual machine
environment. These machines are generally able to work together and can be
associated with each other. Some use-cases people are using multi-machine
environments for today:  

* Accurately modeling a multi-server production topology, such as separating a web and database server.  
* Modeling a distributed system and how they interact with each other.  
* Testing an interface, such as an API to a service component.  
* Disaster-case testing: machines dying, network partitions, slow networks, inconsistent world views, etc.  

Many software packages provide virtualization on modern computer architectures
such as VMWare, Virtual Box, Parallels etc.

## Package managers and distributions

Part of the problem in creating a computational environment is the procurement of
necessary libraries and other dependencies. Linux distributions have long been a source of
extensive scientific development resources. Package managers like [HomeBrew](http://brew.sh/)
and [Chocolatey](https://chocolatey.org/) are also available for OSX and Windows. Scientific
Python distributions are also available like [Anaconda](http://continuum.io/downloads),
[Canopy](https://www.enthought.com/products/canopy/) or [PythonX,Y](https://code.google.com/p/pythonxy/).

## Hands-On

1. [Create your own reproducible computational environment](../environment/).
2. Upload your Docker image to [DockerHub](https://hub.docker.com).
