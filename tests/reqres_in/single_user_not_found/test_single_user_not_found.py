import json
import os

from jsonschema.validators import validate
from tests.conftest import resources_path_reqres_in, reqres_api


def test_single_user_not_found():
    user_id = 'random_value'

    response = reqres_api(
        method='get',
        url=f'/api/users/{user_id}')

    assert response.status_code == 404


def test_single_user_not_found_schema():
    user_id = 'random_value'

    with open(os.path.join(resources_path_reqres_in, 'single_user_not_found_schema.json')) as file:
        schema = json.loads(file.read())

    response = reqres_api(
        method='get',
        url=f'/api/users/{user_id}')
    validate(response.json(), schema)
