#!/usr/bin/python
import cv2
import sys
import Adafruit_TMP.TMP006 as TMP006
import time
import RPi.GPIO as gpio
import thread
import spidev


#servo setup
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
servo = gpio.PWM(11,50)
servo.start(7.5)
servo.ChangeDutyCycle(0)

#temp sensor setup
tempSensor = TMP006.TMP006()
tempSensor.begin(samplerate=TMP006.CFG_8SAMPLE)

#spi setup
spi = spidev.SpiDev()
spi.open(0,0)

#arrays and such
currentPos = 7.5
CFace = 0
moved_right = False
moved_left = True
minPos = 3
maxPos = 11.5
rangeRight = 253
rangeLeft = 138
startTime = 0
fClap = False
sClap = False

#previow ranges 135,255
#webcam face detection
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 320)
video_capture.set(4, 240)

#functions

def getAdc (channel):

	global startTime
	global fClap

	#check for valid channel
	if ( channel > 7 or channel < 0 ):
		return -1
	
	#preform SPI transaction and store returned bits in 'r'
	r = spi.xfer( [1, (8 + channel) << 4, 0] )
	
	#Filter data bits from returned bits
	adcOut = ( (r[1] & 3) << 8 ) + r[2]
	percent = int( round(adcOut / 10.24) )
	
	if ( adcOut > 1022 and not fClap ):		
		startTime = time.clock()
		fClap = True
		print "first clap"
		time.sleep(.1)
		adcOut = 0
		startTime = time.time()
		return

	if ( adcOut > 1022 and fClap and (time.time() - startTime) < 2 ):
		print "second clap"
		fClap = False
		time.sleep(.1)	
		adcOut = 0
		servo.ChangeDutyCycle(3)
	
def clap_detect():
	
	global fClap
	global startTime
	#constantly process the sound level in the room
	while True:	
		getAdc(0)
		time.sleep(.000001)
		if (fClap):		
			while ( (time.time() - startTime) < 2 ):
				getAdc(0)
				time.sleep(.000001)

			print"time's up! at: {0} seconds".format(time.time() - startTime)
			fClap = False

def scan():
	global currentPos
	global moved_right
	global moved_left
	if not moved_right: 
		servo_right()
		if currentPos >= maxPos:
			moved_right = True
			moved_left = False
	if not moved_left:
		servo_left()
		if currentPos <= minPos:
			moved_right = False
			moved_left = True 
	
def servo_left():
	global currentPos
	if currentPos > minPos:
		currentPos = currentPos - .40
		servo.ChangeDutyCycle(currentPos)
	time.sleep(.02)
	servo.ChangeDutyCycle(0)


def servo_right():
	global currentPos
	if currentPos < maxPos:
		currentPos = currentPos + .40
		servo.ChangeDutyCycle(currentPos)
	time.sleep(.02)
	servo.ChangeDutyCycle(0)

def track_face(new_cValue):

	#turn left
	if new_cValue > rangeRight:
		servo_left()
	
	#turn right
	if new_cValue < rangeLeft:
		servo_right()
	time.sleep(.01)
	servo.ChangeDutyCycle(0)

try: 
	thread.start_new_thread(clap_detect, ())
except:
	print"Sorry, but the Dude could not start your thread"


while True:
	
#	time.sleep(.01)	
	#capture frame by frame

	ret, frame = video_capture.read()
#	grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	face = faceCascade.detectMultiScale(
		frame,
		scaleFactor = 1.3,
		minNeighbors = 1,
		minSize = (40,40),
		flags = (cv2.CASCADE_DO_CANNY_PRUNING + cv2.CASCADE_FIND_BIGGEST_OBJECT + cv2.CASCADE_DO_ROUGH_SEARCH + cv2.CASCADE_SCALE_IMAGE))
	#cv2.CASCADE_SCALE_IMAGE
	# draw the rectangle around a face
	for (x, y, w, h) in face:
		cv2.rectangle(frame, (x, y), (x+w,y+h), (0,0,255))
		CFace = (w/2+x)
	# display the resulting frame
	cv2.imshow('Video', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	temp = tempSensor.readObjTempC()		
	#if we found a face send the position to the servo
	if CFace != 0 and temp > 16 and temp < 28:
		track_face(CFace)
#		print "temperature: {0}".format(temp)
#		if temp > 19 and temp < 23:

	else:
		scan()
		#set the value back to zero for the next pass
	CFace = 0 	
		
				

# clean up
gpio.cleanup()
video_capture.release()
cv2.destroyAllWindows()

	
