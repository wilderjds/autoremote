import re 
import os
import requests
import argparse
#import subprocess

class autoremote:
	def __init__(self, url=None):

		self.key_url=requests.get(url,allow_redirects=True)
		if self.key_url.status_code==200:
			url=self.key_url.url
			self.key=re.search(r'key\=(.*)',url,re.DOTALL)
			self.key=self.key.group(1)
		else:
			raise Exception("Can not connect to Autoremote!!!")
		print("Fetching global ip")
		self.publicip = requests.get("http://ipecho.net/plain")
		if self.publicip.status_code==200:
			self.publicip=self.publicip.text
			print('Global IP:',self.publicip)
		print("Fetching local ip")
		self.localip=os.popen("ifconfig|grep inet|head -1|sed 's/\:/ /'|awk '{print $3}'").read()
		print('local IP:',self.localip)
	
	def register(self, name=None):
		print ("device name:",name)
		self.reg_url="http://autoremotejoaomgcd.appspot.com/registerpc?key={0}&name={1}&id=3&type=linux&publicip={2}&localip={3}".format(self.key,name,self.publicip,self.localip)
		self.reg_req=requests.get(self.reg_url)
		if self.reg_req.status_code==200:
			print("Registered successfully")
			
	def send(self,msg):
		self.msg=msg
		self.send_url="http://autoremotejoaomgcd.appspot.com/sendmessage?key={0}&message={1}".format(self.key,self.msg)
		self.send_req=requests.get(self.send_url)
		if self.send_req.status_code==200:
			print("{0} sent successfully".format(self.msg))
		else:
			raise Exception("Autoremote failed to send message!!!")

if __name__ == "__main__":

	# Define and parse command line arguments
	#example:  -n "S5"  -u "http://goo.gl/T8nIJr" -m "notify Test=:=This is a Autoremote test!"
	parser = argparse.ArgumentParser(description="Autoremote")
	parser.add_argument("-n", "--name", help="Autoremote name")
	parser.add_argument("-u", "--url", help="Autoremote url")
	parser.add_argument("-m", "--msg", help="Autoremote message")

	# Handle command Line arguments
	args = parser.parse_args()

	print (args)

	if args.name:
		_name = args.name
	else:
		_name=""

	if args.url:
		_url = args.url
	else:
		_url="[YOUR AUTOREMOTE URL]"

	if args.msg:
		_msg = args.msg
	else:
		#_msg= "say 5=:=This is a Autoremote test!"
		_msg="notify Test=:=This is a Autoremote test!"

	ar=autoremote(url=_url)   # Connect to autoremote server
	if _name:
		ar.register(name=_name)   # Register device
	if _msg:
		ar.send(_msg)			  # Send Message

