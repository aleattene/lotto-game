from random import randint

# This function returns an ordered list of integers (between MIN_NUMBER and MAX_NUMBERS)
def generate_numbers(n):
    MIN_NUMBER = 1
    MAX_NUMBER = 90
    numbers = []
    while n > 0:
        number = randint(MIN_NUMBER, MAX_NUMBER + 1)
        if number not in numbers:
            numbers.append(number)
            n -= 1
    numbers.sort()
    return numbers





