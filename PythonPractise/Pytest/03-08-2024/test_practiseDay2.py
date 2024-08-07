import pytest
import allure


@allure.title("Calculations")
@allure.description("Verifying the all possible calculations")
@pytest.mark.MathCalculation
def test_MathCalculation():
    assert 998/8 == 998/7

    pubmatic