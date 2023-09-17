import json
import os

from jsonschema.validators import validate
from tests.conftest import resources_path_reqres_in, reqres_api


def test_single_user_id():
    user_id = 1

    response = reqres_api(
        method='get',
        url=f'/api/users/{user_id}')

    assert response.status_code == 200
    assert response.json()['data']['id'] == user_id


def test_single_user_schema():
    user_id = 1

    with open(os.path.join(resources_path_reqres_in, 'single_user_schema.json')) as file:
        schema = json.loads(file.read())

    response = reqres_api(
        method='get',
        url=f'/api/users/{user_id}')
    validate(response.json(), schema)
