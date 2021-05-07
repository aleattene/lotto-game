class Ticket:

    # List that will contain the tickets played
    tickets_played = []

    def __init__(self, id_ticket, bet_type, city, numbers):
        self.id_ticket = id_ticket
        self.bet_type = bet_type
        self.city = city
        self.numbers = numbers

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

    # This static method prints the tickets played
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
