from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config.settings import JWT_ACCESS_TOKEN_EXPIRE_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM

def create_access_token(user_id : int):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub" : str(user_id),
        "exp" : expire
    }

    token = jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )

    return token, expire

    