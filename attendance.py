import sqlite3
import time
import datetime

names = ['Joon', 'Andrew', 'Kevin', 'Bala', 'Yuhao', 'Kenneth'] #In here, you must add the externalID (rekognition collection) of those that will use the system.

conn = sqlite3.connect('attendance/attendance.db')
c = conn.cursor()

def create_MLDS_table():
	c.execute('CREATE TABLE IF NOT EXISTS MLDS_attendance_sheet(date_stamp TEXT, name TEXT, presence TEXT, time_stamp TEXT)') 

def update_table(face):
	if(face in names):
		# Set time stamp to current time
		unix = int(time.time())
		date_stamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
		time_stamp = str(datetime.datetime.fromtimestamp(unix).strftime('%H:%M:%S'))

		# Set recognized face to name
		name = face

		# Determine tardiness
		class_begins = '09:00:00'
		if(time_stamp > class_begins):
			presence = 'late'
		else:
			presence = 'on time'

		c.execute("INSERT INTO MLDS_attendance_sheet (date_stamp, name, presence, time_stamp) VALUES (?, ?, ?, ?)",
			 	 (date_stamp, name, presence, time_stamp))
		conn.commit() 		 

# Read from database 
def read_from_db():
	c.execute("SELECT date_stamp, name, presence, time_stamp FROM MLDS_attendance_sheet")
	for row in c.fetchall():
		print(row) 

def close_db(): 
	c.close() 
	conn.close()

