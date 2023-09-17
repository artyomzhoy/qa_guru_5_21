import json
import os

from jsonschema.validators import validate
from tests.conftest import catfact_api, resources_path_catfact


def test_list_breeds_current_page():
    current_page = 2

    response = catfact_api(
        method='get',
        url='/breeds',
        params={'page': current_page}
    )

    assert response.status_code == 200
    assert response.json()['current_page'] == current_page


def test_list_breeds_current_page_schema():
    with open(os.path.join(resources_path_catfact, 'catfact_breeds_schema.json')) as file:
        schema = json.loads(file.read())

    response = catfact_api(
        method='get',
        url='/breeds'
    )
    validate(response.json(), schema)
