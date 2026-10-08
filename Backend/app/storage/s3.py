import boto3  

import boto3
from botocore.config import Config

from app.core.settings import (
    AWS_ACCESS_KEY_ID,
    AWS_REGION,
    AWS_S3_BUCKET,
    AWS_SECRET_ACCESS_KEY
)

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
    config=Config(
        signature_version="s3v4",
        s3={
            "addressing_style": "virtual"
        }
    )
)

def test_download(obj_key: str):
    response = s3_client.get_object(
        Bucket=AWS_S3_BUCKET,
        Key=obj_key
    )

    print("S3 GET SUCCESS")
    print(response["ContentType"])

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

def upload_cover_image(file, obj_key: str, content_type: str):

    s3_client.upload_fileobj(
        Fileobj=file,
        Bucket=AWS_S3_BUCKET,
        Key=obj_key,
        ExtraArgs={
            "ContentType": content_type
        }
    )

    return obj_key

def get_file_url(obj_key: str):
    return s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": AWS_S3_BUCKET,
            "Key": obj_key
        },
        ExpiresIn=3600
    )

def delete_objects(obj_key: str):
    s3_client.delete_object(
        Bucket=AWS_S3_BUCKET,
        Key=obj_key
    )
    