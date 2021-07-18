from lotto_game.bet_type import BetType
from lotto_game.city import City
from lotto_game.numbers_play import NumbersPlay
from lotto_game.ticket import Ticket


def main():

    # Acquisition of the number of tickets to generate
    range_tickets = Ticket.acquire_number_tickets()  # type TUPLE (num_min_tickets,num_max_tickets)

    # TICKETS GENERATION
    for i in range(range_tickets[0], range_tickets[1] + 1):

        # Acquisition of the type of bet for each ticket
        bet_key_name = BetType.acquire_bet_type(i)  # type TUPLE (int,str)

        # Acquisition of the amount of numbers to generate for each ticket
        amount_numbers = NumbersPlay.acquire_amount_numbers(i, bet_key_name[0])  # type INT

        # Acquisition of the wheel/city to play for each ticket
        city_key_name = City.acquire_city(i)  # type TUPLE (int,str)

        # SINGLE TICKET GENERATION
        # New Object of type City
        city = City(city_key_name[0], city_key_name[1])
        # New Object of type BetType
        bet_type = BetType(bet_key_name[0], bet_key_name[1])
        # Generation of the numbers to play for each ticket
        generated_numbers = NumbersPlay.generate_numbers(amount_numbers)  # type LIST [int]
        # New Object of type Ticket
        ticket = Ticket(i, bet_type.name, city.name, generated_numbers)

        # STORAGE OF EACH TICKET PLAYED
        ticket.storage_ticket()

    # PRINT OF ALL TICKETS PLAYED
    Ticket.print_tickets()


if __name__ == "__main__":
    main()
