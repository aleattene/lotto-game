from random import randint


class NumbersPlay:

    # This static method acquires from the user the amount of numbers to generate for each ticket
    @staticmethod
    def acquire_amount_numbers(num_ticket, bet_key):
        # Maximum amount of numbers that can be played for each ticket
        MAX_AMOUNT_NUMBERS = 10
        while True:
            try:
                numbers = int(input("\nEnter the amount of numbers to play for the ticket "  # type INT
                                    "n. {} (from {} to {}): ".format(num_ticket, bet_key, MAX_AMOUNT_NUMBERS)))
                if bet_key <= numbers <= MAX_AMOUNT_NUMBERS:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        return numbers  # type INT

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
        return numbers  # type LIST (ascending order)











