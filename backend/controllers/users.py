from services import http
import os

env = dict(os.environ)

url_microservice_auth = env["URL_MICROSERVICE_AUTH"]


async def create_user(body, bearer_token):
    user = await http(
        url=url_microservice_auth + "users/create",
        method="post",
        body=body,
        params=None,
        headers={"Authorization": bearer_token},
        data=None,
    )
    return user


async def get_user(id, bearer_token):
    user = await http(
        url=url_microservice_auth + "users/me",
        method="get",
        params={"id": id},
        headers={"Authorization": bearer_token},
    )
    return user
