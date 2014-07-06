# Computational Environment

TODO: Why reproducible computational enviroment is important.  What the
characteristics of a reproducible computational environment are.

## Docker

Docker is an open-source engine that automates the deployment of any
application as a lightweight, portable, self-sufficient container that will
run virtually anywhere.

![Container vs VMs](http://tiewei.github.io/images/docker_vm.jpg)

![Docker stack](http://tiewei.github.io/images/docker-filesystems-multilayer.png)

TODO: Docker description

## VM's
As the name suggests, the VM (Virtual Machine) emulates a physical machine as such computers. In the last few years, VM has become very popular because of their scalability, ease of maintenance, and reproducibility. 

Vagrant is a software to define and control virtual machine environemnt. These machines are generally able to work   together or are somehow associated with each other. Here are some use-cases people are using multi-machine environments for today:  

- Accurately modeling a multi-server production topology, such as separating a web and database server.  
- Modeling a distributed system and how they interact with each other.  
- Testing an interface, such as an API to a service component.  
Disaster-case testing: machines dying, network partitions, slow networks, inconsistent world views, etc.  

## Package managers and distributions

TODO: package manager and distribution description

## Exercise

1. [Create your own reproducible computational environment](../environment/).
2. Upload your Docker image to [DockerHub](https://hub.docker.com).
