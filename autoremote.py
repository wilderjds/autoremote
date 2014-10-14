import re 
import os
import urllib2
name='RaspiPi' # WHATEVER YOUR DEVICE NAME
ipreq=urllib2.Request("http://ipecho.net/plain")
ipres=urllib2.urlopen(ipreq)
ipdata = ipres.read()
publicip=ipdata
localip='YOUR_LOCAL_IP'
key='YOUR_AUTOREMOTE_KEY'

def autoremote_reg():
	req=urllib2.Request('http://autoremotejoaomgcd.appspot.com/registerpc?key={0}&name={1}&id=homepi&type=linux&publicip={2}&localip={3}'.format(key,name,publicip,localip))
	res=urllib2.urlopen(req)
	data=res.read()

def autoremote_send(message):
	req=urllib2.Request('https://autoremotejoaomgcd.appspot.com/sendmessage?key={0}&message={1}'.format(key,message))
	res=urllib2.urlopen(req)
	data=res.read()

#autoremote_reg()
