#!usr/bin/env python
#encoding=utf-8

"""
#--------------------------------------------------------------------------
File: props.py

Description: test how to utilize @property object

Author: Edward Yang
#--------------------------------------------------------------------------
"""

class Location(object):    
    #_latitude = 111
    #print self
    #print "new a location class ----> {}".format(_latitude)
    def __init__(self, lat=0, lng=0):
        print self
        #print " init a location class ----> {}".format(self._latitude)
        self._latitude = lat
        #_latitude = lat
        self._longitude = lng
        #print " after init a location class ----> {}:{}".format(_latitude, self._latitude)

    @property
    def latitude(self):
        print "geter _latitude"
        return self._latitude 

    @latitude.setter
    def latitude(self, lat):
        print " set a location class ----> {}".format(self._latitude)
        self._latitude = lat

# p1, p2 bound to different object
p1 = Location(10, 10)
p2 = Location(20, 20)
print "p1 = {}, p2 = {} p1.latitude = {}, p2.latitude = {}".format(p1, p2, p1.latitude, p2.latitude)

p1.latitude = 100
print "p1 = {}, p2 = {} p1.latitude = {}, p2.latitude = {}".format(p1, p2, p1.latitude, p2.latitude)

# p2 bound to the the same object as p1
p2 = p1
print "p1 = {}, p2 = {} p1.latitude = {}, p2.latitude = {}".format(p1, p2, p1.latitude, p2.latitude)

p2.latitude = 200
print "p1 = {}, p2 = {} p1.latitude = {}, p2.latitude = {}".format(p1, p2, p1.latitude, p2.latitude)

