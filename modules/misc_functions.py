import urllib.request as request
from contextlib import closing
import re
import logging

log = logging.getLogger(__name__)

log.debug("Doing something!")

def load_tickers():
    log.info("Downloading ticker validation...")
    valid_tickers = []
    log.debug("Requesting from NASDAQ")
    with closing(request.urlopen("ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt")) as r:
        for line in r:
            line = line.decode()
            newline = (re.search('[^|]*', line).group(),)
            valid_tickers += (newline)
    log.debug("Done with NASDAQ")
    log.debug("Requesting from Other Listed")
    with closing(request.urlopen("ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt")) as r:
        for line in r:
            line = line.decode()
            newline = (re.search('[^|]*', line).group(),)
            valid_tickers += (newline)
    log.debug("Done with Other Listed")
    log.info("Finished downloading ticker validation!")
    return valid_tickers

def get_input(input_message: str, type="str"):
    log.debug(f"Getting input about {input_message}")
    # Type can be Bool, str, int
    input_message = str(input_message)
    type = str(type).lower()
    if type == "bool":
        possible_answers = " (Y/yes/N/no)"
    elif type != "str" and type != "int":
        raise Exception("Type must be bool, str, or int")
    else:
        possible_answers = ""

    while True:
        answer = input(f"{input_message}{possible_answers}: ")

        # answer handling
        if type == "bool":
            try:
                answer = (str(answer).upper())[0]
                if answer == "Y":
                    return True
                elif answer == "N":
                    return False
            except ValueError:
                print("Input error! Please try again.\n")

        if type == "str":
            try:
                return str(answer)
            except ValueError:
                print("Input error! Please try again.\n")

        if type == "int":
            try:
                return int(answer)
            except ValueError:
                print("Input error! Please enter numerical values only.\n")
