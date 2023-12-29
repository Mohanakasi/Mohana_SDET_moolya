class Test_1:
    def test_method1(self):
        print("iam method1")



class Test_2:
    def test_method1(self):
        print("iam method1")

    def test_method2(self):
        print("iam method2")

class Test_first_test:
    def test_method1(self):
        assert 'MOHANA' == 'mohana'.upper()
        print("end of the test")
    #
    def test_method2(self):
        assert 9/5 == '2.5', "fails math issues" #messsege with fail

    #
    def test_math_ops(self):
        assert 5+5 == 10
        assert 5-5 == 0
        assert 5/5 == 1
        assert 5//5 == 1


