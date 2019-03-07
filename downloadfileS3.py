import boto3
import botocore

BUCKET_NAME = 'datagrokrassessment' # bucket name
KEY = 'task.txt' # File in bucket

s3 = boto3.resource('s3')

try:
    s3.Bucket('datagrokrassessment').download_file(KEY,'task.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

from string import punctuation
N = 10
words = {}
words_gen = (word.strip(punctuation).lower() for line in open("task.txt")
for word in line.split())
for word in words_gen:
    words[word] = words.get(word, 0) + 1
    top_words = sorted(words.iteritems(),
    key=lambda(word, count): (-count, word))[:N]
for word, frequency in top_words:
    print "%s: %d" % (word, frequency)

