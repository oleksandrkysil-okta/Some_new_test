import requests
import pytest

from api_tests.conftest import validator
from global_helpers.helpers import email_name_generator

REQUEST_LINK = "http://users.bugred.ru/tasks"


@pytest.mark.NW_schema_test
def test_doregister_schema():
    """
    Test schema for doRegister API
    """
    email, name = email_name_generator()

    json_data = {
          "email": email,
          "name": name,
          "password": "1"
    }

    response = requests.post(REQUEST_LINK + "/rest/doregister", json=json_data)

    validator("doregister_schema", response)
