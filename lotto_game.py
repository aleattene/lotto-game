from lotto_game.bet_type import BetType
from lotto_game.city import City
from lotto_game.numbers_play import NumbersPlay
from lotto_game.ticket import Ticket


def main():
    # DATA STRUCTURE DECLARATION

    # Acquisition of the number of tickets
    range_tickets = Ticket.acquire_number_tickets()  # type TUPLE (num_min_tickets,num_max_tickets)

    # TICKETS GENERATION
    for i in range(range_tickets[0], range_tickets[1] + 1):

        # Acquisition of the type of bet
        bet_key_name = BetType.acquire_bet_type(i)  # type TUPLE

        # Acquisition of the amount of numbers to play
        amount_numbers = NumbersPlay.acquire_amount_numbers(i, bet_key_name[0])  # type INT

        # Acquisition of the wheel(s) to play
        city_key_name = City.acquire_city(i)  # type TUPLE

        # SINGLE TICKET GENERATION
        # New Object of type City
        city = City(city_key_name[0], city_key_name[1])
        # New Object of type BetType
        bet = BetType(bet_key_name[0], bet_key_name[1])
        # Numbers generation
        generated_numbers = NumbersPlay.generate_numbers(amount_numbers)  # type LIST
        # New Object of type Ticket
        ticket = Ticket(i, bet.name, city.name, generated_numbers)

        # STORAGE OF THE PLAYED TICKET
        ticket.storage_ticket()

    # PRINTING OF THE TICKETS PLAYED
    Ticket.print_tickets()


if __name__ == "__main__":
    main()
