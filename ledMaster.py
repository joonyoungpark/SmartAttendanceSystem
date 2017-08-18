import time
import RPi.GPIO as GPIO ## Import GPIO library

def Green():
	GPIO.setmode(GPIO.BCM) 
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17,True) 
	time.sleep(4)
	GPIO.output(17,False)

def YellowOn():
	GPIO.setmode(GPIO.BCM) 
	GPIO.setup(4, GPIO.OUT) ## Setup GPIO 4 to OUT

	while True:
		GPIO.output(4,True) ## Turn on GPIO 4
		time.sleep(0.5)
		GPIO.output(4,False)
		time.sleep(0.5)

def YellowOff():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT)
	GPIO.output(4,False)

def RedOff():
	GPIO.setmode(GPIO.BCM)
	LED = 21
	GPIO.setup(LED, GPIO.OUT)
	GPIO.output(LED,False)

def RedOn():
	GPIO.setmode(GPIO.BCM)
	LED = 21
	GPIO.setup(LED, GPIO.OUT)
	GPIO.output(LED,True)

def RedBlink():
	GPIO.setmode(GPIO.BCM)
	LED = 21
	GPIO.setup(LED, GPIO.OUT)

	for x in range(0, 4):
		GPIO.output(LED,True)
		time.sleep(0.5)
		GPIO.output(LED,False)
		time.sleep(0.5)
