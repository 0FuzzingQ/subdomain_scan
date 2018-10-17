
import urllib
import urllib2
import urlparse
import os
import sys
import argparse
import time
import thread
import socket

print "[*]For use info:python subdomain.py -h,--help"

parser = argparse.ArgumentParser(description='Scan Mission Params Needed')

parser.add_argument('-t', help = "domain you want to scan" , dest = "host")
parser.add_argument('-l', help = "log path you want to save" , required = False, dest = "logpath")
parser.add_argument('-f', help = "doamin from file path" , required = False , dest = "filepath")

args = parser.parse_args()

host = args.host
log = args.logpath
file = args.filepath

default_dict_path = "dict.txt"
content = open(default_dict_path).readlines()
for i in range(0,len(content)):
	content[i] = content[i].strip('\n')
#print content
thread_section = len(content) / 4
thread1_content = content[:thread_section]
thread2_content = content[thread_section:2*thread_section]
thread3_content = content[thread_section*2:thread_section*3]
thread4_content = content[thread_section*3:]



def scan( threadName, target, diction):
	for i in range(0,len(diction)):
		sing_dict = {}
		domain = str(diction[i]) + "." + target
		url = "http://" + domain
		
		try:
			ip = socket.gethostbyname(domain)
			sing_dict["ip"] = ip
		except:
			pass

		try:
			res = urllib2.urlopen(url,timeout = 2)
			sing_dict["net"] = "http/https"
			if res.headers["server"]:
				sing_dict["server"] = res.headers["server"]
		except:
			pass
		
		if "ip" in sing_dict.keys():
			print url,sing_dict
	exit() 


   	

 
try:
   thread.start_new_thread( scan, ("scan-1", host, thread1_content  ) )
   thread.start_new_thread( scan, ("scan-2", host, thread2_content  ) )
   thread.start_new_thread( scan, ("scan-3", host, thread3_content  ) )
   thread.start_new_thread( scan, ("scan-4", host, thread4_content  ) )
except:
   print "Error: unable to start thread"
 
while 1:
   pass



