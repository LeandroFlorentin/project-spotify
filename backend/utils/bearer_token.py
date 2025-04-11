from fastapi import Depends
from fastapi.security import APIKeyHeader


def get_bearer_token():
    return Depends(APIKeyHeader(name="Token"))
