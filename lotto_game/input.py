class Input:

    # Acquisition of the number of tickets
    @staticmethod
    def acquire_number_tickets():
        # Minimum and maximum number of tickets that can be played
        MIN_TICKETS = 1
        MAX_TICKETS = 5
        while True:
            try:
                num_tickets = int(input("How many tickets do you want to play (between 1 and 5, 0 to quit)? "))  # type int
                if num_tickets == 0:
                    print("Thank you. The simulation of the lotto game is over.")
                    quit()
                elif MIN_TICKETS <= num_tickets <= MAX_TICKETS:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again.")
        return num_tickets
