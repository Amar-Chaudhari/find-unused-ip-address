#!/usr/bin/python
import sys
import socket
def ipRange(start_ip, end_ip):
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   temp = start
   ip_range = []
   
   ip_range.append(start_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))    
      
   return ip_range
   
   

# Actual Usage

if len(sys.argv) != 3:
	print "\nIncorrect Arguments"
	print "Usage - script.py 192.168.1.0 192.169.1.200"
else:
	ip_range = ipRange(sys.argv[1],sys.argv[2])

	unused_ip_range = []
	used_ip_range = []

	for ip in ip_range:
		try:
			used_ip_range.append(socket.gethostbyaddr(ip)[0])
		except socket.error:
			unused_ip_range.append(ip)
			pass

	print "\n----  Used IPs  ----\n"

	for ip in used_ip_range:
		try:
			print socket.gethostbyname(ip) + " " + ip
		except socket.error:
			pass

	print "\n---  Unused IPs  ---\n"
	ip_count = 1

	for ip in unused_ip_range:
		print ip_count,ip
	        ip_count +=1		


	print '\n\n'
