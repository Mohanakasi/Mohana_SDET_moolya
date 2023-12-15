import pytest
from pytest import mark
import sys
const = 9/5
def cen_to_fh(cent=0):
    fah = (cent*const) + 32
    return fah

"mark.skip will simply skips the test method without chekcing any condition"
@mark.skip("skiping typecheck as already know") #skip the test & returns the messege
def test_type_simple_skip():
    assert type(cen_to_fh()) == float

"skipif checks for a condition and returns the mentioned reason"
@mark.skipif(sys.version_info < (3,10), reason='chekcing skip if')
def test_validate1():
    assert cen_to_fh() == 32

def test_validate2():
    assert cen_to_fh(38) == 100.4

"""examples of skipif with sys module"""
@mark.skipif(sys.version_info > (3,2), reason='chekcing skip if')
def test_validate_version():
    assert cen_to_fh() == 32

@mark.skipif(100>1, reason="checking skipif")
def test_skip_condition():
    assert cen_to_fh(100) == 212


@mark.skipif(sys.platform == 'win32', reason="checking skipif")
def test_validate_platoform():
    assert cen_to_fh(100) == 212

@mark.skipif(pytest.__version__ < '6.4.6', reason='checking if with pytest version')
def test_pytest_version_less_then_check():
    assert cen_to_fh(140) == 284

@mark.skipif(pytest.__version__ > '7.3.2', reason='checking if with pytest version')
def test_pytest_version_check():
    assert cen_to_fh(140) == 284