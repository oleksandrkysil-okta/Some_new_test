import requests

from api_tests.conftest import validator

REQUEST_LINK = "http://users.bugred.ru/tasks"


def test_doregister_schema():

    # TODO create new user name and email generator and use it here
    json_data = {
          "email": "some_testgon_teadasdab@yopmail.com",
          "name": " ique_usedasdasda23",
          "password": "1"
    }

    response = requests.post(REQUEST_LINK + "/rest/doregister", json=json_data)

    validator("doregister_schema", response)