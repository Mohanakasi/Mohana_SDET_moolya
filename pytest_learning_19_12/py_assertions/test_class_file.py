# class Test_class_intro:
#     def test_method1(self):
#         assert type('Mohana') == str
#
#     def test_method2(self):
#         assert type(int('98')) == int
#
#     def test_method3(self):
#         assert 'mohana'.capitalize() == 'Mohana'
import pytest


class Test_class2:

    @pytest.mark.my_methdos
    def test_practice_method1(self):
        print("this is method1")

    @pytest.mark.my_methdos
    def test_practice_meethod2(self):
        print("this is method2")


@pytest.mark.parametrize_practice_220
class Test_class3:

    @pytest.mark.xfail(reason="length error got it")
    @pytest.mark.parametrize("string, length", [('kasi', 4), ('Mohana', 6), ('Rao', 4)])
    def test_method_220(self, string, length):
        assert len(string) == length

    @pytest.mark.parametrize("combination1", [1,2,3,4,5]) #5
    @pytest.mark.parametrize('combination2', [6,7,8,9]) #4  total tests is 5 * 4 = 20
    def test_file2(self, combination1, combination2):
        print(combination1, combination2)

