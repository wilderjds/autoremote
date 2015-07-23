This Derivative: Dan Yeakley at https://github.com/ddyeakley/Autoremote-python
Original autoremote.py author:  sriramsv/Autoremote-python at https://github.com/sriramsv/Autoremote-python
Credits: Joao dias (developer of the autoremote plugin for tasker)

Here is a small autoremote python wrapper module that can be used on a Raspberry PI.  Copy the module on any into /usr/lib/python/2.x/ import the module into your python code.

General API usage:

	ar=autoremote("your autoremote url")   	# Connect to autoremote server
	ar.register("your device name")   		# Register device
	ar.send("message to send")			  	# Send Message

Command line usage:
	
	usage: autoremote.py [-h] [-n NAME] [-u URL] [-m MSG]

	optional arguments:
	  -h, --help            show this help message and exit
	  -n NAME, --name NAME  Autoremote name
	  -u URL, --url URL     Autoremote url
	  -m MSG, --msg MSG     Autoremote message