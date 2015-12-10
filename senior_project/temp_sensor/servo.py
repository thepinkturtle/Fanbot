# Servo Control
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(18,gpio.OUT)
pwm = gpio.PWM(18,50)
pwm.start(5)
pwm.ChangeDutyCycle(3)
time.sleep(.5)
pwm.ChangeDutyCycle(4)
time.sleep(.5)
pwm.ChangeDutyCycle(5)
time.sleep(.5)
pwm.ChangeDutyCycle(6)
time.sleep(.5)
pwm.ChangeDutyCycle(7)
time.sleep(.5)
pwm.ChangeDutyCycle(8)
time.sleep(.5)
pwm.ChangeDutyCycle(9)
time.sleep(.5)
pwm.ChangeDutyCycle(10)
time.sleep(.5)
pwm.ChangeDutyCycle(11)
time.sleep(.5)
pwm.ChangeDutyCycle(12)
gpio.cleanup()

