from lotto_game.city import City


class Win:

    # Dictionary containing which and how many combinations can be achieved on a single wheel/city.
    combinations = {
        # Numbers: [Ambata, Ambo, Terno, Quaterna, Cinquina]
        1: [1],
        2: [2, 1],
        3: [3, 3, 1],
        4: [4, 6, 4, 1],
        5: [5, 10, 10, 5, 1]
    }

    # Dictionary containing the gross amount of winnings obtained by betting € 1 on a single wheel/city.
    gross_winnings = {
        # Numbers Played: [Ambata, Ambo, Terno, Quaterna, Cinquina]
        1: [11.23],
        2: [5.61, 250],
        3: [3.74, 83.33, 4500],
        4: [2.80, 41.66, 1125, 120000],
        5: [2.24, 25, 450, 24000, 6000000],
        6: [1.87, 16.66, 225, 8000, 1000000],
        7: [1.60, 11.90, 128.57, 3428.57, 285714.28],
        8: [1.40, 8.92, 80.35, 1714.28, 107142.85],
        9: [1.24, 6.94, 53.57, 952.38, 47619.04],
        10: [1.12, 5.55, 37.50, 571.42, 23809.52]
    }

    def __init__(self, city_name, extracted_numbers):
        self.city_name = city_name                  # type STR
        self.extracted_numbers = extracted_numbers  # type LIST of INT
        self.gross_amount = 0.0                     # type FLOAT
        self.net_amount = 0.0                       # type FLOAT

    def __str__(self):
        return (f"""
        City: {self.city_name}
        Numbers: {self.extracted_numbers}
        Gross Amount: {self.gross_amount}
        Net Amount: {self.net_amount}
       """)

    # This instance method calculates the gross and net win for each wheel/city played
    def calculate_gross_net_win(self, ticket):
        TAX = (100 - 8) / 100  # Tax = 8%
        # Combinations can be achieved on a single wheel/city
        combinations = Win.combinations[len(self.extracted_numbers)][ticket.bet_type_id - 1]
        # GROSS WINNING FOR A SINGLE WHEEL/CITY PLAYED
        amount = (Win.gross_winnings[len(ticket.numbers)][ticket.bet_type_id-1]) * combinations * ticket.money_put
        if ticket.city.name == "Tutte":
            # Subdivision gross winning between all wheels/cities played and instance attribute updating
            self.gross_amount = amount / (len(City.all_cities)-1)
        else:
            # Instance attribute updating
            self.gross_amount = amount
        # Instance attribute updating
        self.net_amount = self.gross_amount * TAX






