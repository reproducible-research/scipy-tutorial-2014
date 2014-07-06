#!/bin/sh

# Build and publish the website to
#
# http://reproducible-research.github.io/scipy-tutorial-2014/
#
# Run from the top of the repository

my_dir="$(dirname "$0")"

"$my_dir/generate.sh"

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

push_website
