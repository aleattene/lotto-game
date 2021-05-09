from lotto_game.bet_type import BetType
from lotto_game.city import City
from lotto_game.numbers import Numbers
from lotto_game.ticket import Ticket
from lotto_game.extraction import Extraction


def main():

    # Acquisition of the number of tickets to generate
    range_tickets = Ticket.acquire_number_tickets()  # type TUPLE (num_min_tickets,num_max_tickets)

    # TICKETS GENERATION
    for i in range(range_tickets[0], range_tickets[1] + 1):

        # Acquisition of the type of bet_type for each ticket
        bet_key_name = BetType.acquire_bet_type(i)  # type TUPLE (int,str)

        # Acquisition of the amount of numbers to generate for each ticket
        amount_numbers = Numbers.acquire_amount_numbers(i, bet_key_name[0])  # type INT

        # Acquisition of the wheel/city to play for each ticket
        city_key_name = City.acquire_city(i)  # type TUPLE (int,str)

        # SINGLE TICKET GENERATION
        # New Object of type City
        city = City(city_key_name[0], city_key_name[1])
        # New Object of type BetType
        bet_type = BetType(bet_key_name[0], bet_key_name[1])
        # Generation of the numbers to play for each ticket
        generated_numbers = Numbers.generate_numbers(amount_numbers)  # type LIST [int]
        # New Object of type Ticket
        # .... bet_type must be an OBJECT (class BetType) but doesn't work
        ticket = Ticket(i, bet_type.id_bet_type, bet_type.name, city, generated_numbers)

        # STORAGE OF EACH TICKET PLAYED
        ticket.storage_ticket()

    # PERFORM AND PRINT THE EXTRACTION
    Extraction.perform_extraction()
    Extraction.print_extraction()

    # PRINT OF ALL TICKETS
    Ticket.print_tickets()


if __name__ == "__main__":
    main()
