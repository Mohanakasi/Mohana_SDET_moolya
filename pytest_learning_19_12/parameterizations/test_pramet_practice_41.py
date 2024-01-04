import pytest
@pytest.fixture
# @pytest.mark.parametrize("name",["Mohana kasi", 'Rao', 'viswa']) fixtures not works
def string_pass():
    return 'kasi'

@pytest.mark.name_fixtures_param
@pytest.mark.parametrize("company, desig", [('moolya', 'xyz'), ('sdet', 'ET')])
def test_details_fetch(string_pass,company, desig):
    print(string_pass, company, desig)