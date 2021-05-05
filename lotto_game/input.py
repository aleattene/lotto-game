class Input:

    # Acquisition of the number of tickets
    @staticmethod
    def acquire_number_tickets(min_tickets, max_tickets):
        while True:
            try:
                num_tickets = int(input("How many tickets do you want to play (between 1 and 5, 0 to quit)? "))  # type int
                if num_tickets == 0:
                    print("Thank you. The simulation of the lotto game is over.")
                    quit()
                elif min_tickets <= num_tickets <= max_tickets:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again.")
        return num_tickets

    # Acquisition of the type of bet
    @staticmethod
    def acquire_bet_type(num_ticket, all_bets):
        print("##### TICKET N. {} #####".format(num_ticket))
        for k in all_bets:
            print("  {} : {}".format(k, all_bets[k]))
        while True:
            try:
                bet_key = int(input("Bet Type ? : "))  # type int
                if bet_key in all_bets:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        bet_name = all_bets[bet_key]
        return bet_key, bet_name

    # Acquisition of the amount of numbers to play
    @staticmethod
    def acquire_amount_numbers(bet_key, max_numbers):
        while True:
            try:
                numbers = int(input("Numbers (from {} to 10) : ".format(bet_key)))  # type int
                if bet_key <= numbers <= max_numbers:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
