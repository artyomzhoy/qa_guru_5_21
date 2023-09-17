import json
import os

from jsonschema.validators import validate
from tests.conftest import catfact_api, resources_path_catfact


def test_fact_max_length():
    max_length = 50

    response = catfact_api(
        method='get',
        url='/fact',
        params={'max_length': max_length}
    )

    assert response.status_code == 200
    assert response.json()['length'] <= max_length


def test_fact_max_length_schema():
    with open(os.path.join(resources_path_catfact, 'catfact_fact_schema.json')) as file:
        schema = json.loads(file.read())

    response = catfact_api(
        method='get',
        url='/fact'
    )
    validate(response.json(), schema)

