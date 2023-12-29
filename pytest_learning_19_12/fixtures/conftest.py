import pytest


#creating global variables in pytest which will be avialable for all tests
def pytest_configure():
    pytest.string1 = 'its beautiful day'
    pytest.list1 = ['Iam', 'Mohana kasi', 'python', 'language']

@pytest.fixture(scope="class")
def string_setup():
    print("executing 1st conftest")
    string_ = pytest.string1[::]
    string_.upper()
    yield string_

@pytest.fixture
def list_setup():
    list_ = pytest.list1.copy()
    yield list_[::-1]


def check_conf_normal_function():
    print("normal fucntion also executing in conftest")

