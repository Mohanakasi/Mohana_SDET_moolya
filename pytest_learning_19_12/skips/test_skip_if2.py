import pytest
import sys

# pytestmark = pytest.mark.skipif(sys.platform == 'win32', reason="run only on ios")
pytestmark = [pytest.mark.skipif(sys.platform == 'win32', reason="run only on ios"), pytest.mark.skipif(pytest.__version__ > '7.4.3', reason='not rquire for latest python versions')]
def test_sanity1():
    print(sys.platform)
    print(pytest.__version__)
    print("set1 test cases")


def test_sanity2():
    print("set2 test cases")

def test_sanity3():
    print("sanity3 test cases")


#