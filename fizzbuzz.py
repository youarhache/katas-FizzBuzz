def get_fizzbuzz(number: int):
    if is_multiple_of_3_and_5(number):
        return "FizzBuzz"
    elif is_multiple_of_3(number):
        return "Fizz"
    elif is_multiple_of_5(number):
        return "Buzz" 
    return number

def is_multiple_of_3_and_5(number):
    return number % 5 == number % 3 == 0

def is_multiple_of_5(number):
    return number % 5 == 0

def is_multiple_of_3(number):
    return number % 3 == 0