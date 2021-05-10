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
        for k in sorted(City.all_cities):   # type(k) = INT
            if City.all_cities[k] != "Tutte":
                extracted_numbers = NumberUtils.generate_numbers(AMOUNT_NUMBERS_EXTRACTION)  # type LIST
                # Dictionary Updating
                Extraction.extraction[City.all_cities[k]] = extracted_numbers

    # This static method prints the table of the extraction
    @staticmethod
    def print_extraction():
        # Table HEADER
        print("\n╔{:^43}╗".format("═" * 43))  # ASCII code (201,187,205)
        print("║{:^43}║".format("ESTRAZIONE del "  # ASCII code (186)
                                "{}".format(datetime.today().strftime('%d/%m/%Y'))))  # date format: DD/MM/YYYY
        print("╠{:^43}╣".format("═" * 43))  # ASCII code (204,185,205)
        # Table BODY
        for city in sorted(Extraction.extraction):
            print("║   {:13}".format(city), end="")  # ASCII code (186)
            for value in Extraction.extraction[city]:
                print("{:4}".format(value), end=" ")
            print("  ║")  # ASCII code (186)
        # Table FOOTER
        print("╚{:^43}╝".format("═" * 43))  # ASCII code (200,188,205)
