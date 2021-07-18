class City:

    # Dictionary containing the cities (aka "wheel") that can be chosen for each ticket
    all_cities = {1: "Bari", 2: "Cagliari", 3: "Firenze", 4: "Genova", 5: "Milano",
                  6: "Napoli", 7: "Palermo", 8: "Roma", 9: "Torino", 10: "Venezia", 11: "Tutte"}

    def __init__(self, id_city, name):
        self.id_city = id_city      # type INT
        self.name = name            # type STR

    def __str__(self):
        return (f"""
        Id City: {self.id_city} 
        City: {self.name}  
        """)

    # This static method acquires from the user the city to play for each ticket
    @staticmethod
    def acquire_city(num_ticket):
        print()
        for k in City.all_cities:   # type(k) = INT
            print("       {}: {}".format(k, City.all_cities[k]))
        while True:
            try:
                city_key = int(input("\nEnter the city for the ticket n. "
                                     "{} (between 1 and {}): ".format(num_ticket, len(City.all_cities))))  # type INT
                if city_key in City.all_cities:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect Entry. Try Again")
        city_name = City.all_cities[city_key]   # type STR
        return city_key, city_name  # type TUPLE (int,str)
