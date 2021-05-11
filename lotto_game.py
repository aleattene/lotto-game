import argparse
from lotto_game.bet_type import BetType
from lotto_game.city import City
from lotto_game.number_utils import NumberUtils
from lotto_game.ticket import Ticket
from lotto_game.extraction import Extraction
from lotto_game.win import Win


def main():

    try:
        # Acquisition of the number of tickets to generate directly from command line
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--num_ticket", help="Number of tickets")
        args = parser.parse_args()
        # Check insertion of the correct value
        if 1 <= int(args.num_ticket) <= 10:
            range_tickets = (1, int(args.num_ticket))  # type TUPLE (1, max 10)
        else:
            raise ValueError
    except ValueError:
        # Error message
        print("\nWarning, you have entered from the command line a value not allowed.")
        # Acquisition of the number of tickets to generate from the user
        range_tickets = Ticket.acquire_number_tickets()  # type TUPLE (num_min_tickets,num_max_tickets)

    # TICKETS GENERATION
    for i in range(range_tickets[0], range_tickets[1] + 1):

        # Acquisition of the type of bet_type for each ticket
        bet_key_name = BetType.acquire_bet_type(i)  # type TUPLE (int,str)

        # Acquisition of the amount of numbers to generate for each ticket
        amount_numbers = NumberUtils.acquire_amount_numbers(i, bet_key_name[0])  # type INT

        # Acquisition of the amount of money to put on each ticket
        amount_money = Ticket.acquire_money_put_ticket(i)  # type FLOAT

        # Acquisition of the wheel/city to play for each ticket
        city_key_name = City.acquire_city(i)  # type TUPLE (int,str)

        # SINGLE TICKET GENERATION
        # New Object of type City
        city = City(city_key_name[0], city_key_name[1])

        # New Object of type BetType
        bet_type = BetType(bet_key_name[0], bet_key_name[1])

        # Generation of the numbers to play for each ticket
        generated_numbers = NumberUtils.generate_numbers(amount_numbers)  # type LIST [int]

        # New Object of type Ticket
        # .... bet_type must be an OBJECT (class BetType) but doesn't work
        ticket = Ticket(i, bet_type.id_bet_type, bet_type.name, amount_money, city, generated_numbers)

        # STORAGE OF EACH TICKET PLAYED
        ticket.storage_ticket()

    # PERFORM AND PRINT THE EXTRACTION
    Extraction.perform_extraction()
    Extraction.print_extraction()

    # CHECK RESULTS
    for ticket in Ticket.tickets_played:
        result = ticket.check_ticket()  # type TUPLE (str,[int])
        if ticket.check_ticket():   # non-empty tuple
            i = 0
            while True:
                # New Object of type Win
                win = Win(result[i], result[i+1])

                # .... result/win must be an OBJECTS (class Win) but doesn't work
                ticket.result_city.append(win.city_name)
                ticket.result_numbers.append(win.extracted_numbers)

                # Calculation of gross and net winnings for each wheel played
                win.calculate_gross_net_win(ticket)

                # .... result/win must be an OBJECT (class Win) but doesn't work
                # Adding the value of winnings to the attributes of the ticket object
                ticket.result_gross_amount.append(win.gross_amount)
                ticket.result_net_amount.append(win.net_amount)
                i += 2

                # In the following case, there are no more winning wheels
                if i >= len(result):
                    break

    # PRINT RESULTS
    for ticket in Ticket.tickets_played:
        ticket.print_ticket()


if __name__ == "__main__":
    main()
