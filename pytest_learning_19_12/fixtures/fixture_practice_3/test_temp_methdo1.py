import pytest

class Test_class_temp:

    @pytest.mark.sample_fixture_practice_41
    def test_method_220(self, demo_fixture1, demo_fixture_2):
        print(demo_fixture1)

    @pytest.mark.sample_fixture_practice_41
    def test_method_2(self):
        print("metjhjdo2")

class Test_class_2:

    @pytest.mark.class_2_methods
    def file_methdod1(self, demo_fixture1, demo_fixture_2):
        print("method of class 2")



@pytest.mark.language_check
def test_language(data_fetch):
    if data_fetch < '4.0':
        raise TypeError


@pytest.mark.factory_fixture_practice
def test_fixture_practice_41(factory_fixture):
    print(factory_fixture("this is kasi world".split()))
    print(factory_fixture("this, can not , to judge".split(',')))
