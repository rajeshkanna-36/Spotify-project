import boto3

from app.core.settings import AWS_ACCESS_KEY_ID,AWS_REGION,AWS_S3_BUCKET,AWS_SECRET_ACCESS_KEY

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def test_connnection():

    response = s3_client.head_bucket(
        Bucket = AWS_S3_BUCKET
    )

    print(response)

def upload_mp3(file,obj_key : str):

    s3_client.upload_fileobj(
        Fileobj=file,
        Bucket=AWS_S3_BUCKET,
        Key=obj_key,
        ExtraArgs={
            "ContentType":"audio/mpeg"
        }
    )

    return obj_key
    