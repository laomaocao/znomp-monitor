#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2
import json
import time
import redis

znomphost='192.168.21.15'
znompport='8080'
Coin='zcash'
Internal=30
redishost='127.0.0.1'
redisport=6379

def getstatfromnomp():
	url="http://"+znomphost+":"+znompport+"/api/stats"
        try:
		req=urllib2.Request(url)
        	resp=urllib2.urlopen(req).read()
        	response=json.loads(resp)
	except:
		print "error in getstatfromnomp"
	else:
        	return response


def connectredis():
	try:
		r=redis.Redis(host=redishost,port=redisport,decode_responses=True)
	except:
		print "error in connecting to redis"
	else:
		return r

if len(sys.argv)!=1:
	print sys.argv[0]+" HostIP Port Coinname Internalsesonds"
	znomphost=sys.argv[1]
	print "HostIP:"+znomphost
	znompport=sys.argv[2]
	print "Port:"+znompport
	Coin=sys.argv[3]
	print "Coinname:"+Coin
	Internal=int(sys.argv[4])
	print "Internal seconds"+sys.argv[4]
	

redisconn=connectredis()
while True:
	s=getstatfromnomp()
	for k in s['pools'][Coin]['workers']:
		workername=s['pools'][Coin]['workers'][k]['name']
		workerhash=s['pools'][Coin]['workers'][k]['hashrateString']
		workeraddress=workername.split(".")[0]
		minername=workername.split(".")[1]
		workerhash=workerhash.split(" ")[0]
		redisconn.zadd(Coin+":"+workeraddress,minername,float(workerhash))
	time.sleep(Internal)

