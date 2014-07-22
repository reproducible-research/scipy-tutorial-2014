# Dockerfile for the 2014 SciPy Conference tutorial
#
#  Reproducible Research: Walking the Walk
#
# Make sure to use a persistent Docker image tag
FROM       phusion/baseimage:0.9.10
MAINTAINER Ana Nelson <ana@ananelson.com>

# Set the locale to UTF-8
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || true

# Use squid deb proxy (if available on host OS)
# as per https://gist.github.com/dergachev/8441335
ENV HOST_IP_FILE /tmp/host-ip.txt
RUN /sbin/ip route | awk '/default/ { print "http://"$3":8000" }' > $HOST_IP_FILE
RUN HOST_IP=`cat $HOST_IP_FILE` && curl -s $HOST_IP | grep squid && echo "found squid" && echo "Acquire::http::Proxy \"$HOST_IP\";" > /etc/apt/apt.conf.d/30proxy || echo "no squid"

### "update"
RUN apt-get update

### "utils"
RUN apt-get install -y build-essential
RUN apt-get install -y adduser
RUN apt-get install -y curl
RUN apt-get install -y sudo

### "nice-things"
RUN apt-get install -y ack-grep
RUN apt-get install -y strace
RUN apt-get install -y vim

### "git"
RUN apt-get install -y git

### "python"
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip

### "scipy"
RUN apt-get install -y python-numpy
RUN apt-get install -y python-scipy
RUN apt-get install -y python-matplotlib
RUN apt-get install -y ipython
RUN apt-get install -y ipython-notebook
RUN apt-get install -y python-nose

### "dexy"
RUN pip install dexy

### "latex"
RUN apt-get install -y pandoc
RUN apt-get install -y --no-install-recommends texlive-latex-base
RUN apt-get install -y --no-install-recommends texlive-latex-extra

### "itk"
RUN easy_install SimpleITK

### "mplayer"
RUN apt-get install -y mplayer

### "create-user"
RUN useradd -m -p $(perl -e'print crypt("foobarbaz", "aa")') repro
RUN adduser repro sudo
RUN chown -R repro.repro /home/repro

### "activate-user"
ENV HOME /home/repro
USER repro
WORKDIR /home/repro
