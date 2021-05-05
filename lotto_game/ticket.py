class Ticket:

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
