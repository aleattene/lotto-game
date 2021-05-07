from lotto_game.input import Input
from lotto_game.bet_type import BetType
from lotto_game.city import City
from lotto_game.helper import Helper
from lotto_game.output import Output
from lotto_game.ticket import Ticket


def main():
    # DECLARATION OF VARIABLES, CONSTANTS AND DATA STRUCTURES

    # Minimum and maximum number of tickets that can be played
    MIN_TICKETS = 1
    MAX_TICKETS = 5

    # Maximum amount of numbers that can be played for each ticket
    MAX_AMOUNT_NUMBERS = 10

    # Range of numbers that can be generated in the lotto game
    MIN_NUMBER = 1
    MAX_NUMBER = 90

    # Dictionary containing the type of bet
    all_bet_types = {1: "Ambata", 2: "Ambo", 3: "Terno", 4: "Quaterna", 5: "Cinquina"}

    # Dictionary containing the cities(aka "wheel") that can be chosen for the bet
    all_cities = {1: "Bari", 2: "Cagliari", 3: "Firenze", 4: "Genova", 5: "Milano",
                  6: "Napoli", 7: "Palermo", 8: "Roma", 9: "Torino", 10: "Venezia", 11: "Tutte"}

    # Dictionary that will contain the played tickets
    tickets_played = {}

    # Acquisition of the number of tickets
    num_tickets = Input.acquire_number_tickets(MIN_TICKETS, MAX_TICKETS)

    # TICKETS GENERATION
    for i in range(MIN_TICKETS, num_tickets + 1):

        # Acquisition of the type of bet
        bet_key_name = Input.acquire_bet_type(i, all_bet_types)  # type TUPLE

        # Acquisition of the amount of numbers to play
        amount_numbers = Input.acquire_amount_numbers(i, bet_key_name[0], MAX_AMOUNT_NUMBERS)  # type INT

        # Acquisition of the wheel(s) to play
        city_key_name = Input.acquire_wheel(i, all_cities)  # type TUPLE

        # SINGLE TICKET GENERATION
        # New Object of type City
        city = City(city_key_name[0], city_key_name[1])
        # New Object of type BetType
        bet = BetType(bet_key_name[0], bet_key_name[1])
        # Numbers generation
        generated_numbers = Helper.generate_numbers(amount_numbers, MIN_NUMBER, MAX_NUMBER)  # type LIST
        # New Object of type Ticket
        ticket = Ticket(i, bet.name, city.name, generated_numbers)

        # STORAGE OF THE PLAYED TICKET
        Helper.storage_ticket(tickets_played, ticket)

    # PRINTING OF THE TICKETS PLAYED
    Output.print_tickets(tickets_played)


if __name__ == "__main__":
    main()
