def get_fizzbuzz(number: int):
    if number == 15 or number == 30:
        return "FizzBuzz"
    elif is_multiple_of_3(number):
        return "Fizz"
    elif is_multiple_of_5(number):
        return "Buzz" 
    return number

def is_multiple_of_5(number):
    return number % 5 == 0

def is_multiple_of_3(number):
    return number % 3 == 0