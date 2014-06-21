Docker Computational Environment Creation
=========================================

Installing Docker
-----------------

You must already have [docker](http://docker.io) installed. See http://docker.io for more information.

Running Notebooks
-----------------

To install and run IPython notebooks in a docker container, run the
`run-docker-interactive.sh` script from within this directory.

At the end of the build process, you should see output like this:

```
Successfully built 7b7bc4cbc144
repro@c4601f2ecc0b:~$
```

You are now in a Docker container.

If you want to run the IPython notebook server from within this container, cd
to the `example` directory and run the `run-ipython.sh` script:

```
repro@c4601f2ecc0b:~/example$ ls
README.md  ReproducibleResearch.ipynb  run-ipython.sh
repro@c4601f2ecc0b:~/example$ bash run-ipython.sh
```

Using `ifconfig` in the container, determine the IP address, and, using your
normal web browser, navigate to that address plus `:8888` to view the notebook.

Or you can determine the container's IP address via `docker inspect c4601`
where c4601 is the start of the container ID, which is visible at the command
prompt (after `repro@`)

Running Dexy
------------

The `run-dexy-in-docker.sh` script creates a Docker container which has all
necessary software to run `dexy` on the `dexy/` directory and generate
reproducible research from the sources there.
