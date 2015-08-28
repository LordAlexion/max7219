#!/usr/bin/env python

import max7219.led as led
import time
import os
from max7219.font import proportional, CP437_FONT

device = led.matrix(cascaded=1)
device.orientation(180)

# ERROR

def error():
	device.show_message('Loading...', font=proportional(CP437_FONT))
	time.sleep(1)


# ! > 10

def excAlert():
	device.brightness(8)
	device.letter(0, ord('!'))
	for _ in range(5):
		device.invert(1)
		time.sleep(0.5)
		sevice.invert(0)
		time.sleep(0.5)


# 0 < NUM < 10

def numAlert(name, value):
	device.brightness(1)
	device.show_message(name, font=proportional(CP437_FONT))
	time.sleep(0.5)
	if value == 0:
		device.letter(0, 3)
	else:
		device.letter(0, ord(str(value)))
	for x in range(5):
		for i in range(1, 8):
			device.brightness(i)
			time.sleep(0.05)
		for j in range(1, 8):
			device.brightness(8 - j)
			time.sleep(0.05)
		time.sleep(0.5)
	for y in range(8):
		device.scroll_down()
		time.sleep(0.05)


# BOTH HEALTHY

def bothhealthy():
	device.brightness(0)
	device.letter(0, 3)
	for _ in range(3):
		for i in range(6):
			device.brightness(i)
			time.sleep(0.06)
		for j in range(6):
			device.brightness(5 - j)
			time.sleep(0.06)
		time.wait(1)
		



x = 0

while True:

	hst = int(open('/tmp/downhosts.tmp').read())
	sst = int(open('/tmp/criticalservices.tmp').read())
	
	if x == 0: 
		x = 1
	else:
		x = 0

	if hst == None or sst == None:
		error()
	elif hst > 9 or sst > 9:
		excAlert()
	elif hst == 0 & sst == 0:
		bothhealthy()
	elif x == 1:
		numAlert('Hosts', hst)
	else:
		numAlert('Services', sst)
