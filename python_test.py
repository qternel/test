from typing import Iterable
def sum_squares(lst:Iterable[float|int])->float|int:
    sum = 0
    for x in lst:
        sum += x * x
    return sum

def test_sum_squares_list():
    assert sum_squares([1,2,3])==14
    
def test_sum_squares_set():
    assert sum_squares(set([1,2,-3]))==14

def test_sum_squares_tuple():
    assert sum_squares((1,1,1,1,-1,-1,-1,-1))==8
    