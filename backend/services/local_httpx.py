from typing import Literal, Optional
from fastapi import HTTPException
import httpx


async def http(
    url: str,
    method: Literal["get", "post", "put", "delete"],
    body: Optional[dict] = None,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
):
    try:
        async with httpx.AsyncClient() as client:
            method__not_exist = method.lower() not in ["get", "post", "put", "delete"]
            if method__not_exist:
                raise ValueError(f"Método HTTP no soportado: {method}")
            client_method = getattr(client, method.lower())
            response = None

            if method.lower() in ["post", "put"]:
                print("UEREELE", url)
                response = await client_method(
                    url, json=body, params=params, headers=headers, data=data
                )
            else:
                response = await client_method(url, params=params, headers=headers)
            if response.status_code >= 400:
                raise HTTPException(
                    status_code=response.status_code, detail=response.text
                )
            return response.json()
    except httpx.HTTPError as exc:
        print(f"HTTP Exception for {exc.request.url} - {exc}")
        raise HTTPException(500, exc)
