from lotto_game.input import Input
from lotto_game.bet import Bet
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
    MAX_NUMBERS = 10
    # Dictionary containing the type of bet
    all_bets = {1: "Ambata", 2: "Ambo", 3: "Terno", 4: "Quaterna", 5: "Cinquina"}
    # Dictionary containing the cities(aka "wheel") that can be chosen for the bet
    all_cities = {1: "Bari", 2: "Cagliari", 3: "Firenze", 4: "Genova", 5: "Milano",
                  6: "Napoli", 7: "Palermo", 8: "Roma", 9: "Torino", 10: "Venezia", 11: "Tutte"}

    # Dictionary that will contain the tickets played
    tickets_played = {}

    # Acquisition of the number of tickets
    num_tickets = Input.acquire_number_tickets(MIN_TICKETS, MAX_TICKETS)

   # TICKETS GENERATION
    for i in range(1, num_tickets + 1):

        # Acquisition of the type of bet
        bet_key_name = Input.acquire_bet_type(i, all_bets)  # type tuple

        # Acquisition of the amount of numbers to play
        numbers = Input.acquire_amount_numbers(bet_key_name[0], MAX_NUMBERS)

        # Entering the wheel (city) to play
        for k in all_cities:
            print("  {}: {}".format(k, all_cities[k]))
        while True:
            try:
                city_key = int(input("Choice the city (between 1 and 11) : "))   # type int
                if city_key in all_cities:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        # Single Ticket Generation
        city_name = all_cities[city_key]
        city = City(city_name)  # new object of type City

        bet = Bet(bet_key_name[1])     # new object of type BetType
        selected_numbers = Helper.generate_numbers(numbers)
        ticket = Ticket(i, bet.name, city.name, selected_numbers)

        # Ticket storage
        tickets_played[ticket.num_ticket] = (ticket.numbers, ticket.city, ticket.bet)

        # PRINTING OF THE TICKETS PLAYED
        Output.print_tickets(tickets_played)


if __name__ == "__main__":
    main()
