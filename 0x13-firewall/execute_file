#!/usr/bin/env bash
## Execute a file sript to your server.

###	Parameters (4)
###	1. The path to the file to be execute
###	2. The IP of the server we want to transfer the file to
###	3. The username scp connects with

if [ "$#" -lt 3 ]
then
	echo "Usage: 0-execute_file PATH_TO_FILE IP USERNAME "
elif [ "$#" -eq 3 ]
then
	ssh "$3@$2" 'bash -s' < "$1"
fi
