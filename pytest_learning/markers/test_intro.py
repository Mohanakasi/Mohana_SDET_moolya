from pytest import mark

"a test function can have mote than one markers"
@mark.sanity
def test_length_checking():
    string_ = 'Mohana'
    assert len(string_) == 6

def test_first_index_last_index():
    string_ = 'Iam from moolya'
    assert string_[0] == 'I'
    assert string_[-1] == 'a' == string_[14]

@mark.sanity2
def test_dividing_words():
    string_ = 'We all together come here'
    assert string_.split() == ['We', 'all', 'together', 'come', 'here']

def test_upper():
    string_ = 'Mohana'
    assert string_.upper() == 'MOHANA'

def test_joins():
    string_ = 'This is Mohana kasi'
    assert '$'.join(string_) == 'This$is$Mohana$kasi'

