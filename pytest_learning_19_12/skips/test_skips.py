import pytest


def type_check(param):
    return type(param)

def test_string_rev():
    res = type_check('Mohana')
    assert res == str

def test_nums_cjheck():
    res = type_check(1008)
    assert res == int

@pytest.mark.skip
def test_float_check():
    res = type_check(5/3)
    assert res == float


@pytest.mark.skip(reason='skipping the list cases')
def test_list_type():
    res = type_check('this is Mohana'.split())
    assert res == list