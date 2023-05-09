#!/bin/bash

# copies all log files from fox server to local machine

src="ecc462@10.100.240.203:~/logs/"
dst="/home/shrdlu/code/utsa-linux-server-usage-analysis/logs"

rsync -a "$src" "$dst" 
