class Ticket:

    def __init__(self, num_ticket, bet, city):
        self.num_ticket = num_ticket
        self.bet = bet
        self.city = city

    def __str__(self):
        return (f"""
        Ticket number: {self.num_ticket} 
        Bet Type: {self.bet} 
        City: {self.city} 
        """)
