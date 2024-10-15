from src.math import add, subtract


def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert subtract(5,3) == 2
    
def test_subtract():
    assert subtract(2,3) == -1
    assert subtract(-1,1) == -2
    assert add(5,3) == 8
    
