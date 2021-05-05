class Input:

    # Acquisition of the number of tickets
    @staticmethod
    def acquire_number_tickets(min_tickets, max_tickets):
        while True:
            try:
                num_tickets = int(input("\nHow many tickets do you want to generate (between 1 and 5, 0 to quit)? "))  # type int
                if num_tickets == 0:
                    print("\nThank you for your attention.\nThe simulation of the lotto game is terminated.")
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
    def acquire_bet_type(num_ticket, all_bet_types):
        print("\n##### TICKET N. {} #####\n".format(num_ticket))
        for k in all_bet_types:
            print("       {}: {}".format(k, all_bet_types[k]))
        while True:
            try:
                bet_key = int(input("\nEnter the Type of Bet (between 1 and {}): ".format(len(all_bet_types))))  # type int
                if bet_key in all_bet_types:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        bet_name = all_bet_types[bet_key]
        return bet_key, bet_name

    # Acquisition of the amount of numbers to play
    @staticmethod
    def acquire_amount_numbers(num_ticket, bet_key, max_numbers):
        while True:
            try:
                numbers = int(input("\nEnter the amount of numbers to play for the ticket "
                                    "n. {} (from {} to {}): ".format(num_ticket, bet_key, max_numbers)))  # type int
                if bet_key <= numbers <= max_numbers:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        return numbers

    # Acquisition of the wheel(s) to play
    @staticmethod
    def acquire_wheel(num_ticket, all_cities):
        print()
        for k in all_cities:
            print("       {}: {}".format(k, all_cities[k]))
        while True:
            try:
                city_key = int(input("\nEnter the city for the ticket n. "
                                     "{} (between 1 and {}): ".format(num_ticket, len(all_cities))))   # type int
                if city_key in all_cities:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        city_name = all_cities[city_key]
        return city_key, city_name

