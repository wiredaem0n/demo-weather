#!/usr/bin/env python

##### Openweathermap.org Accumulated Data Precipitation API url ################################################################################################################
#PAID   API url  http://history.openweathermap.org/data/2.5/history/accumulated_precipitation?id={city ID}&start={start}&end={end}													
#Sample API url http://samples.openweathermap.org/data/2.5/history/accumulated_precipitation?id=4887398&start=1505336400&end=1505941200&appid=b1b15e88fa797225412429c1c50c122a1"    
################################################################################################################################################################################### 

import urllib2
import time
import json
import sys
import datetime
from optparse import OptionParser

options = OptionParser(usage='%prog server [options]', description='Openweathermap API call Sample')
options.add_option('-k', '--apikey', type='str', help='API Key [Required]')
options.add_option('-n', '--days', type='int', default=5, help='Number of days (default:5)')
options.add_option('--cid', type='str', default="4887398", help='City ID to query (default:Chicago)')
opts, args = options.parse_args()


if not opts.apikey :
  sys.exit(options.print_help())


baseurl		= "http://history.openweathermap.org/data/2.5/history/accumulated_precipitation?"
sampleurl 	= "http://samples.openweathermap.org/data/2.5/history/accumulated_precipitation?"
api_key		= opts.apikey
city_id		= opts.cid
ndays		= opts.days
sdate 		= int(time.time()) # in unix time
edate 		= sdate - (86400 * ndays)	
fullurl		= sampleurl + "id=" + city_id + "&start=" + str(sdate) + "&end=" + str(edate) + "&appid=" + api_key

#API Call
print "Requesting the last " + str(ndays) + " days."

try:
	headers = {}
	headers['User-Agent'] = "ApiWeatherCaller-V1"
	request  = urllib2.Request(fullurl,headers=headers)

	response = urllib2.urlopen(request)
	content = response.read()
	if len(content):
		print "Success[%d] => %s" % (response.code,fullurl)
		#Json to python object
		decoded = json.loads(content)

		response.close() 

		print("***** Date ******     **** Precipitation(in) **** ")	
		for item in reversed(decoded['list']):
			print("   {}                     {} ".format(item['date'],item['rain']))

except urllib2.URLError as error:
	print "Failed reaching url[]=>:  %s" % (fullurl)

