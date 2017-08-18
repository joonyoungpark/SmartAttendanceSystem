import pprint
from boto.s3.connection import S3Connection
import boto3

#A nice little tool to do different Rekognition Collection utilities from me to you.

SIMILARITY_THRESHOLD = 85.0
AWS_ACCESS_KEY_ID = 'YOURKEY'
AWS_SECRET_ACCESS_KEY = 'YOURSECRETACCESSKEY'

conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
client = boto3.client('rekognition', 
                      region_name='us-east-1', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

#################Stuff to make and break a collection############################
def createCollection():
	response = client.create_collection(
	    CollectionId='TargetImages'
	)

def deleteCollection():
	response = client.delete_collection(
	     CollectionId='TargetImages'
	)
	pprint.pprint(response)

##################Add an indexed face to the collection############################

def indexFace():
	response = client.index_faces(
	    CollectionId='TargetImages',
	    Image={
	        'S3Object': {
	            'Bucket': 'rekognitionfaces',
	            'Name': 'Bobby.JPG'
	        }
	    },
	    ExternalImageId='Bobby',
	    DetectionAttributes=[
	        'DEFAULT','ALL'
	    ]
	)
	pprint.pprint(response)

indexFace()

def deleteFace():
	response = client.delete_faces(
    CollectionId='TargetImages',
    FaceIds=[
        '41199fbf-42f4-5c34-d51f-2291r7ie3eon'
    ]
)
#deleteFace()

def listCollection():
	response = client.list_faces(
	    CollectionId='TargetImages',
	    MaxResults=123
	)
	pprint.pprint(response)

listCollection()
