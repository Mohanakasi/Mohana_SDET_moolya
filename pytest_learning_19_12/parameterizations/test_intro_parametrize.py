import pytest

# @pytest.mark.parametrize("user_name", ['Mohana', 'kasi', 'Rao'])
# def test_trial1(user_name):
#     print(user_name)

@pytest.mark.nums_check
@pytest.mark.parametrize("number", [109, 84, 45, 289])
def test_numbers_check(number):
    assert number > 100





@pytest.mark.user_pass_word
@pytest.mark.parametrize("user_name, pass_word", [('Mohana', 123), ('kasi', 4560), ('Rao', 789)])
def test_trial1(user_name, pass_word):
    assert isinstance(user_name, str)
    assert isinstance(pass_word, int)

@pytest.mark.strings_check_vowel
@pytest.mark.parametrize("string", ['integrate', 'Mohana', 'python', 'user_name'])
def test_vowels_check(string):
    assert string[0].lower() in 'aeiou'

@pytest.mark.multiplication
@pytest.mark.parametrize('input, output', [(2, 4), (8, 64), (45, 3458)])
def test_multiplication_validation(input, output):
    assert (input * input == output)
