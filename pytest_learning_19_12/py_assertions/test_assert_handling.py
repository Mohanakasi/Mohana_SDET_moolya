import pytest


class Test_intro_pytest_raises:
    def test_method1(self):
        with pytest.raises(ZeroDivisionError):
            assert 1/0
            # assert 3<2

    def index_out_range_error(self):
        raise IndexError
    def test_method2(self):
        with pytest.raises(Exception) as index_handle:
            string_ = 'Mohana kasi'
            assert string_[89]
            self.index_out_range_error()
        print(str(index_handle.value))

    def test_method_error1(self):
        print("str" + {'a': 1})


    def test_method_error2(self):
        print("Mohana"[87])