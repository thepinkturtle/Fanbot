
################################_Imports_################################
## Servo imports
import RPi.GPIO as gpio
import time

## Temperature sensor import
import Adafruit_TMP.TMP006 as TMP006

################################_Setup_################################
## Servo setup
gpio.setmode(gpio.BOARD) # Map the gpio pins to the breadboard
gpio.setup(18, gpio.OUT) # Tell Pi we'll use pin 18 to talk to servo
servo = gpio.PWM(18, 50) # Setup to control servo with 50 hz frequency on pin 18

## Temperature sensor constructor
tempSensor = TMP006.TMP006()

## Setting the sample rate for tempSensor
## Set the sample rate to 3 if its to inaccurate or slow change it with
## 8SAMPLE or some number
tempSensor.begin(samplerate = TMP006.CFG_3SAMPLE)

################################_Functions_################################

## Convert to Fahrenheit
def celsius_to_farh(c)
	return c * 9.0 / 5.0 +32.0

## Loopleft for servo

## LoopRight for servo

## Track a face

## Look for a face