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

s = serial.Serial('COM3',9600)

def input(sound):
    print 'COMING LIVE FROM SERIALSEND WITH COMMAND', sound
    s.write(sound)
    print s.readline()
    
    