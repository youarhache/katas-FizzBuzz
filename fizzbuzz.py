def get_fizzbuzz(number: int):
    if is_multiple_of_6(number):
        return "Fizz"
    elif number == 5:
        return "Buzz" 
    return number

def is_multiple_of_6(number):
    return number % 3 == 0