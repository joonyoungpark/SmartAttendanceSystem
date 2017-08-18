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

![alt text](https://drive.google.com/drive/folders/0B9W7ptBZHWfca1N2NHBENy1uRkk "bread board")
![alt text](https://drive.google.com/drive/folders/0B9W7ptBZHWfca1N2NHBENy1uRkk "bread board")
For each light, there is a GPIO pin connected to the jack going directly to the LED. 
There is a resistor going between the LED and the other jack, which leads to a GND pin. 
Although it may not be entirely clear, here are some images of where the connectors are inserted into the rPi:













When on standby, only the red light is on. After the user presses the button, the yellow light starts blinking and a photo is taken. 
The yellow light keeps on blinking until the API call to AWS Rekognition is successful and the name of the user is returned.     




 


