import json
import os

from jsonschema.validators import validate
from tests.conftest import resources_path_reqres_in, reqres_api


def test_create_user():
    name = 'morpheus'
    job = 'leader'

    response = reqres_api(
        method='post',
        url='/api/users/',
        data={'name': name, 'job': job})

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_create_user_schema():
    name = 'morpheus'
    job = 'leader'

    with open(os.path.join(resources_path_reqres_in, 'create_user_schema.json')) as file:
        schema = json.loads(file.read())

    response = reqres_api(method='post',
                          url='/api/users',
                          data={'name': name, 'job': job}
                          )
    validate(response.json(), schema)
