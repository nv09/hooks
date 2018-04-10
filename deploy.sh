#!/bin/bash

#re=$(echo $PWD)
rep=$(echo $PWD | rev | cut -d '/' -f1 | rev )
mkdir /var/www/html/${rep} 2>&
TRAGET="/var/www/html/${rep}"
#if [ ! -d $TARGET ]; then
#  mkdir $TARGET
#fi
GIT_DIR=`git rev-parse --git-dir`
BRANCH="master"

while read oldrev newrev ref
do
	# only checking out the master (or whatever branch you would like to deploy)
	if [[ $ref = refs/heads/$BRANCH ]];
	then
		echo "Ref $ref received. Deploying ${BRANCH} branch to production..."
		git --work-tree=$TRAGET --git-dir=$GIT_DIR checkout -f
	else
		echo "Ref $ref received. Doing nothing: only the ${BRANCH} branch may be deployed on this server."
	fi
done
