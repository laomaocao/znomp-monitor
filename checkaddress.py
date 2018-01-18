#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import os

cmd='zcash-cli validateaddress '+sys.argv[1]
result=json.load(os.popen(cmd))
if result['isvalid']:
	print "OK"
else:
	print "NO"

