import pytest

# @pytest.mark.usefixtures("dict_fetch")
# def test_check_module_fixture(dict_fetch):
#     print(dict_fetch['name'])
#     print("temp check")
#
#
# @pytest.mark.usefixtures("second_fixture")
# def test_check_module_fixture2(second_fixture, request_fixture_dheck):
#     print("temp check 2nd fixture")


@pytest.mark.request_practice
def test_check_request(request_fixture_practice):
    print("fixture ")

@pytest.mark.practice_params
def test_prameters_check(params_check_list_2):
    print("these are the prameters")

@pytest.mark.fixture_with_dict_param
def test_dict_ficture(prams_with_dict):
    print("dict also possible as parameter in fictures")

@pytest.mark.fixture_stirng_param
def test_string_param(prams_with_string):
    print("string also possible in fixture params but each time characters will comes")

@pytest.mark.practice_factiries_fixture
def test_factory_fixture_check(factories_fixture):
    assert type(factories_fixture('string')) == str
    assert type(factories_fixture('list')) == list


@pytest.mark.practice_fixture_parametrization
def test_fixtures_params(fixture_parametrization):
    assert (type(fixture_parametrization)) in [tuple, list]

@pytest.mark.fixures_as_parametrization
def test_practice_fixtures_params(fixture_parametrization, fixture_params02):
    if fixture_params02 == "access":
        assert (fixture_parametrization[0])
    elif fixture_params02 == "slice":
        assert fixture_parametrization[::-1]