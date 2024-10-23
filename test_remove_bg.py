from firefly import FireflyServices
import os

import boto3
from botocore.config import Config

ff_client_id = os.environ.get('CLIENT_ID')
ff_client_secret = os.environ.get('CLIENT_SECRET')

ff = FireflyServices(ff_client_id, ff_client_secret)

s3_bucket = "pythonffssdk"
s3_client = boto3.client('s3')

# Credit: https://github.com/AdobeDocs/cis-photoshop-api-docs/blob/main/sample-code/storage-app/aws-s3/example.py
def get_presigned_url(bucket, key, operation, expires_in):
    s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
    url = s3.generate_presigned_url(operation, Params={'Bucket': bucket, 'Key': key}, ExpiresIn=expires_in)
    return url 


imageInput = get_presigned_url(s3_bucket, 'source_cat.jpg', 'get_object', 3600)
imageOutput = get_presigned_url(s3_bucket, 'source_cat_nobg.jpg', 'put_object', 3600)
print("Generated read and write URLs for Photoshop")

print("Kicking off Remove BG job")
result = ff.removeBackground(imageInput, imageOutput)
print(result)