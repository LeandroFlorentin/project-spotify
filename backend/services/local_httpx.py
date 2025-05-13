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
    print("Execute HTTP Request:", url, method, body, params, headers, data)
    try:
        async with httpx.AsyncClient() as client:
            if method.lower() not in ["get", "post", "put", "delete"]:
                raise ValueError(f"Método HTTP no soportado: {method}")

            client_method = getattr(client, method.lower())

            if method.lower() in ["post", "put"]:
                response = await client_method(
                    url, json=body, params=params, headers=headers, data=data
                )
            else:
                response = await client_method(url, params=params, headers=headers)
            print("ASD", response.status_code)
            if response.status_code >= 400:
                try:
                    error_data = response.json()
                    raise HTTPException(
                        status_code=response.status_code,
                        detail=error_data.get("message", "Error en el microservicio"),
                    )
                except Exception:
                    raise HTTPException(
                        status_code=response.status_code,
                        detail=response.text,
                    )

            return response.json()
    except httpx.HTTPError as exc:
        print(f"HTTP Exception for {exc.request.url} - {exc}")
        raise HTTPException(status_code=500, detail=str(exc))
