import boto3

# Using Amazon s3
client = boto3.client('s3')

BUCKET_NAME = ''

S3_URL = ''


# Upload a file
def upload_file(file, key):
    client.upload_file(file, BUCKET_NAME, key)
    image_url = F'{S3_URL}/{BUCKET_NAME}/{key}'
    return image_url


# Upload a file obj
def upload_file_obj(file_obj, key):
    with open(file_obj, 'rb') as data:
        client.upload_fileobj(data, BUCKET_NAME, key)
        image_url = F'{S3_URL}/{BUCKET_NAME}/{key}'
        return image_url


# Download an S3 object to a file.
def download_s3_file(file_name, key):
    client.Object(BUCKET_NAME, key).download_file(file_name)
