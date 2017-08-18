import pprint
from boto.s3.connection import S3Connection
import boto3
import os

SIMILARITY_THRESHOLD = 85.0 #Faces must have this percentage similarity to be considered a match. 
AWS_ACCESS_KEY_ID = 'YOURKEY'
AWS_SECRET_ACCESS_KEY = 'YOURSECRETKEY' #All this syntax is from boto3 docs. Copy and paste. 

conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
client = boto3.client('rekognition', 
                      region_name='us-east-1', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

#imageName = str(input())

def searchFacesbyImage(imageName): #For this to work you need an AWS rekognition collection. You can make one via AWS's CLI, and I've also included a python script. 
	
	with open(imageName, 'rb') as target_image:
		target_bytes = target_image.read()

	response = client.search_faces_by_image(
		CollectionId='TargetImages',
		Image={
			'Bytes': target_bytes
		},
		MaxFaces=123,
		FaceMatchThreshold=70
	)
	os.system("""kill $(ps aux | grep 'buttonPress.py' | awk '{print $2}' | head -n1)""") #Immediately kill yellow light blinking upon successful API call. 
	output = response['FaceMatches'][0]['Face']['ExternalImageId']
	return output

#searchFacesbyImage("photo.jpg")
