#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
logfile='/home/chengang/.zcash/debug.log'
notifycmd='/home/chengang/znomp/scripts/blocknotify 127.0.0.1:17117 zcash '
height=""
blockhash=""

f=open(logfile,'r')
f.seek(0,2)
#goto file end and star readline again and again to search UpdataTips
while True:
	line=f.read()
	while line:
		if "UpdateTip" in line:
			result=line.split(" ")
                        blockhash=result[4][5:]
                        height=result[6][7:]
			print "update new block, height=", height," new prehash=",blockhash
                        print "blocknotify to pool"
                        notifycmd=notifycmd+blockhash
			os.popen(notifycmd)
		else:
			print "no update in line, current height:", height	
		line=f.read()
	time.sleep(3)

