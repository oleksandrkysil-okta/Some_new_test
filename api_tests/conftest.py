import os
import json
from jsonschema import validate

from global_helpers.constants import SCHEMA_PATH


def validator(schema_name, response):
    """
    The overloaded method for response json schema validation.
    First verify response status code is 200.
    Then verify response scheme matches to expected.
    """
    assert response.status_code == 200, f"Next reposnse was't successful, reponse status_code {response.status_code}"

    with open(os.path.abspath(os.curdir) + SCHEMA_PATH + schema_name + ".json", "r") as read_file:
        schema_read = json.load(read_file)

    validate(response.json(), schema_read)