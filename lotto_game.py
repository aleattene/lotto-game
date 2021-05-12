import argparse
from lotto_game.bet_type import BetType
from lotto_game.city import City
from lotto_game.number_utils import NumberUtils
from lotto_game.ticket import Ticket
from lotto_game.extraction import Extraction
from lotto_game.win import Win


def main():

    # Acquisition of the number of tickets to generate directly from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_ticket", help="Number of tickets", type=int)
    args = parser.parse_args()

    # Check insertion of the correct value
    range_tickets = ()
    argument = False
    if args.num_ticket is not None:  # an argument has been inserted
        if 1 <= args.num_ticket <= 10:
            range_tickets = (1, args.num_ticket)  # type TUPLE (1, max 10)
            argument = True
        else:
            # Error message
            print("\nWarning, you have entered from the command line a numeric value not allowed.")
            argument = False

    if not argument:  # no argument has been added
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
        # New Object of type City (int,str)
        city = City(city_key_name[0], city_key_name[1])

        # New Object of type BetType (int,str)
        bet_type = BetType(bet_key_name[0], bet_key_name[1])

        # Generation of the numbers to play for each ticket
        generated_numbers = NumberUtils.generate_numbers(amount_numbers)  # type LIST [int]

        # New Object of type Ticket (int,obj,float,obj,[int])
        ticket = Ticket(i, bet_type, amount_money, city, generated_numbers)

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
                # New Object of type Win (str,[int])
                win = Win(result[i], result[i+1])

                # Addition of win object to the attribute ticket.winning (list of objects)
                ticket.winning_wheels.append(win)

                # Calculation of gross and net winnings for each wheel played
                win.calculate_gross_net_win(ticket)

                i += 2
                # In the following case, there are no more winning wheels
                if i >= len(result):
                    break

        # Calculation of total gross and net win for each ticket
        ticket.calculate_total_gross_net_amount()

    # PRINT RESULTS
    for ticket in Ticket.tickets_played:
        ticket.print_ticket()


if __name__ == "__main__":
    main()
