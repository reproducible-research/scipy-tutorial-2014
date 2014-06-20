docker build -t wtw/interactive - < Dockerfile-interactive
docker run -t -i \
    -v `pwd`/../../notebooks:/home/repro/example \
    wtw/interactive /bin/bash
