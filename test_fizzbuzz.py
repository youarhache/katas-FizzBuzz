from fizzbuzz import get_fizzbuzz

def test_when_3_then_fizz():
    result_3 = get_fizzbuzz(3)

    assert result_3 == "Fizz"


def test_when_5_then_buzz():
    result_5 = get_fizzbuzz(5)

    assert result_5 == "Buzz"

def test_when_1_then_1():
    result_1 = get_fizzbuzz(1)

    assert result_1 == 1

def test_when_13_then_13():
    result_13 = get_fizzbuzz(13)

    assert result_13 == 13