import pytest
import allure


@allure.title("#TC1 - Verify that 1+1 is equal to 2")
@allure.description("This is Smoke TestCase")
@pytest.mark.smoke
def test_addition():
    assert 1+1 == 2


@allure.title("#TC2 - Verify that 2-2 is equal to 0")
@allure.description("This is sanity TestCase")
@pytest.mark.sanity
def test_subtraction():
    print(2-2 == 2-2)



@allure.title("#TC3 - Verify the multiplication")
@allure.description("This is regression TestCase")
@pytest.mark.regression
def test_multiplication():
    print(8 * 5 == 8 * 5)

# To get the result in allure_result folder command is ******pytest folderpath --alluredir=allure_result*******

# To check allure report command is ******* allure serve allure_result*********


