from random import randint


class Helper:

    # This static method returns an ordered list of integers (between min_number and max_number)
    @staticmethod
    def generate_numbers(amount_numbers):
        # Range of numbers that can be generated in the lotto game
        MIN_NUMBER = 1
        MAX_NUMBER = 90
        numbers = []
        while amount_numbers > 0:
            number = randint(MIN_NUMBER, MAX_NUMBER + 1)
            if number not in numbers:
                numbers.append(number)
                amount_numbers -= 1
        numbers.sort()
        return numbers










