class BetType:

    # Dictionary containing all the type of lotto bet
    all_bet_types = {1: "Ambata", 2: "Ambo", 3: "Terno", 4: "Quaterna", 5: "Cinquina"}

    def __init__(self, id_bet_type, name):
        self.id_bet_type = id_bet_type
        self.name = name

    def __str__(self):
        return (f"""
        Id Bet Type: {self.id_bet_type} 
        Bet Type: {self.name}  
        """)

    # This static method acquires from the user the type of bet
    @staticmethod
    def acquire_bet_type(num_ticket):
        print()
        for k in BetType.all_bet_types:  # type INT
            print("       {}: {}".format(k, BetType.all_bet_types[k]))
        while True:
            try:
                bet_key = int(input("\nEnter the type of bet for the ticket n. "    # type INT
                                    "{} (between 1 and {}): ".format(num_ticket, len(BetType.all_bet_types))))
                if bet_key in BetType.all_bet_types:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again.")
        bet_name = BetType.all_bet_types[bet_key]   # type STR
        return bet_key, bet_name  # type TUPLE (int,str)
