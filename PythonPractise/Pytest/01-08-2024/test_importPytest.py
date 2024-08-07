import pytest


@pytest.mark.smoke
def test_addition():
    assert 1+1 == 2


@pytest.mark.sanity
def test_subtraction():
    print(2-2 == 2-2)


@pytest.mark.regression
def test_multiplication():
    print(8 * 5 == 8 * 5)
