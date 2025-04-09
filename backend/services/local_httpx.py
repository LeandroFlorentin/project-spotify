from typing import Literal
import httpx


async def http(
    url: str,
    method: Literal["get", "post", "put", "delete"],
    body: any,
    params: any,
    headers: any,
    data: any,
):
    try:
        async with httpx.AsyncClient() as client:
            client_method = getattr(client, method.lower())
            response = await client_method(
                url, json=body, params=params, headers=headers, data=data
            )
            print("RESPUESTA", response)
            return response.json()
    except httpx.HTTPError as exc:
        print(f"HTTP Exception for {exc.request.url} - {exc}")
        raise
