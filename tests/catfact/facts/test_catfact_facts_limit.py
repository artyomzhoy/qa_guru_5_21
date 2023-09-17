import json
import os

from jsonschema.validators import validate
from tests.conftest import catfact_api, resources_path_catfact


def test_catfact_facts_limit():
    limit = 5

    response = catfact_api(
        method='get',
        url='/facts',
        params={'limit': limit}
    )

    assert response.status_code == 200
    assert len(response.json()['data']) == limit


def test_catfact_facts_limit_schema():
    with open(os.path.join(resources_path_catfact, 'catfact_facts_schema.json')) as file:
        schema = json.loads(file.read())

    response = catfact_api(
        method='get',
        url='/facts'
    )
    print(response.json())
    validate(response.json(), schema)
