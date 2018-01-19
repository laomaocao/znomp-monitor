#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
logfile='/home/chengang/.zcash/debug.log'
notifycmd='/home/chengang/znomp/scripts/blocknotify 127.0.0.1:17117 zcash '
height=0
blockhash=""

f=open(logfile,'r')
f.seek(0,2)
#goto file end and star readline again and again to search UpdataTips
while True:
	line=f.read()
	while line:
		if "UpdateTip" in line:
			result=line.split(" ")
                        newhash=result[4][5:]
                        newheight=int(result[6][7:])
			print "update new block, height=", newheight," new prehash=",newhash
                        height=newheight
                        print "blocknotify to pool"
                        notifycmd=notifycmd+newhash
			os.popen(notifycmd)
		else:
			print "no update in line, current height:", newheight	
		line=f.read()
	time.sleep(3)

