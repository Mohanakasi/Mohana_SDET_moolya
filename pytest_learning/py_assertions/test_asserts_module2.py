class Test_asserts:

    def test_type(self):
        assert type(1) == int

    def test_str(self):
        assert str.upper('Mohana') == 'MOHANA'
        assert 'mohana'.capitalize() == 'Mohana'
