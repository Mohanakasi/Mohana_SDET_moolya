import pytest

pytestmark = [pytest.mark.str, pytest.mark.list] #mark at module level
"here we need to use fixed global variable called pytestmark then only it works"

def test_str_method():
    print("kasi is back".split())

def test_str_method_upper():
    print("python is a language".upper())

def test_list_reverse():
    print([109, 'kasi', 1.56, True][::-1])

def test_list_merge():
    print(['kasi']+['Mohana'])

def test_list_dict_pick():
    list_ = []


class Test_temp_markers:

    def test_method1(self):
        print("iam method1")

    def test_method2(self):
        print("iam method2")

    def test_string_rev_list(self):
        list_ = ['mohana', 1008]
        for item in list_:
            if isinstance(item, str):
                print((item)[::-1])

