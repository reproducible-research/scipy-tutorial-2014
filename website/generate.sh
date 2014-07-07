#!/bin/sh

# Build the website
#
# Run from the top of the repository

running_in_docker() {
  awk -F/ '$2 == "docker"' /proc/self/cgroup | read
}

clear_website() {
  echo
  echo "Removing ./output-site ..."
  [ -d ./output-site ] && rm -r ./output-site
  echo "Removing ./output-site ... [ok]"
}

generate_website() {
  echo
  echo "Generating website..."
  if test running_in_docker; then
	  dexy setup
	  dexy || exit 1
  else
	  docker run --rm -v $PWD:/home/repro reproducible/dexy dexy setup
	  docker run --rm -v $PWD:/home/repro reproducible/dexy dexy
	  test $? || exit 1
  fi
  echo "Generating website... [ok]"
}

clear_website
generate_website
