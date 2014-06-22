FROM       phusion/baseimage:35c2d5a269ff
MAINTAINER Ana Nelson <ana@ananelson.com>

RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :
ENV DEBIAN_FRONTEND noninteractive

# Use squid deb proxy as per https://gist.github.com/dergachev/8441335
# Uncomment this line if squid-deb-proxy configured on host.
RUN /sbin/ip route | awk '/default/ { print "Acquire::http::Proxy \"http://"$3":8000\";" }' > /etc/apt/apt.conf.d/30proxy

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
RUN apt-get install -y python-matplotlib

### "dexy"
RUN pip install dexy

### "itk"
RUN easy_install SimpleITK

### "mplayer"
RUN apt-get install -y mplayer

### "normal user"
RUN useradd -m reproducible
RUN adduser reproducible sudo

RUN chown -R reproducible /home/reproducible

### "activate-user"
ENV HOME /home/reproducible
USER reproducible
