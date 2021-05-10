from lotto_game.city import City


class Win:

    combinations = {
        1: [1],
        2: [2, 1],
        3: [3, 3, 1],
        4: [4, 6, 4, 1],
        5: [5, 10, 10, 5, 1]
    }

    gross_winnings = {
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

    def __init__(self, city, extracted_numbers):
        self.city = city
        self.extracted_numbers = extracted_numbers
        self.gross_amount = 0
        self.net_amount = 0

    def __str__(self):
        return (f"""
        City: {self.city}
        Numbers: {self.extracted_numbers}
       """)

    def calculate_gross_net_win(self, ticket):
        TAX = (100 - 8) / 100
        combinations = Win.combinations[len(self.extracted_numbers)][ticket.bet_type_id - 1]
        amount = (Win.gross_winnings[len(ticket.numbers)][ticket.bet_type_id-1]) * combinations * ticket.money_put
        if ticket.city.name == "Tutte":
            self.gross_amount = amount / (len(City.all_cities)-1)
        else:
            self.gross_amount = amount
        self.net_amount = self.gross_amount * TAX





