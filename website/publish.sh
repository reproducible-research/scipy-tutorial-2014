#!/bin/sh

# Build and publish the website to
#
# http://reproducible-research.github.io/scipy-tutorial-2014/
#
# Run from the top of the repository

running_in_docker() {
  awk -F/ '$2 == "docker"' /proc/self/cgroup | read
}

generate_website() {
  echo
  echo "Generating website..."
  if test running_in_docker; then
	  dexy setup
	  dexy || exit 1
  else
	  docker run --rm -v $PWD:/home/reproducible reproducible/dexy dexy setup
	  docker run --rm -v $PWD:/home/reproducible reproducible/dexy dexy
	  test $? || exit 1
  fi
  echo "Generating website... [ok]"
}

push_website(){
  echo
  echo "Pushing website..."
  repo_dir=$PWD
  cd /tmp
  repo=$(basename $repo_dir)
  git clone $repo_dir $repo 2>/dev/null
  cd $repo
  git remote set-url origin $(cd $repo_dir; git config remote.origin.url)
  git pull
  git checkout gh-pages 2>/dev/null || git checkout -b gh-pages origin/gh-pages
  git rm -rf *
  cp -r $repo_dir/output-site/* ./
  rm ./README.md
  git add *
  git commit -m "Build on $(date) of $(cd $repo_dir; git rev-parse --short HEAD)."
  git push origin gh-pages:gh-pages
  echo "Pushing website... [ok]"
}

generate_website
push_website
