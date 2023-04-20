from app import isEven

def test_isEven():
    assert (isEven(1) == False)
    assert (isEven(2) == True)
    assert (isEven(3) == False)
    assert (isEven(4) == True)
    assert (isEven(5) == False)
    assert (isEven(6) == True)
    assert (isEven(7) == False)
    assert (isEven(8) == True)
    assert (isEven(9) == False)
    assert (isEven(10) == True)
