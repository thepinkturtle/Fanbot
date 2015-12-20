#!/usr/bin/python
import time
import thread
import Adafruit_TMP.TMP006 as TMP006
import sys

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
		return c * 9.0 / 5.0 + 32.0


# Default constructor will use the default I2C address (0x40) and pick a default I2C bus.
sensor = TMP006.TMP006()


# Initialize communication with the sensor, using the default 16 samples per conversion.
# This is the best accuracy but a little slower at reacting to changes.
sensor.begin()

# Optionally initialize with a faster but less precise sample rate.  You can use
# any value from TMP006_CFG_1SAMPLE, TMP006_CFG_2SAMPLE, TMP006_CFG_4SAMPLE, 
# TMP006_CFG_8SAMPLE, or TMP006_CFG_16SAMPLE for the sample rate.
#sensor.begin(samplerate=TMP006.CFG_1SAMPLE)
def hello_world():
	while True:
		print "I'm threading the needle!"
		time.sleep(1)
		

try:
	thread.start_new_thread(hello_world, ())

except:
	print"I couldn't start the thread, man!"


# Loop printing measurements every second.
print 'Press Ctrl-C to quit.'
while True:
	obj_temp = sensor.readObjTempC()
	die_temp = sensor.readDieTempC()
	print 'Object temperature: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp))
	print '   Die temperature: {0:0.3F}*C / {1:0.3F}*F'.format(die_temp, c_to_f(die_temp))
	time.sleep(1.0)

