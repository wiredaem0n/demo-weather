#!/usr/bin/env python
import urllib2
import time
import json

#####Openweathermap.org Accumulated DATA Precipitation API URLS ################################################################################################################
#PAID   API url  http://history.openweathermap.org/data/2.5/history/accumulated_precipitation?id={city ID}&start={start}&end={end}													
#Sample API url http://samples.openweathermap.org/data/2.5/history/accumulated_precipitation?id=4887398&start=1505336400&end=1505941200&appid=b1b15e88fa797225412429c1c50c122a1"    
################################################################################################################################################################################### 
baseurl		= "http://history.openweathermap.org/data/2.5/history/accumulated_precipitation?id=4887398&appid=6d08d471221ed4f8b902fda13c58d276&"
sampleurl 	= "http://samples.openweathermap.org/data/2.5/history/accumulated_precipitation?id=4887398&appid=6d08d471221ed4f8b902fda13c58d276&"
api_key		= "6d08d471221ed4f8b902fda13c58d276"
city_id		= "4887398" 
sdate 		= int(time.time())
edate 		= sdate - (86400 * 5)	


#API Request
fullurl = sampleurl + "&start=" + str(sdate) + "&end=" + str(edate)


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

