from fastapi import Request, HTTPException, status
from utils.jwt import decoded_token


async def decode_token_dependency(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Bearer no encontrado",
        )

    token = auth_header.replace("Bearer ", "")
    decoded = decoded_token(token)

    return decoded["data"]
