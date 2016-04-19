#------------------------------------------------------------------- 
# WSDL Example
#------------------------------------------------------------------- 
from SOAPpy import WSDL
from SOAPpy import SOAPProxy

WSDLFile 	= "http://webservices.daehosting.com/services/TemperatureConversions.wso?WSDL"
namespace 	= "http://webservices.daehosting.com/temperature"
url 		= "http://webservices.daehosting.com/services/TemperatureConversions.wso"

def cToF_WSDL(x):
	proxy     = WSDL.Proxy(WSDLFile)
	#proxy.soapproxy.config.debug = 1

	# NOTE.  The following line is workaround for SOAPpy namespace issue
	proxy.methods['CelciusToFahrenheit'].namespace = proxy.wsdl.targetNamespace
	return proxy.CelciusToFahrenheit(nCelcius=x)


#------------------------------------------------------------------- 
# SOAP Proxy Example
#-------------------------------------------------------------------

def cToF_Proxy(x):
	server = SOAPProxy(url, namespace)
	#server.config.debug = 1
	return server.CelciusToFahrenheit(nCelcius=x)

def cbWSDL():
	v = int(edtCelcius.get())
	s = cToF_WSDL(v)
	updateFahrenheit(s)
	print "cToF_WSDL = %s" % s

def cbProxy():
	v = int(edtCelcius.get())
	s = cToF_Proxy(v)
	updateFahrenheit(s)
	print "cToF_Proxy = %s" % s	

def updateFahrenheit(s):
	varFahrenheit.set("Fahrenheit = %12s" % s)

if __name__ == '__main__':

	from Tkinter import *

	top = Tk()
	
	labelCelcius = Label(top, text="Celcius 	= ")
	labelCelcius.pack(side = LEFT)

	varFahrenheit = StringVar()
	updateFahrenheit("")
	labelFahrenheit = Label(top, textvariable=varFahrenheit)
	labelFahrenheit.pack(side = RIGHT)

	edtCelcius = Entry(top, bd =5)
	edtCelcius.pack(side = LEFT)

	buttonWSDL = Button(top, text="WSDL", command = cbWSDL)
	buttonWSDL.pack(side = RIGHT)

	buttonProxy = Button(top, text="Proxy", command = cbProxy)
	buttonProxy.pack(side = RIGHT)

	top.mainloop()



