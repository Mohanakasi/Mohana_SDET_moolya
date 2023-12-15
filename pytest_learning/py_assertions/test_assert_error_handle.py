import pytest
string_ = 'Mohana'
def test_1():
    with pytest.raises(IndexError):
        print(string_[10]) #as it gives index error

def test_2():
    with pytest.raises(ZeroDivisionError):
        assert 1/0
def test_3():
    with pytest.raises(TypeError) as set_key_error:
        set_ = {1,45, 'kasi'}
        print(set_[2])
    print(str(set_key_error)) #prints the exception messege


def value_exception():
    raise ValueError("value not found in string")

def test_4():
    with pytest.raises(Exception) as value_error:
        value_exception()
    print(str(value_error))
    print(str(value_error.value))

