import pytest

# class files_fixtures:

@pytest.fixture
def setup_file():
    print("executing 2nd conftest")
    with open("sample_file1.txt", 'x') as fiel1:
        print("file is created")



@pytest.fixture
def file_data_create():
    with open("sample_file1.txt", 'w') as file2:
        file2.write("sample notes for testing multiple conftests")
    print("file closed")


@pytest.fixture
def file_read():
    with open("sample_file1.txt", 'r') as file3:
        yield file3
