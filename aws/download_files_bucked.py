import boto3

s3 = boto3.client('s3')
#s3.download_file('latokhindima', 'images.jpeg', 'local-images.jpeg')
s3.download_file('latokhindima', 'file_for_bucket_s3.txt', 'local-ile_for_bucket_s3.txt')
