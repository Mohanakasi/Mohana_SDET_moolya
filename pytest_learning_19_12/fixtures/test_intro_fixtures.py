import pytest

#defining the fixtures directly in test files
@pytest.fixture
def setup_city():
    print("\nthis is the starting of fixtuer")
    print("\nbeeing called by pytest, not you")
    cities = ['guntur', 'bangalore', 'mumbai']
    return cities


@pytest.mark.fixture_cities
def test_city_process(setup_city):
    print(setup_city[1:2])
    assert setup_city[0] == 'guntur'


def reverse_list(list):
    res = []
    for item in list:
        res = [item] + res
    return res

def test_exam2(setup_city):
    assert setup_city[::-2] == ['mumbai','guntur']
    assert setup_city[::-1] == reverse_list(setup_city)



#using fixtures by decorating with mark

@pytest.mark.usefixtures("setup_city")
#while using usefixtures the fixture function should not have return statment
def test_method1():
    print(setup_city[::-1])


@pytest.mark.xfail(reason="known reason, test with use fixtuere, the fixture should not have return statement")
@pytest.mark.usefixtures("setup_city")
#while using usefixtures the fixture function should not have return statment
def test_method1():
    print(setup_city[::-1])


@pytest.mark.usefixtures("setup_city")
def test_method2():
    assert 'Mohana' == 'mohana'.capitalize()
