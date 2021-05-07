from lotto_game.city import City
from lotto_game.numbers import Numbers
from datetime import datetime


class Extraction:

    extraction = {}

    @staticmethod
    def perform_extraction():
        AMOUNT_NUMBERS_EXTRACTION = 5
        for k in sorted(City.all_cities):
            extracted_numbers = Numbers.generate_numbers(AMOUNT_NUMBERS_EXTRACTION)
            Extraction.extraction[City.all_cities[k]] = extracted_numbers

    @staticmethod
    def print_extraction():
        # TABLE HEADER
        print("╔{:^43}╗".format("═" * 43))  # ASCII code (201,205,187)
        print("║{:^43}║".format("ESTRAZIONE del "
                                "{}".format(datetime.today().strftime('%d/%m/%Y'))))  # ASCII code (186,186)
        print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
        # TABLE BODY
        for city in sorted(Extraction.extraction):
            print("║   {:13}".format(city), end="")  # ASCII code (186)
            for value in Extraction.extraction[city]:
                print("{:4}".format(value), end=" ")
            print("  ║")  # ASCII code (186)
        # TABLE FOOTER
        print("╚{:^43}╝".format("═" * 43))  # ASCII code (200,205,188)
