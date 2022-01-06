from fizzbuzz import print_fizzbuzz

def test_when_3_then_fizz():
    result_3 = print_fizzbuzz(3)

    assert result_3 == "Fizz"