import pytest

# @pytest.mark.temp_220_marker
# def test_method_220():
#     print("test messeege")
#
# @pytest.mark.temp_220_marker
# def test_method_221():
#     print("test messeege")
#
# @pytest.mark.temp_220_marker
# def test_method_222():
#     print("test messeege")
#
#
# @pytest.mark.class_marker_500
# class Test_class_for_marker:
#
#     def test_method_1(self):
#         print("this is method area")
#
#     def test_method_2(self):
#         print("this is method area")
#
#     def test_method_3(self):
#         print("this is method area")
#
#
#


# class Test_class_456:
#
#     @pytest.mark.group1
#     def test_method12(self):
#         print("messege body")
#
#     @pytest.mark.group1
#     def test_method134(self):
#         print("messege body")
#
#     @pytest.mark.group1
#     def test_method120(self):
#         print("messege body")
#     @pytest.mark.group2
#     def test_method13(self):
#         print("messege body")

# pytestmark = [pytest.mark.practice_module_marker]
# def test_case_1():
#     print("messege")
#
# def test_case_23():
#     print("not the messege")
#
# class Test_case_4:
#
#     def test_class_method_1(self):
#         print(id(self))
#
#     @classmethod
#     def test_class_only_mehtod(cls):
#         print(id(cls))


@pytest.mark.xfail_marker_344
@pytest.mark.xfail(raises=IndexError)
def test_method_244():
   assert "mohana"[44]


# @pytest.mark.never_work
# @pytest.mark.xfail(raises=TypeError)
# def test_method_xfail_220():
#     assert {1, 324, 234}[0]



@pytest.mark.will_work_234
@pytest.mark.xfail(pytest.__version__ > '4.5.6', reason='not a valid version')
def test_method_xfail_cond():
    print(pytest.__version__)
    print("its a valid pytest version")

