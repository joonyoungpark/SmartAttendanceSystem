import RPi.GPIO as GPIO
import time
import ledMaster
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonPress():
	while True:
		input_state = GPIO.input(20)
		if input_state ==False:
			ledMaster.RedOff()
			os.system("python buttonPress.py &") #Run the yellow light blinking as a background process so I can keep it running but continue with my script
			break
		time.sleep(0.1)

