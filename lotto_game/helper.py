from random import randint


class Helper:

    # This method returns an ordered list of integers (between MIN_NUMBER and MAX_NUMBERS)
    @staticmethod
    def generate_numbers(num_tickets):
        MIN_NUMBER = 1
        MAX_NUMBER = 90
        numbers = []
        while num_tickets > 0:
            number = randint(MIN_NUMBER, MAX_NUMBER + 1)
            if number not in numbers:
                numbers.append(number)
                num_tickets -= 1
        numbers.sort()
        return numbers





