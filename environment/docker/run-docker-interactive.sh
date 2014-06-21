docker build -t reproducible - < Dockerfile-interactive
docker run -t -i \
    -v `pwd`/../../notebooks:/home/repro/example \
    reproducible /bin/bash
