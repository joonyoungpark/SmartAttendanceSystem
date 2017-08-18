import boto3
from pygame import mixer
import os

AWS_ACCESS_KEY_ID = 'YOURKEY'
AWS_SECRET_ACCESS_KEY = 'YOURSECRETACCESSKEY'

client = boto3.client('polly', 
                      region_name='us-east-1', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def greeting(face):
	spoken_text = client.synthesize_speech(Text='Good to see you' + str(face) + ". I've noted you down.",
										   OutputFormat='mp3',
										   VoiceId='Joanna')

	# Save output speech as mp3 file
	with open('output.mp3', 'wb') as f:
		f.write(spoken_text['AudioStream'].read())
		f.close()

	#Play mp3 file from cmd 
	mixer.init()
	mixer.music.set_volume(1.0) #Set to max volume
	mixer.music.load('output.mp3')
	mixer.music.play()
	# Remove mp3 file after speech is finished
	while(mixer.music.get_busy() == True):
		pass

	mixer.quit()
	os.remove('output.mp3')

	#greeting(face)
