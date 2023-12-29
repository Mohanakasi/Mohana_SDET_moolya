import pytest



class Test_conftest_ops:

    def test_list_ops(self, list_setup):
        list_setup.remove('python')
        print(list_setup)




def test_string_ops(string_setup):
    string_setup.replace('day', 'month')
    print(string_setup)