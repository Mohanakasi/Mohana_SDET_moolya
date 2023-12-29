import sys

import pytest

@pytest.mark.xfail(raises=IndexError, reason='index is out of the range')
#other than index error it will fails the test case
def test_char_fetch_1():
    string_ = 'python is full of puzle codes'
    assert string_[25]

@pytest.mark.xfail(raises=IndexError, reason='index is out of the range')
def test_char_fetch():
    string_ = 'python is full of puzle codes'
    assert string_+1

@pytest.mark.xfail(sys.platform == 'win32', reason='its work in linux only')
def test_platform_check():
    print("in linux version")

@pytest.mark.xfail(sys.platform == 'linux', reason='its work in windows only')
def test_wind_platform_check():
    print("in windows version")
