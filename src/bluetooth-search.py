#encoding=utf-8

__author__ = "Paulo Gil"
__email__ = "paulogil93@gmail.com"

import bluetooth
import os

def cls():
	os.system(['clear','cls'][os.name == 'nt'])

cls()

print "Searching for devices..."
nearby_devs = bluetooth.discover_devices()

if len(nearby_devs) == 0:
	print "No devices were found..."
elif len(nearby_devs) == 1:
	print "Found 1 device..."
else:
	print "Found %d devices..." % len(nearby_devs)

for addr in nearby_devs:
	name = bluetooth.lookup_name(addr)
	print "Name: %s | MAC: %s" % (name, addr)
