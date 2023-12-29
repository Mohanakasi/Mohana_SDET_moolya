import math

import pytest

data = [([1,9,25], 'sum', 35),
        ([1,5,6], 'prod', 30)]

@pytest.mark.test1_maths
@pytest.mark.parametrize("nums_list, opration, value", data)
def test_maths_ops(nums_list, opration, value):
    if opration == 'sum':
        assert sum(nums_list) == value

    elif opration == 'prod':
        assert math.prod(nums_list) == value


