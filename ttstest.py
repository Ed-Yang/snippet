#!usr/bin/env python  
#encoding=utf-8  

"""
#-------------------------------------------------------------------------- 
File: ttstest.py

Description:
   The sample code for ITRI text to speech web service.  Beofre testing it, 
   it is needed to apply a service account
   
   	http://tts.itri.org.tw/member/registeration.php
	
	In shell, run the following script:
	
		$ python ttstest.py -a account -p password -t message
	   
	If success, the translated voice will be store in "message" with .wav file extension.
	   
Author: Edward Yang
#-------------------------------------------------------------------------- 
"""

import urllib2
from time import sleep
from SOAPpy import SOAPProxy

WSDLFile 	= "http://tts.itri.org.tw/TTSService/Soap_1_3.php?wsdl"
url 		= "http://tts.itri.org.tw/TTSService/Soap_1_3.php"
namespace 	= "http://tts.itri.org.tw/TTSService"

def textToSpeech(name, passwd, xlatText):		
	proxy     = WSDL.Proxy(WSDLFile)
	proxy.soapproxy.config.debug = 1

	# NOTE.  The following line is workaround for SOAPpy namespace issue
	proxy.methods['ConvertSimple'].namespace = proxy.wsdl.targetNamespace
	#print proxy.methods.keys()
	status = proxy.ConvertSimple(accountID=name, password=passwd, TTStext=xlatText)
	#print status
	return status

def textToSpeech2(name, passwd, xlatText):
	server = SOAPProxy(url, namespace)
	server.config.debug = 0
	reqStatus = server.ConvertSimple(name, passwd, xlatText)
	print "request status = ", reqStatus
	retResult = reqStatus.split('&')
	print "request result = " , retResult
		
	if int(retResult[0]) == 0 :
		# check convert progress
		cvtResult = ['0'] * 5
		#statusCode = '0'
		while int(cvtResult[2]) in {0, 1}: # wait completion
			cvtStatus = server.GetConvertStatus(name, passwd, int(retResult[2]))
			print "convert status = ", cvtStatus, "ID", retResult[2]
			# on success, status is return URL
			#resultCode, resultString, statusCode, status = cvtStatus.split('&')
			cvtResult = cvtStatus.split('&')			
			print cvtResult
			sleep(0.5)

		# save to file
		if (int(cvtResult[2]) == 2): # '2' means "completed"
			waveUrl = cvtResult[4]
			req = urllib2.Request(waveUrl)
			resp = urllib2.urlopen(req)
			wavFile = resp.read()
			outfile = open(xlatText + u".wav", 'wb')
			outfile.write(wavFile)		
	else:	
		return retResult[1]
	
class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):	
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "a:p:t:h", ["account", "password", "text", "help"])
		except getopt.error, msg:
			raise Usage(msg)
		
		# clean account information
		account = password = textMsg = u""
		for opt, arg in opts:
			if opt in ('-a', '--account'):
				account = arg
			elif opt in ('-p', '--password'):
				password = arg
			elif opt in ('-t', '--text'):			

				print "sys encoding = ", sys.getdefaultencoding()	
				print "arg type  -->", type(arg)
				
				# in windows (zh-TW), the default encoding of command shell is 'ascii'.
				# for chinese input, the encoding could be 'big5' or 'mbcs'
				textMsg = unicode(arg, sys.getfilesystemencoding())		
			elif opt in ('-h', '--help'):																		
				print >> sys.stderr, "python ttstest.py -a account -p password -t message"
				return 0
				
		if (textMsg != u""):			
			status = textToSpeech2(account, password, textMsg)
			print status
		else:
			raise Usage("message is not specified !")		
		
	except Usage, err:
		print >> sys.stderr, err.msg
 		print >> sys.stderr, "for help use --help"
  		return 2

if __name__ == "__main__":
	import sys
	import getopt
	
	#reload(sys)  
	#sys.setdefaultencoding('utf8')	
		
	sys.exit(main())

	print status	
	