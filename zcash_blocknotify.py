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
try:
	while True:
		line=f.readline()
		while line:
			findstr=line.find("UpdateTip")
			if findstr == 20:
				print "found Updatetips at:",findstr
				print "line lengh: " , len(line)
				result=line.split(" ")
                        	blockhash=result[4][5:]
                        	height=result[6][7:]
				blocktime=result[1]
				print "At:",blocktime," update new block, height=", height," new hash=",blockhash
                        	notifycmdtemp=notifycmd+blockhash
				print "excute notify : ",notifycmdtemp
				os.popen(notifycmdtemp)
			else:
				print line
				print "no update in line, current height:", height	
			line=f.readline()
		time.sleep(3)
except  KeyboardInterrupt:
        print 'Shutting down by keyboarad'
	f.close() 


