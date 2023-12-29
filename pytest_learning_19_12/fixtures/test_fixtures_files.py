import pytest

@pytest.fixture
def file_setup():
    with open("file1.txt", 'w') as file1:
        file1.write("This is python language")
    with open("file1.txt", 'r') as file12:
        yield file12
    print("file closed")

@pytest.mark.usefixtures("file_setup")
def test_file_ops1(file_setup):
    assert file_setup.readline() == 'This is python language'

