import requests
import pytest
import allure

from api_tests.conftest import validator
from global_helpers.constants import REQUEST_LINK
from global_helpers.helpers import email_name_generator

@allure.feature("User Registration API")
@allure.story("Validate registration schema")
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
