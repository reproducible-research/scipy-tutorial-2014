docker build -t wtw/repro .
docker run  \
    -v `pwd`/../../dexy:/home/repro/example \
    wtw/repro
