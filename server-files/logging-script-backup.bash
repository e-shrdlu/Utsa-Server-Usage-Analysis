#!/bin/bash

filename="/home/ecc462/logs/foxlog_`date +'%F'`.txt"

touch $filename

for x in {1..4}
do
	echo server$x @ `date +'%F %T'` | tee -a $filename
	echo '{' | tee -a $filename
	ssh -i "/home/ecc462/.ssh/id_rsa" "ecc462@10.100.240.20$x" "who -u" | tee -a $filename
	echo '}' | tee -a $filename
done

