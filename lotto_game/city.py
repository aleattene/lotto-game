class City:

    # Dictionary containing the cities(aka "wheel") that can be chosen for the bet
    all_cities = {1: "Bari", 2: "Cagliari", 3: "Firenze", 4: "Genova", 5: "Milano",
                  6: "Napoli", 7: "Palermo", 8: "Roma", 9: "Torino", 10: "Venezia", 11: "Tutte"}

    def __init__(self, id_city, name):
        self.id_city = id_city
        self.name = name

    # # This static method acquires from the user the city to play
    @staticmethod
    def acquire_city(num_ticket):
        print()
        for k in City.all_cities:
            print("       {}: {}".format(k, City.all_cities[k]))
        while True:
            try:
                city_key = int(input("\nEnter the city for the ticket n. "
                                     "{} (between 1 and {}): ".format(num_ticket, len(City.all_cities))))  # type int
                if city_key in City.all_cities:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        city_name = City.all_cities[city_key]
        return city_key, city_name
