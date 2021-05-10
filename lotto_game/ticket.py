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
        # .... result must be an OBJECT (class Win) but doesn't work
        self.result_city = []
        self.result_numbers = []
        self.result_gross_amount = []
        self.result_net_amount = []

    def __str__(self):
        return (f"""
        Ticket number: {self.id_ticket} 
        Bet Type: {self.bet_type_name} 
        City: {self.city} 
        Numbers: {self.numbers} 
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
            for number in Extraction.extraction[self.city.name]:
                if number in self.numbers:
                    extracted_numbers.append(number)
            if len(extracted_numbers) >= self.bet_type_id:
                wins += self.city.name, extracted_numbers
        else:   # cities chosen = "Tutte"
            for city in Extraction.extraction:
                extracted_numbers = []
                for number in Extraction.extraction[city]:
                    if number in self.numbers:
                        extracted_numbers.append(number)
                if len(extracted_numbers) >= self.bet_type_id:
                    wins += city, extracted_numbers
        return wins  # type TUPLE (str,[int])

    # This method prints a ticket
    def print_ticket(self):
        print()
        print("╔{:^43}╗".format("═" * 43))     # ASCII code (201,205,187)
        print("║{:^43}║".format("Ticket n. {}".format(self.id_ticket)))     # ASCII code (186)
        print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
        print("║    Wheel:  {:31}║".format(self.city.name))  # ASCII code (186)
        print("║    Money:  {:31}║".format("€ {:.2f}".format(self.money_put)))  # ASCII code (186)
        # .... bet_type must be an OBJECT (class BetType) but doesn't work
        print("║  BetType:  {:31}║".format(self.bet_type_name))  # ASCII code (186)
        numbers = ""
        for number in self.numbers:
            numbers += str(number) + " "
        print("║  Numbers:  {:31}║".format(numbers))  # ASCII code (186)
        print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
        if self.result_city:  # non-empty list
            print("║{:^43}║".format("Congratulations, you won."))
            for i, city in enumerate(self.result_city):
                print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
                print("║              Wheel: {:22}║".format(city))  # ASCII code (186)
                numbers = ""
                for value in self.result_numbers[i]:
                    numbers += str(value) + " "
                print("║  Extracted numbers: {:22}║".format(numbers))  # ASCII code (186)
                print("║          Gross win:"
                      " {:22}║".format("€ {:.2f}".format(self.result_gross_amount[i])))  # ASCII code (186)
                print("║            Net win:"
                      " {:22}║".format("€ {:.2f}".format(self.result_net_amount[i])))  # ASCII code (186)
            print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
            print("║    TOTAL GROSS WIN:"
                  " {:22}║".format("€ {:.2f}".format(sum(self.result_gross_amount))))  # ASCII code (186)
            print("║      TOTAL NET WIN:"
                  " {:22}║".format("€ {:.2f}".format(sum(self.result_net_amount))))  # ASCII code (186)
        else:  # False
            print("║{:^43}║".format("{}".format("I’m sorry, you lost.")))  # ASCII code (186)
        print("╚{:^43}╝".format("═" * 43))  # ASCII code (200,205,188)

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
        return amount_money  # type int
