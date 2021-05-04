class Output:

    # This method receives the dictionary of tickets played and prints them
    @staticmethod
    def print_tickets(tickets_played):
        for k in sorted(tickets_played):
            # ... complete responsive layout
            print("╔" + "═" * 20 + "╗")     # ASCII code (201,205,187)
            print("║     Ticket n. {}    ║".format(k))     # ASCII code (186,186)
            print("╠" + "═" * 20 + "╣")     # ASCII code (204,205,185)
            print("║ Numbers : {}     ║".format(tickets_played[k][0]))
            print("║ Wheel: {}        ║".format(tickets_played[k][1]))
            print("║ Bet Type : {}  ║".format(tickets_played[k][2]))
            print("╚" + "═" * 20 + "╝")     # ASCII code (200,205,188)
