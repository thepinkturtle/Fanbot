# Servo Control
import RPi.GPIO as gpio
import time
import Adafruit_TMP.TMP006 as TMP006

#def a fx for celcius to fahrenheit.
def c_to_f(c):
	return c * 9.0 / 5.0 + 32.0

#default constuctor
sensor = TMP006.TMP006()

#default sample rate for temp sensor
sensor.begin(samplerate = TMP006.CFG_8SAMPLE)

#if it measures temp to slow you can change it like this:
#sensor.begin(samplerate = TMP006.CFG_1SAMPLE)


#set up for servo
gpio.setmode(gpio.BOARD)
gpio.setup(18,gpio.OUT)
pwm = gpio.PWM(18,50)
pwm.start(5)

#loop rotate the servo/fan and take temp
while True:
	pwm.ChangeDutyCycle(3)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(4)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(5)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(6)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(7)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(8)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(9)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(10)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(11)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

	pwm.ChangeDutyCycle(12)
	obj_temp = sensor.readObjTempC()
	print 'Temp: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)) 
	time.sleep(1)

#clean up after loop
gpio.cleanup()

