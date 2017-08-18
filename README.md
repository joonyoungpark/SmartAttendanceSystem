# Smart Attendance System (SAS)
**SAS** takes attendance using **facial recognition**, intended to replace paper-based traditional attendance sheets. 
This can be seen as a practical usage of Amazon Web Services such as rekognition, S3, and Polly.

## Getting Started
### Requirements
#### Hardware
* 1 raspberry pi (we used rPi 3 model B)
* 1 microUSB to USB power cord for rPi
* 1 USB webcam
* 3 LED lights (one red, one yellow, one green)
* 1 small breadboard (see image)
* 8 male-female connectors
* 1 button
* 1 mobile phone battery

#### Installation
You must run the below commands on the raspberry Pi:

```
sudo apt-get install boto
sudo apt-get install boto3
sudo apt-get install fswebcam
sudo apt-get install python-pygame
```

Also consider turning up the volume on your raspberry pi. There is a nice tool to do this called alsamixer.

### Electronic Configuration
Have the female sides of the connectors connected to the raspberry pi. 
For each LED and for the button, there must be one connector connected to a GND (ground) pin, and one connected to a GPIO (general purpose input/output) pin. 
The code here uses BCM numbering, so the LEDs and button are numbered by GPIO port. For example, and LED connected to GPIO17 would be numbered as 17.
![alt text](https://github.com/joonyoungpark/SmartAttendanceSystem/blob/master/images/rbpconfiguration.PNG "rbpblueprint")

The configuration of the breadboard is shown below:
![alt text](https://github.com/joonyoungpark/SmartAttendanceSystem/blob/master/images/breadboard.PNG "breadboard")

For each light, there is a GPIO pin connected to the jack going directly to the LED. 
There is a resistor going between the LED and the other jack, which leads to a GND pin. 
Although it may not be entirely clear, here are some images of where the connectors are inserted into the rPi:
![alt text](https://github.com/joonyoungpark/SmartAttendanceSystem/blob/master/images/pi.PNG "raspberrypi3")

#### LED implications
When on standby, only the red light is on. After the user presses the button, the yellow light starts blinking and a photo is taken. 
The yellow light keeps on blinking until the API call to AWS Rekognition is successful and the name of the user is returned. 

## Notes
You need Git bash or an equivalent to do the below commands. 

Copy all files in laptop folder to pi folder:
scp -P 2222 * pi@10.20.11.235:foldername

Connect to rPi: 
ssh pi@10.20.11.235 -p 2222

The Pi that was configured for this project is listening for SSH on port 2222 for security purposes. 
Remove the -p 2222 on the commands if you are using a fresh raspberry pi. 
Change the ip address with the ip address of your pi. 

Note that this system is viable. The current runtime can be more than halved if:
1. The USB webcam is swapped for an official camera module
2. AWS Polly is replaced for a local text to speech program or an LCD display. 
3. A stable wifi connection is obtained or the system is hooked up to ethernet cable

---

## Further Improvements
There are several ways that you can improve this project.
* Get the official raspberry pi camera module. Most webcams are not reliable and require you to stay still for some time to take a photo.
* Instead of calling AWS polly, consider using a built-in text to speech library. This can dramatically improve the runtime.
* Get a bluetooth speaker or a micro speaker which can be embedded inside the case. As an alternative, replace that entirely with an LCD display.
* Implement automatic photo-taking when face detected instead of having the user manually pressing the photo-taking button. This can be done with openCV. 
* Replace the mobile phone charging battery for a long rPi power cord that plugs into a wall socket.
* Connect the pi’s attendance sheet to your computer via network shared folder so that it automatically synchronizes.
* Ensure that you have a reliable internet connection or connect the system to LAN.
* Write a script or find some method to quickly and conveniently upload new faces and names to the AWS Rekognition Collection. 

## Authors
Joon Park
Andrew Luo