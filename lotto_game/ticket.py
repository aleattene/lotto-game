from lotto_game.extraction import Extraction


class Ticket:

    # List that will contain all the tickets played
    tickets_played = []

    def __init__(self, id_ticket, bet_type_id, bet_type_name, city, numbers):
        self.id_ticket = id_ticket      # type INT
        # .... bet_type must be an OBJECT (class BetType) but doesn't work
        self.bet_type_id = bet_type_id
        self.bet_type_name = bet_type_name
        self.city = city                # type OBJECT (class City)
        self.numbers = numbers          # type LIST

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

    def check_ticket(self):
        if self.city.name != "Tutte":
            count = 0
            for number in Extraction.extraction[self.city.name]:
                if number in self.numbers:
                    count += 1
                    if count >= self.bet_type_id:
                        return True, self.city.name
        else:
            for city in Extraction.extraction:
                count = 0
                for number in Extraction.extraction[city]:
                    if number in self.numbers:
                        count += 1
                        if count >= self.bet_type_id:
                            return True, city
        return False, ""

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
            print("║    Wheel:  {:31}║".format(ticket.city.name))  # ASCII code (186,186)
            # .... bet_type must be an OBJECT (class BetType) but doesn't work
            print("║  BetType:  {:31}║".format(ticket.bet_type_name))  # ASCII code (186,186)
            numbers = ""
            for number in ticket.numbers:
                numbers += str(number) + " "
            print("║  Numbers:  {:31}║".format("{}".format(numbers)))  # ASCII code (186,186)
            print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
            result = ticket.check_ticket()
            if result[0]:  # True
                print("║{:^43}║".format("{}".format("Congratulations, you won. Wheel: "
                                                    "" + result[1])))  # ASCII code (186,186)
            else:  # False
                print("║{:^43}║".format("{}".format("I’m sorry, you didn't win.")))  # ASCII code (186,186)
            print("╚{:^43}╝".format("═" * 43))  # ASCII code (200,205,188)
