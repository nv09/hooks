#!/bin/bash
if [ ! -d ~/git/${1} ]; then
  echo "Project not exist!!" > push.log
  exit 1
fi
cd ~/git/${1}
git push origin master -v > ~/hooks/push.log 2>&1
