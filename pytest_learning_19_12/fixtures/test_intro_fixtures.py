# # import pytest
# #
# # #defining the fixtures directly in test files
# # @pytest.fixture
# # def setup_city():
# #     print("\nthis is the starting of fixtuer")
# #     print("\nbeeing called by pytest, not you")
# #     cities = ['guntur', 'bangalore', 'mumbai']
# #     return cities
# #
# #
# # @pytest.mark.fixture_cities
# # def test_city_process(setup_city):
# #     print(setup_city[1:2])
# #     assert setup_city[0] == 'guntur'
# #
# #
# # def reverse_list(list):
# #     res = []
# #     for item in list:
# #         res = [item] + res
# #     return res
# #
# # def test_exam2(setup_city):
# #     assert setup_city[::-2] == ['mumbai','guntur']
# #     assert setup_city[::-1] == reverse_list(setup_city)
# #
# #
# #
# # #using fixtures by decorating with mark
# #
# # @pytest.mark.usefixtures("setup_city")
# # #while using usefixtures the fixture function should not have return statment
# # def test_method1():
# #     print(setup_city[::-1])
# #
# #
# # @pytest.mark.xfail(reason="known reason, test with use fixtuere, the fixture should not have return statement")
# # @pytest.mark.usefixtures("setup_city")
# # #while using usefixtures the fixture function should not have return statment
# # def test_method1():
# #     print(setup_city[::-1])
# #
# #
# # @pytest.mark.usefixtures("setup_city")
# # def test_method2():
# #     assert 'Mohana' == 'mohana'.capitalize()
# import pytest
#
#
# @pytest.fixture
# def fixtrure_intro_w1():
#     return "Mohana"
#
# @pytest.fixture
# def char_fixture():
#     string_ = 'Kasi viswanadh'
#     yield string_.split()
#
# @pytest.mark.fixture_practice_marker_220
# def test_practice_220(fixtrure_intro_w1):
#     print(type(fixtrure_intro_w1))
#
#
# @pytest.mark.char_fixture_2220
# @pytest.mark.usefixtures('char_fixture')
# def test_method_220(char_fixture):
#     print(char_fixture)
#
#
# @pytest.mark.char_fixture_221
# def test_method_2221()
