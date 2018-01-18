#!/usr/bin/python
# -*- coding: utf-8 -*-
import BaseHTTPServer
import urllib
import os

HOST='192.168.21.15'
PORT=8091
class ServerHTTP(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		query=self.path
		print query
		self.send_response(200)
		self.send_header("Content-Type","text/html;charset=UTF-8")
		self.end_headers()
		if len(query) < 35:
			data='invalid query. (http://HOST:PORT/mineraddress)'
		else:
			if os.popen('./checkaddress.py {address}'.format(address=query[1:])).read()!="OK\n":
				data='invalid address'	
			else:
				body=os.popen('./front.py {address}'.format(address=query[1:])).read()
				data=str(headstr+body+tailstr)
		self.wfile.write(data)

	def do_POST(self):
		path=self.path
		print path
		self.send_response(200,"ok")
		self.send_header('Content-type', 'text/html')
		self.end_headers()
try:
	httpserver=BaseHTTPServer.HTTPServer((HOST,PORT),ServerHTTP)
	fop=open("head","r")
	headstr=fop.read()
	fop.close()
	fop=open("tail","r")
	tailstr=fop.read()
	fop.close()	
	httpserver.serve_forever()
except  KeyboardInterrupt:
	 print 'Shutting down the server by keyboarad'
	 httpserver.shutdown()


