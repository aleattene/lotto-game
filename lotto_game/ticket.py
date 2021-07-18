class Ticket:

    # List that will contain all the tickets played
    tickets_played = []

    def __init__(self, id_ticket, bet_type, city, numbers):
        self.id_ticket = id_ticket      # type INT
        self.bet_type = bet_type        # type OBJECT (class BetType)
        self.city = city                # type OBJECT (class City)
        self.numbers = numbers          # type LIST

    def __str__(self):
        return (f"""
        Ticket number: {self.id_ticket} 
        Bet Type: {self.bet_type} 
        City: {self.city} 
        Numbers: {self.numbers} 
        """)

    # This instance method storages the tickets played
    def storage_ticket(self):
        Ticket.tickets_played.append(self)

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

    # This static method prints all the tickets played
    @staticmethod
    def print_tickets():
        print()
        for ticket in Ticket.tickets_played:
            print("╔{:^43}╗".format("═" * 43))     # ASCII code (201,205,187)
            print("║{:^43}║".format("Ticket n. {}".format(ticket.id_ticket)))     # ASCII code (186,186)
            print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
            print("║    Wheel:  {:31}║".format(ticket.city))  # ASCII code (186,186)
            print("║  BetType:  {:31}║".format(ticket.bet_type))  # ASCII code (186,186)
            numbers = ""
            for number in ticket.numbers:
                numbers += str(number) + " "
            print("║  Numbers:  {:31}║".format("{}".format(numbers)))  # ASCII code (186,186)
            print("╚{:^43}╝".format("═" * 43))  # ASCII code (200,205,188)
