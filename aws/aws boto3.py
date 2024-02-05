import boto3

s3 = boto3.client('s3')

bucket_name = 'latokhindima'

region = 'eu-north-1'

s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})

