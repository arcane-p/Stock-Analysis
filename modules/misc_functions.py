import urllib.request as request
from contextlib import closing
import re
from pretty_print import PL


def load_tickers():
    PL.print("Downloading ticker validation...", 1)
    valid_tickers = []
    PL.print("Requesting from NASDAQ", 0)
    with closing(request.urlopen("ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt")) as r:
        for line in r:
            line = line.decode()
            newline = (re.search('[^|]*', line).group(),)
            valid_tickers += (newline)
    PL.print("Done with NASDAQ", 0)
    PL.print("Requesting from Other Listed", 0)
    with closing(request.urlopen("ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt")) as r:
        for line in r:
            line = line.decode()
            newline = (re.search('[^|]*', line).group(),)
            valid_tickers += (newline)
    PL.print("Done with Other Listed", 0)
    PL.print("Finished downloading ticker validation!", 1)
    return valid_tickers


def get_input(input_message: str, type="str"):
    PL.print(f"Getting input about {input_message}", 0)
    # Type can be Bool, str, int
    input_message = str(input_message)
    type = str(type).lower()
    if type == "bool":
        possible_answers = " (Y/yes/N/no)"
    elif type != "str" and type != "int":
        PL.print("get_input type is incorrect!", 4)
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
                PL.print("Input error! Please try again.", 3)
                print()  # newline

        if type == "str":
            try:
                return str(answer)
            except ValueError:
                PL.print("Input error! Please try again.", 3)
                print()  # newline

        if type == "int":
            try:
                return int(answer)
            except ValueError:
                PL.print("Input error! Please enter numerical values only.", 3)
                print()  # newline
