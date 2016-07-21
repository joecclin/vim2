#!/bin/bash

# for one user name in one git
# git config user.name "joecclin"

# for git config to push all branches
git config --global push.default matching
# for git config to push this working branches
#git config --global push.default simple

# add ignore rule file
git config --global core.excludesfile ~/.gitignore_global

# set vimdiff to git diff 
git config --global diff.tool vimdiff
git config --global difftool.prompt false
git config --global alias.df difftool

# git alias ci to commit
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.st status

# add symbolic link
cd ..
ln -s ./.vimrc ../.vimrc
ln -s ./.vimproject_mappings ../.vimproject_mappings
ln -s ./.gitignore_global ../.gitignore_global

