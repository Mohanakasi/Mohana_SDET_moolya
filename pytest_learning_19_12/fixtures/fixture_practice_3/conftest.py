import pytest
# print(f"conftest /")
@pytest.fixture(scope='class')
def demo_fixture1():
    yield "sample data processed"
    print(f"end of the {demo_fixture1.__name__}")

@pytest.fixture(scope="module")
def demo_fixture_2():
    yield "module ficture executed"
    print(f"end of the fixture {demo_fixture_2.__name__}")


@pytest.fixture(params=['python', 'java', 'c'])
def data_fetch(request):
    if request.param == 'python':
        return '3.10'
    elif request.param == 'java':
        return '5.8'
    elif request.param == 'c':
        return '4.6'


@pytest.fixture
def factory_fixture():
    def finds_word_count(list_):
        return len(list_)
    return finds_word_count

