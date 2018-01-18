#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import redis
import time

Coin='zcash'
redishost='127.0.0.1'
redisport=6379
try:
	r=redis.Redis(host=redishost,port=redisport,decode_responses=True)
except:
	print "error in connecting to redis"
#front.py coinaddress
workeraddress=sys.argv[1]
#get timestamp in second
now=int(time.time())
#check if address is in database
if r.exists(Coin+":"+workeraddress)==False:
	print 'address not avaliable'
else:
	#generate talbe head
	wdata='<table border="2"><caption>'+workeraddress+' </caption>'+"\n"
	wdata=wdata+'<tr><th>miner name</th><th>Hash rate</th><th>last subbmit </th></tr>'+"\n"
	#get all member with scores in zset workeraddress
	result=r.zrange(Coin+":"+workeraddress,0,-1,withscores=True)
	#count all miner in coin:address 
	count=r.zcard(Coin+":"+workeraddress)
	#suppose all miner is online
	livecount=count
	for k in result:
		#get lastsubmit timestamp from hash coin:workerlist by address.miner in millionsecond
		lastsubtime=r.hget(Coin+":workerlist",workeraddress+"."+k[0])
		#how long until last submit share in second
		difftime=now-int(lastsubtime)/1000
		#if more than very long time , delete it from zset and will not be counted in next time
		if difftime > 7200:
			r.zrem(Coin+":"+workeraddress,k[0])
		#if there is no submit more than 60 seconds , mark it in table
		elif difftime > 60:
			wdata=wdata+'<tr class="off"><td>'+k[0]+'</td><td>'+str(k[1])+' Sol/s </td><td>'+str(difftime)+'</td>'+"\n"
			livecount=livecount-1
		else:
			wdata=wdata+'<tr><td>'+k[0]+'</td><td>'+str(k[1])+' Sol/s </td><td>'+str(difftime)+'</td>'+"\n"
	wdata=wdata+"</table>\n"
	count=r.zcard(Coin+":"+workeraddress)
	wdata=wdata+'<p>total count: '+str(livecount)+'/'+str(count)+'</p>'+"\n"
	print wdata
	
