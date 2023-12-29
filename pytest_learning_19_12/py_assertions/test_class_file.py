class Test_class_intro:
    def test_method1(self):
        assert type('Mohana') == str

    def test_method2(self):
        assert type(int('98')) == int

    def test_method3(self):
        assert 'mohana'.capitalize() == 'Mohana'