#!/bin/bash
if [ -d ~/git/${1} ]; then
  echo "Project already exist!!" > cr.log
  exit 1
fi
git init --bare ~/git/$1 > cr.log
cp deploy.sh ~/git/${1}/hooks/
chmod +x ~/git/${1}/hooks/deploy.sh
cp post-receive ~/git/${1}/hooks/
chmod +x ~/git/${1}/hooks/post-receive
echo ${2} > ~/git/${1}/hooks/url
cd ~/git/${1}/
git remote add origin $3
