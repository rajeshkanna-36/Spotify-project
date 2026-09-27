import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not set")

if not AWS_ACCESS_KEY_ID:
    raise ValueError("AWS_ACCESS_KEY_ID is not set")

if not AWS_SECRET_ACCESS_KEY:
    raise ValueError("AWS_SECRET_ACCESS_KEY is not set")

if not AWS_REGION:
    raise ValueError("AWS_REGION is not set")

if not AWS_S3_BUCKET:
    raise ValueError("AWS_S3_BUCKET is not set")
