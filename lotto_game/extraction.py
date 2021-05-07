from lotto_game.city import City
from lotto_game.numbers import Numbers


class Extraction:

    extraction = {}

    @staticmethod
    def perform_extraction():
        AMOUNT_NUMBERS_EXTRACTION = 5
        for k in sorted(City.all_cities):
            extracted_numbers = Numbers.generate_numbers(AMOUNT_NUMBERS_EXTRACTION)
            Extraction.extraction[City.all_cities[k]] = extracted_numbers


