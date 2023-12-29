import pytest

def pytest_configure():
    pytest.dict_ = {'name': "mohana kasi", 'age':27}


@pytest.fixture(scope="module")
def dict_fetch():
    print("in conftest module_fixture1")
    yield pytest.dict_
    print("closing of module ficture")

@pytest.fixture(scope="function")
def second_fixture():
    print("second fixture executed")

@pytest.fixture()
def request_fixture_dheck(request):
    print(dir(request))
    print(dir(request.__module__))

@pytest.fixture()
def request_fixture_practice(request):
    print(f"\n scope of this fixture is {request.scope}")
    print(f"\n name of this function is {request.function.__name__}")
    print(f"\n {request.module.__name__}") #gives the packages names which fixture is in



@pytest.fixture(params=["kasi", 'Mohana']) #here fixture will run for total length of params list
def params_check(request):
    print("parameters are not using")

@pytest.fixture(params=["kasi", 'Mohana', 1008]) #here fixture will run for total length of params list
def params_check_list_2(request):
    if request.param == 'kasi' and isinstance(request.param, str):
        print("kasi found")
    else:
        pass

@pytest.fixture(params={'name': 'kasi', 'age':27})
def prams_with_dict(request): #eachtime key will pass to request parameter
    print(request.param)


@pytest.fixture(params="this is kasi from python")
def prams_with_string(request): #eachtime key will pass to request parameter
    print(request.param)

@pytest.fixture()
def factories_fixture():
    def data_type_check(name):
        if name == 'string':
            return "sample string"
        elif name == 'list':
            return [1,2,3,4]
        else:
            print("not a proper data type")
    return data_type_check


@pytest.fixture(params=[(3,4), [5,6]], ids=['tuple', 'list'])
def fixture_parametrization(request):
    return request.param

@pytest.fixture(params=["access", "slice"])
def fixture_params02(request):
    return request.param

