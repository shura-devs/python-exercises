from basic_exercises import *

def test_reverse_list():
    my_list = []
    assert [] == reverse_list(my_list)

    my_list = [1,2,3]
    assert [3,2,1] == reverse_list(my_list)