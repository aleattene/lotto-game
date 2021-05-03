
from lotto_game.bet import Bet
from lotto_game.city import City
from lotto_game.helper import generate_numbers, print_tickets
from lotto_game.ticket import Ticket


def main():
    all_cities = {1: "Bari", 2: "Cagliari", 3: "Firenze", 4: "Genova", 5: "Milano",
                  6: "Napoli", 7: "Palermo", 8: "Roma", 9: "Torino", 10: "Venezia", 11: "Tutte"}
    all_bets = {1: "Ambata", 2: "Ambo", 3: "Terno", 4: "Quaterna", 5: "Cinquina"}
    tickets_played = {}
    MIN_TICKETS = 1
    MAX_TICKETS = 5
    MAX_NUMBERS = 10
    # Entering the number of tickets
    while True:
        try:
            num_tickets = int(input("How many bills do you want to play (min 1 , max 5, 0  exit): "))   # type int
            if MIN_TICKETS <= num_tickets <= MAX_TICKETS:
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect Entry. Try Again")
    # Tickets generation
    for i in range(1, num_tickets+1):
        print("### TICKET N. {} ###".format(i))
        # Entering the type of bet
        for k in all_bets:
            print("  {} : {}".format(k, all_bets[k]))
        while True:
            try:
                bet_key = int(input("Bet Type ? : "))   # type int
                if bet_key in all_bets:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        # Entering the number of numbers to play
        while True:
            try:
                numbers = int(input("Numbers (from {} to 10) : ".format(bet_key)))  # type int
                if bet_key <= numbers <= MAX_NUMBERS:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
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
        bet_name = all_bets[bet_key]
        bet = Bet(bet_name)     # new object of type Bet
        selected_numbers = generate_numbers(numbers)
        ticket = Ticket(i, bet.name, city.name, selected_numbers)
        # Ticket storage
        tickets_played[ticket.num_ticket] = (ticket.numbers, ticket.city, ticket.bet)
        print_tickets(tickets_played)


if __name__ == "__main__":
    main()
