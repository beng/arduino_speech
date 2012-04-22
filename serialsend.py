import serial
import time

'''
@file:		serialsend.py
@author: 	Ben Gelb

This file:
	-reads in data from the web app
	-reads in data from the micro-controller
	-writes data to the micro-controller
'''

port = 'COM3'
s = serial.Serial(port,9600)

def input(sound):
	print 'COMING LIVE FROM SERIALSEND WITH COMMAND', sound

def write_test(x):
	for i in range(x):
		s.write('Y')
		time.sleep(1)
		s.write('N')
		print s.readline()