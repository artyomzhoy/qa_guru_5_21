import os
import allure
from requests import sessions
from curlify import to_curl
from utils import attach

resources_path_reqres_in = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/reqres_in'))
resources_path_catfact = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/catfact'))


def base_url(resourse, method, url, **kwargs):
    new_url = resourse + url
    method = method.upper()
    with allure.step(f'{method} {url}'):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, **kwargs)
            message = to_curl(response.request)
            attach.add_curl(message)
            if response.content:
                attach.add_response_json(response)
            else:
                attach.add_empty_response(response)
    return response


def reqres_api(method, url, **kwargs):
    response = base_url(
        resourse='https://reqres.in',
        method=method,
        url=url,
        **kwargs
    )
    return response


def catfact_api(method, url, **kwargs):
    response = base_url(
        resourse='https://catfact.ninja',
        method=method,
        url=url,
        **kwargs
    )
    return response
