import pytest
list1 = ['mon', 'tue', 'wed']
list2 = ['thur', 'fri', 'sat']

@pytest.fixture
def setup_weeks_01():
    print("in the fixture")
    wk1 = list1.copy()
    yield wk1
    wk1.pop()
    print("\n after the fixture")
    print("\n closing week sun")


@pytest.fixture
def setup_02():
    print("in fixture2")
    wk2 = list2.copy()
    wk2.append("new_week_day")
    yield wk2
    print("\n after the fixture2")
    wk2.pop()

@pytest.mark.setup_fixtures_1
@pytest.mark.usefixtures("setup_weeks_01")
def test_setup_fixtures(setup_weeks_01):
   print("\n in the test case")
   setup_weeks_01.append('sun')
   setup_weeks_01.extend(list2)
   assert setup_weeks_01 == ['mon', 'tue', 'wed','sun','thur', 'fri', 'sat']



@pytest.mark.fixture_method2
@pytest.mark.usefixtures("setup_weeks_01", "setup_02")
def test_length_validation(setup_weeks_01, setup_02):
    assert len(setup_02) != len(setup_weeks_01)

