from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException
import jwt
import uuid

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = {k: str(v) if isinstance(v, uuid.UUID) else v for k, v in data.items()}  # Convert UUIDs to strings
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# def decode_token(token: str):
#     try:
#         decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

#         # Convert 'id' from string back to UUID safely
#         if "id" in decoded_payload:
#             decoded_payload["id"] = str(decoded_payload["id"])  # ✅ Fix: Convert UUID to string

#         return decoded_payload

#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token has expired")
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=401, detail="Invalid token")

def decode_token(token: str):
    print("token: ", token)
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    print("decoded_payload: ", decoded_payload)
    return decoded_payload
