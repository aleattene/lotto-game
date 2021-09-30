
from lotto_game.lotto_game import LottoGame


def main():

    # Play Tickets
    LottoGame.acquire_tickets()
    # Do Extraction
    LottoGame.do_extraction()
    # Check Results
    LottoGame.check_results()


if __name__ == "__main__":
    main()
