from random import randint


class Helper:

    # This method returns an ordered list of integers (between min_number and max_number)
    @staticmethod
    def generate_numbers(num_tickets, min_number, max_number):
        numbers = []
        while num_tickets > 0:
            number = randint(min_number, max_number + 1)
            if number not in numbers:
                numbers.append(number)
                num_tickets -= 1
        numbers.sort()
        return numbers

    # Storage of the played tickets
    @staticmethod
    def storage_ticket(tickets_played, ticket):
        tickets_played[ticket.num_ticket] = (ticket.numbers, ticket.city, ticket.bet)









