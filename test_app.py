import pytest
from app import sum_list, count_negatives


@pytest.mark.parametrize("numbers, expected", [
    ([3, 1, 4, 1, 5, 9], 23),
    ([-5, 0, 15, -20 , 40], 30),
    ([42], 42)
    ([1,2,3,4],10)
])
def test_sum_list(numbers, expected):
    
    assert sum_list(numbers) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, -3, 4, -5], 2),
    ([2, 4, 6, 8], 0),      
    ([7, -3, 11, 0, 1], 1)
])
def test_count_negatives(numbers, expected):

    assert count_negatives(numbers) == expected