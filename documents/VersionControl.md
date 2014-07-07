### Clone a repo

```bash
$ git clone https://github.com/your-username/scipy-tutorial-2014.git
```

### Branches

To create a branch

```bash
$ git checkout -b my-working-branch
```

Remember that this creates a branch *from* whatever branch is currently checked out. It's typically best to branch from master only, unless there's a reason to branch from an existing branch.

### Creating a Commit

```bash
git add -u # stages all changed files, including deleted files
git commit -m "Briefly describe your changes" # Try for 50 characters or less
```

### See your changes

```bash
$ git log master..
$ git diff master...
```

### Pushing your Branch

```bash
$ git push origin my-working-branch
```

When you're ready, create a pull request on GitHub to merge your work.

### Seeing changes in master

If your pull request was not from a fork, the changes you made will be available on the master branch.

```bash
$ git pull origin master
$ git log master
$ git log master --first-parent
```

### Working with Forks

If your pull request was from a fork, you'll need to pull changes from the upstream repository to get your changes in master.

```bash
$ git remote -v # list remotes
$ git remote add upstream https://github.com/reproducible-research/scipy-tutorial-2014
$ git remote -v # should now see your new upstream remote
```

To update your fork from the upstream

```bash
$ git fetch upstream
$ git rebase upstream/master
```

Then, to get those changes back up into your fork on GitHub

```bash
$ git push origin master
```

### Resources

 * https://guides.github.com/introduction/flow/
 * https://github.com/jnunemaker/dotfiles/blob/master/bash/config
 * https://github.com/jnunemaker/dotfiles/blob/master/bash/git-completion
 * https://guides.github.com/activities/citable-code/
