class BetType:

    # Dictionary containing the type of bet
    all_bet_types = {1: "Ambata", 2: "Ambo", 3: "Terno", 4: "Quaterna", 5: "Cinquina"}

    def __init__(self, id_bet_type, name):
        self.id_bet_type = id_bet_type
        self.name = name

    # This static method acquires from the user the type of bet
    @staticmethod
    def acquire_bet_type(num_ticket):

        print("\n##### TICKET N. {} #####\n".format(num_ticket))
        for k in BetType.all_bet_types:
            print("       {}: {}".format(k, BetType.all_bet_types[k]))
        while True:
            try:
                bet_key = int(input("\nEnter the Type of Bet "
                                    "(between 1 and {}): ".format(len(BetType.all_bet_types))))  # type int
                if bet_key in BetType.all_bet_types:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        bet_name = BetType.all_bet_types[bet_key]
        return bet_key, bet_name
