import os
import boto3

os.environ['AWS_DEFAULT_PROFILE'] = 'admin'
os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'

s3_client = boto3.client('s3')