class Input:

    # This static method acquires from the user the number of tickets to generate
    @staticmethod
    def acquire_number_tickets():
        # Minimum and maximum number of tickets that can be played
        MIN_TICKETS = 1
        MAX_TICKETS = 5
        while True:
            try:
                num_tickets = int(input("\nHow many tickets do you want to generate (between "
                                        "{} and {}, 0 to quit)? ".format(MIN_TICKETS, MAX_TICKETS)))  # type int
                if num_tickets == 0:
                    print("\nThank you for your attention.\nThe simulation of the lotto game is terminated.")
                    quit()
                elif MIN_TICKETS <= num_tickets <= MAX_TICKETS:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again.")
        return MIN_TICKETS, num_tickets

    # This static method acquires from the user the amount of numbers to generate for each ticket
    @staticmethod
    def acquire_amount_numbers(num_ticket, bet_key):
        # Maximum amount of numbers that can be played for each ticket
        MAX_AMOUNT_NUMBERS = 10
        while True:
            try:
                numbers = int(input("\nEnter the amount of numbers to play for the ticket "
                                    "n. {} (from {} to {}): ".format(num_ticket, bet_key, MAX_AMOUNT_NUMBERS)))  # type int
                if bet_key <= numbers <= MAX_AMOUNT_NUMBERS:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        return numbers



