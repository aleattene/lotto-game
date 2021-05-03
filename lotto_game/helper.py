from random import randint


# This function returns an ordered list of integers (between MIN_NUMBER and MAX_NUMBERS)
def generate_numbers(n):
    MIN_NUMBER = 1
    MAX_NUMBER = 90
    numbers = []
    while n > 0:
        number = randint(MIN_NUMBER, MAX_NUMBER + 1)
        if number not in numbers:
            numbers.append(number)
            n -= 1
    numbers.sort()
    return numbers


# This function prints all of the played tickets
def print_tickets(tickets):
    for k in sorted(tickets):
        print("Ticket n. {}".format(k))
        print("Numbers : {}".format(tickets[k][0]))
        print("Wheel: {}".format(tickets[k][1]))
        print("Bet Type : {}".format(tickets[k][2]))


