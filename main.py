import sqlite3
import time
import datetime
import callRekog
import os
import ledMaster
import sys
import polly
import buttonFirst
import attendance


while True:
	ledMaster.RedOn()
	buttonFirst.buttonPress()
	time.sleep(0.5)
	os.system("fswebcam -r 1280x720 -F 5 --no-banner 2>/dev/null photo.jpg")
	print("photo done.")

	attendance.create_MLDS_table()

	imageName = "photo.jpg"
	try:
		face = callRekog.searchFacesbyImage(imageName) #Try and except block here if the API call fails. 
	except:
		os.system("""kill $(ps aux | grep 'buttonPress.py' | awk '{print $2}' | head -n1)""") #Kill the yellow light blinking. (We ran that as a background process in buttonFirst.buttonPress)
		ledMaster.YellowOff() #In case the process was killed when the yellow light was still on
		ledMaster.RedBlink() # Blink the light 4 times to indicate an error
		sys.exit() #Stop execution of the python script.

	ledMaster.YellowOff()#in case job was killed while the yellow LED was on.
	ledMaster.Green() #Green light goes on for 4 seconds to show success. 
	polly.greeting(face) #We run this before updating table to optomize user experience. (Users don't need to see the schedule)
	attendance.update_table(face) #update the schedule
	attendance.read_from_db() #Prints out the table. Good for troubleshooting. 
	attendance.close_db()