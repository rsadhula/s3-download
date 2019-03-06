import boto3
import botocore

BUCKET_NAME = 'rajashekar-smartshift' # replace with your bucket name
KEY = 'raju.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket('rajashekar-smartshift').download_file(KEY,'raju1.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

data = open('raju1.txt').read()
count = data.count('Devops')

print count
