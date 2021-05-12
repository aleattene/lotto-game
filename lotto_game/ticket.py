from lotto_game.extraction import Extraction


class Ticket:

    # List that will contain all the tickets played
    tickets_played = []

    def __init__(self, id_ticket, bet_type_id, bet_type_name, money_put, city, numbers):
        self.id_ticket = id_ticket      # type INT
        # .... bet_type must be an OBJECT (class BetType) but doesn't work
        self.bet_type_id = bet_type_id
        self.bet_type_name = bet_type_name
        self.money_put = money_put      # type FLOAT
        self.city = city                # type OBJECT (class City)
        self.numbers = numbers          # type LIST
        self.winning_wheels = []        # type LIST of win (obj of type Win)
        self.gross_amount = 0           # type FLOAT
        self.net_amount = 0             # type FLOAT

    def __str__(self):
        return (f"""
        Ticket number: {self.id_ticket} 
        Bet Type: {self.bet_type_name} 
        City: {self.city} 
        Numbers: {self.numbers} 
        Result: {self.winning_wheels} 
        """)

    # This instance method storages the tickets played
    def storage_ticket(self):
        Ticket.tickets_played.append(self)

    # This instance method checks whether the ticket is winning or not
    def check_ticket(self):
        # Tuple that will contain the cities and extracted numbers for each win
        wins = ()
        if self.city.name != "Tutte":  # city choice: only one
            # List that will contain the extracted numbers for each city
            extracted_numbers = []
            for number in Extraction.extraction[self.city.name]:  # type(number) = INT
                if number in self.numbers:
                    extracted_numbers.append(number)
            if len(extracted_numbers) >= self.bet_type_id:  # both of type INT
                wins += self.city.name, extracted_numbers  # type STR, type [int]
        else:   # cities chosen = "Tutte"
            for city in Extraction.extraction:
                extracted_numbers = []
                for number in Extraction.extraction[city]:  # type(number) = INT
                    if number in self.numbers:
                        extracted_numbers.append(number)
                if len(extracted_numbers) >= self.bet_type_id:  # both of type INT
                    wins += city, extracted_numbers  # type STR, type [int]
        return wins  # type TUPLE (str,[int])

    #
    def calculate_total_gross_net_amount(self):
        total_gross_amount = 0
        total_net_amount = 0
        for win in self.winning_wheels:
            total_gross_amount += win.gross_amount
            total_net_amount += win.net_amount
        self.gross_amount = total_gross_amount
        self.net_amount = total_net_amount

    # This method prints a ticket played
    def print_ticket(self):
        # Table HEADER
        print()
        print("╔{:^43}╗".format("═" * 43))     # ASCII code (201,205,187)
        print("║{:^43}║".format("Ticket n. {}".format(self.id_ticket)))     # ASCII code (186)
        print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
        # Table BODY
        print("║    Wheel:  {:31}║".format(self.city.name))  # ASCII code (186)
        print("║    Money:  {:31}║".format("€ {:.2f}".format(self.money_put)))  # ASCII code (186)
        # .... bet_type must be an OBJECT (class BetType) but doesn't work
        print("║  BetType:  {:31}║".format(self.bet_type_name))  # ASCII code (186)
        # In this section are printed the numbers played
        numbers = ""
        for number in self.numbers:  # type INT
            numbers += str(number) + " "
        print("║  Numbers:  {:31}║".format(numbers))  # ASCII code (186)
        print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
        # In this section has printed the winning result of the bet
        if self.winning_wheels:  # non-empty list
            print("║{:^43}║".format("Congratulations, you won."))
            for win in self.winning_wheels:  # type obj #######################
                print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
                print("║              Wheel: {:22}║".format(win.city_name))  # ASCII code (186)
                # In this section are printed the numbers extracted
                numbers = ""
                for value in win.extracted_numbers:
                    numbers += str(value) + " "
                print("║  Extracted numbers: {:22}║".format(numbers))  # ASCII code (186)
                # In this section are printed the winnings for each wheel/city
                print("║          Gross win:"
                      " {:22}║".format("€ {:.2f}".format(win.gross_amount)))  # ASCII code (186)
                print("║            Net win:"
                      " {:22}║".format("€ {:.2f}".format(win.net_amount)))  # ASCII code (186)
            print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
            # In this section has printed the total winnings for each ticket
            print("║    TOTAL GROSS WIN:"
                  " {:22}║".format("€ {:.2f}".format(self.gross_amount)))  # ASCII code (186)
            print("║      TOTAL NET WIN:"
                  " {:22}║".format("€ {:.2f}".format(self.net_amount)))  # ASCII code (186)
        # In this section has printed the losing result of the bet
        else:  # False
            print("║{:^43}║".format("{}".format("I’m sorry, you lost.")))  # ASCII code (186)
        # Table FOOTER
        print("╚{:^43}╝".format("═" * 43))  # ASCII code (200,205,188)

    # This static method acquires from the user the number of tickets to generate
    @staticmethod
    def acquire_number_tickets():
        # Minimum and maximum number of tickets that can be played
        MIN_TICKETS = 1
        MAX_TICKETS = 5
        while True:
            try:
                num_tickets = int(input("\nHow many tickets do you want to generate (between "  # type INT
                                        "{} and {}, 0 to quit)? ".format(MIN_TICKETS, MAX_TICKETS)))
                if num_tickets == 0:
                    print("\nThank you for your attention.\nThe simulation of the lotto game is terminated.")
                    quit()
                elif MIN_TICKETS <= num_tickets <= MAX_TICKETS:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again.")
        return MIN_TICKETS, num_tickets  # type TUPLE (int,int)

    # This static method acquires from the user the amount of money to put on each ticket
    @staticmethod
    def acquire_money_put_ticket(num_ticket):
        # Minimum and maximum amount of money to put on each ticket
        MIN_AMOUNT_MONEY = 1
        MAX_AMOUNT_MONEY = 200
        while True:
            try:
                amount_money = float(input("\nEnter the amount of money to put on the ticket " +  # type FLOAT
                                           "n. {} (between € {} and".format(num_ticket, MIN_AMOUNT_MONEY) +
                                           " € {}): € ".format(MAX_AMOUNT_MONEY)))
                # ... control 50 cents
                if MIN_AMOUNT_MONEY <= amount_money <= MAX_AMOUNT_MONEY:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again.")
        return amount_money  # type INT

