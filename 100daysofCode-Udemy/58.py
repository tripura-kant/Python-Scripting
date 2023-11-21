#!/usr/bin/python

import json
import sys
import urllib2
import base64

# Replace XXXXX with your actual values
user = 'admin'
password = '1178bf128bc88f1bc8650118f227d517d6'
jenkins_url = 'http://localhost:8080/'

def urlopen(url, data=None):
    '''Open a URL using the urllib2 opener.'''
    request = urllib2.Request(url, data)
    base64string = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    response = urllib2.urlopen(request)
    return response

if len(sys.argv) > 1:
    job_name = sys.argv[1]
else:
    sys.exit(1)

try:
    jenkins_stream = urlopen(jenkins_url + job_name + "/lastBuild/api/json")
except urllib2.HTTPError as e:
    print ("URL Error: " + str(e.code))
    print " (job name [" + job_name + "] probably wrong)"
    sys.exit(2)

try:
    build_status_json = json.load(jenkins_stream)
except ValueError:
    print ("Failed to parse json")
    sys.exit(3)

if "result" in build_status_json:
    print("[" + job_name + " #" + str(build_status_json["number"]) + "]: " + build_status_json["result"])
    if build_status_json["result"] != "SUCCESS":
        sys.exit(4)
else:
    sys.exit(5)

sys.exit(0)
