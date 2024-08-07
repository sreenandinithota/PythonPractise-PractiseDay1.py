import pytest
import allure
import requests


# @allure.title("TC1_Get Request -> GET RESTFUL BOOKER ID")
# @allure.description("Verify the Get requests with ID")
# @allure.tag('P0', 'Regression')
# @allure.label('owner', 'Sree Nandini')
# @allure.testcase("TestCase1")
# @pytest.mark.Sanity
# def test_Get_single_request_id():
#     url = "https://restful-booker.herokuapp.com/booking/1"
#     responseData = requests.get(url)
#     print(responseData.json())
#     assert responseData.status_code == 200

@allure.title("TC1_Get Request -> GET RESTFUL BOOKER ID")
@allure.description("Verify the RESTFUL BOOKER with ID")
@allure.tag("P0", "Regression")
@allure.label("owner", "Sree Nandini")
@allure.testcase("TC1")
@pytest.mark.Smoke



def test_Get_Single_Request_Id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responsedata = requests.get(url)
    print(responsedata.json())
    assert responsedata.status_code == 200

















