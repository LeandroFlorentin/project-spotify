from services import http
from fastapi import HTTPException
import os

env = dict(os.environ)


async def login(body):
    try:
        response = await http(
            url=env["URL_MICROSERVICE_AUTH"] + "auth/login",
            method="post",
            body=body,
            params=None,
            headers=None,
            data=None,
        )
        print("RESPONSEEEE", response)
        return response
    except HTTPException as err:
        print("ERRORSITO", err)
        raise err
    except KeyError as err:
        raise HTTPException(
            status_code=500, detail=f"Missing environment variable: {err}"
        )
