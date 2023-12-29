from pytest import fixture

@fixture
def temp_return_data():
    print("before")
    yield
    print("after")
