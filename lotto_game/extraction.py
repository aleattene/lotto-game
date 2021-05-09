from lotto_game.city import City
from lotto_game.number_utils import NumberUtils
from datetime import datetime


class Extraction:

    # Dictionary that will contain the extraction {key -> city : value -> [numbers]}
    extraction = {}

    # This static method performs the extraction (generating randomly 5 numbers for each wheel/city)
    @staticmethod
    def perform_extraction():
        # Max amount of numbers that can be extracted for each wheel/city
        AMOUNT_NUMBERS_EXTRACTION = 5
        for k in sorted(City.all_cities):
            if City.all_cities[k] != "Tutte":
                extracted_numbers = NumberUtils.generate_numbers(AMOUNT_NUMBERS_EXTRACTION)  # type LIST
                # Dictionary Update
                Extraction.extraction[City.all_cities[k]] = extracted_numbers

    # This static method prints the table of the extraction
    @staticmethod
    def print_extraction():
        # Table header
        print("\n╔{:^43}╗".format("═" * 43))  # ASCII code (201,205,187)
        print("║{:^43}║".format("ESTRAZIONE del "
                                "{}".format(datetime.today().strftime('%d/%m/%Y'))))  # ASCII code (186)
        print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,205,185)
        # Table body
        for city in sorted(Extraction.extraction):
            print("║   {:13}".format(city), end="")  # ASCII code (186)
            for value in Extraction.extraction[city]:
                print("{:4}".format(value), end=" ")
            print("  ║")  # ASCII code (186)
        # Table footer
        print("╚{:^43}╝".format("═" * 43))  # ASCII code (200,205,188)
