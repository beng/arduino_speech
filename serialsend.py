import serial
import time

s = serial.Serial('COM3',9600)

def input(sound):
	print 'COMING LIVE FROM SERIALSEND WITH COMMAND', sound

for i in range(0,5):
	s.write('Y')
	time.sleep(1)
	s.write('N')
	print s.readline()


