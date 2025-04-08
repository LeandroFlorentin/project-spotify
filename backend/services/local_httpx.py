import httpx


async def http(url, method, body, params, headers, data):
    try:
        async with httpx.AsyncClient() as client:
            client_method = getattr(client, method.lower())
            response = await client_method(
                url, json=body, params=params, headers=headers, data=data
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as exc:
        print(f"HTTP Exception for {exc.request.url} - {exc}")
        raise
