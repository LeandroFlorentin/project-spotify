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
        return response
    except HTTPException as err:
        raise err
    except KeyError as err:
        raise HTTPException(
            status_code=500, detail=f"Missing environment variable: {err}"
        )
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
