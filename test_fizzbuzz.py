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


def test_when_14_then_14():
    result_14 = get_fizzbuzz(14)

    assert result_14 == 14


def test_when_6_then_Fizz():
    result_6 = get_fizzbuzz(6)

    assert result_6 == "Fizz"


def test_when_21_then_Fizz():
    result_21 = get_fizzbuzz(21)

    assert result_21 == "Fizz"


def test_when_10_then_Buzz():
    result_10 = get_fizzbuzz(10)

    assert result_10 == "Buzz"


