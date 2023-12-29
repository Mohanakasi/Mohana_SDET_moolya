import pytest

class Test_xfail_practice:

    @pytest.mark.xfail(reason='its not a proper index to fetch')
    def test_get_car_str_index(self):
        string_ = 'its a beutiful day'
        assert string_[18]

    @pytest.mark.xfail(reason='its not a proper index to fetch')
    def test_get_car_str_type2(self):
        string_ = 'its a beutiful day'
        assert string_[2]

    @pytest.mark.xfail(reason='you can not conctinate different data type')
    def test_str_num_concatinate(self):
        name = 'Mohana kasi'
        id = 1008
        assert name+id


