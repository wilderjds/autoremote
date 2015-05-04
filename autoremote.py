import re 
import os
import requests
import subprocess

class autoremote:
	def __init__(self):
		#self.name=raw_input("Enter the name of the device:")
		#self.url=raw_input("Enter the Autoremote URL:")
		self.name="Home-Linux"
		self.url="http://goo.gl/pZw1BO"
		self.key_url=requests.get(self.url,allow_redirects=True)
		if self.key_url.status_code==200:
			self.url=self.key_url.url
			self.key=re.search(r'key\=(.*)',self.url,re.DOTALL)
			self.key=self.key.group(1)
		else:
			raise 		
		print "device name:",self.name
		print "fetching global ip"
		self.publicip = requests.get("http://ipecho.net/plain")
		if self.publicip.status_code==200:
			self.publicip=self.publicip.text
			print 'global IP:',self.publicip
		print "fetching local ip"
		self.localip=os.popen("ifconfig|grep inet|head -1|sed 's/\:/ /'|awk '{print $3}'").read()
		print 'local IP:',self.localip
	
	def register(self):
		self.reg_url="http://autoremotejoaomgcd.appspot.com/registerpc?key={0}&name={1}&id=3&type=linux&publicip={2}&localip={3}".format(self.key,self.name,self.publicip,self.localip)
		self.reg_req=requests.get(self.reg_url)
		if self.reg_req.status_code==200:
			print "Registered successfully"
	def send(self,message):
		self.message=message
		self.send_url="http://autoremotejoaomgcd.appspot.com/sendmessage?key={0}&message={1}".format(self.key,self.message)
		self.send_req=requests.get(self.send_url)
		if self.send_req.status_code==200:
			print "{0} sent successfully".format(self.message)
		else:
			raise


if __name__ == "__main__":
	pc=autoremote()
	pc.register()
	#pc.send("hello Jarvis")
	
	
	
