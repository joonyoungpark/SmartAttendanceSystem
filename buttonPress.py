import ledMaster

ledMaster.YellowOn() #Entire purpose of this file is to help run the function as a background process.
#Since we want the yellow LED to blink on and off while we are calling rekognition, treating it 
#as a background process and killing it is the way to go. 