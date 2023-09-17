import json
import os

from jsonschema.validators import validate
from tests.conftest import resources_path_reqres_in, reqres_api


#  аргумент -s к команде pytest при выполнении теста для отображения принтов
def test_list_users_per_page():
    per_page = 5

    response = reqres_api(
        method='get',
        url='/api/users',
        params={'per_page': per_page}
    )

    assert response.status_code == 200
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page


def test_list_users_schema():
    with open(os.path.join(resources_path_reqres_in, 'list_users_schema.json')) as file:
        schema = json.loads(file.read())

    response = reqres_api(
        method='get',
        url='/api/users'
    )
    validate(response.json(), schema)
