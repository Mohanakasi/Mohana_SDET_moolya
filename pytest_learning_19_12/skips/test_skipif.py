import sys
import pytest

@pytest.mark.skipif(sys.version_info < (3,5), reason='skipping as low version installed')
def test_low_python_version_validate():
    print("proper python version")


@pytest.mark.skipif(sys.version_info > (3,5), reason='not required for higher versions')
def test_high_python_version_validate():
    print("least python version")


#cheecking for latest python version
@pytest.mark.skipif(pytest.__version__ <'7.4.3', reason='old python version installed')
def test_py_version_check():
    print("latest pytest version")


#checking for old python version
@pytest.mark.skipif(pytest.__version__ > '7.4.3', reason='not rquire for latest python versions')
def test_py_version_check():
    print("old python version only installed")