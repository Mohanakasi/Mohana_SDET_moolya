import pytest

@pytest.mark.strings_sanity
def test_merging_strings():
    return "mohana"+"kasi"

@pytest.mark.lists
def test_string_first_letter_check():
    list_ = ['Mohana', 'mac', 'bhavani',  'lokitha']
    list_2 = []
    for string_ in list_:
        if 'a'<=string_[0].lower()<='s':
            list_2.append(string_)

@pytest.mark.lists
def test_unpacking_list_items():
    data1,data2 = ['Mohana', 'guntur']
    print(data1, data2)

@pytest.mark.strings_sanity
def test_string_even_check():
    string_ = 'this is mohana'
    if len(string_) %2 == 0:
        return True

@pytest.mark.strings_sanity
def test_string_revrse():
    list_ = [1089, 'bengaluru', {'kasi'}]
    for item in list_:
        if isinstance(item, str):
            print(item[::-1])



