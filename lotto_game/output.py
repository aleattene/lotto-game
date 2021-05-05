class Output:

    # This method receives the dictionary of tickets played and prints them
    @staticmethod
    def print_tickets(tickets_played):
        for k in sorted(tickets_played):
            # ... complete responsive layout
            print("╔{:^43}╗".format("═"*43))     # ASCII code (201,205,187)
            print("║{:^43}║".format("Ticket n. {}".format(k)))     # ASCII code (186,186)
            print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
            print("║  Wheel:  {:^33}║".format(" {}".format(tickets_played[k][1])))  # ASCII code (186,186)
            print("║  BetType:{:^33}║".format(" {}".format(tickets_played[k][2])))  # ASCII code (186,186)
            numbers = ""
            for value in tickets_played[k][0]:
                numbers += str(value) + " "
            print("║  Numbers:{:^33}║".format("{}".format(numbers)))  # ASCII code (186,186)
            print("╚{:^43}╝".format("═" * 43))  # ASCII code (200,205,188)
