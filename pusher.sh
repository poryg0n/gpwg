#!/bin/bash

#git init
#git add -A
#git status
#git commit -m "Adding stuffs"
##git push main master
#git push -u master --all
#

#echo "# lareva" >> README.md
git init
git add . -A
git commit -m "first commit"
git branch -M main
git remote remove origin
git remote add origin https://github.com/poryg0n/gpwg.git
git push -fu origin main
