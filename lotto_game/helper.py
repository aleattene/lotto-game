from random import randint


class Helper:

    # This method returns an ordered list of integers (between min_number and max_number)
    @staticmethod
    def generate_numbers(amount_numbers, min_number, max_number):
        numbers = []
        while amount_numbers > 0:
            number = randint(min_number, max_number + 1)
            if number not in numbers:
                numbers.append(number)
                amount_numbers -= 1
        numbers.sort()
        return numbers

    # Storage of the played tickets
    @staticmethod
    def storage_ticket(tickets_played, ticket):
        tickets_played[ticket.id_ticket] = (ticket.numbers, ticket.city, ticket.bet_type)









