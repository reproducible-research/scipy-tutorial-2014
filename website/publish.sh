#!/bin/sh

# Build and publish the website to
#
# http://reproducible-research.github.io/scipy-tutorial-2014/
#
# Run from the top of the repository

docker run -v $PWD:/home/reproducible reproducible/dexy dexy setup
docker run -v $PWD:/home/reproducible reproducible/dexy dexy
test $? || exit 1

repo_dir=$PWD
cd /tmp
git clone $repo_dir 2> /dev/null
cd $(basename $repo_dir)
git checkout gh-pages
git rm -rf *
cp -r $repo_dir/output-site/* ./
rm ./README.md
git add *
git commit -m "Build on $(date) of $(cd $repo_dir; git rev-parse --short HEAD)."
git push git@github.com:reproducible-research/scipy-tutorial-2014.git gh-pages:gh-pages
