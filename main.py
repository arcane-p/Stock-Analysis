from modules.misc_functions import get_input, load_tickers
from modules.pretty_print import PL
from modules.stock_analysis import Stock
# from modules.stock_analysis import

# Initialize Logging
PL = PL(0)
PL.print("Started Logging!", 1)

# Load Tickers
tickerlist = load_tickers()

# Main thing

# 200 times per minute - multithreaded
for ticker in tickerlist:
    s = Stock(ticker, 84)
    timestamps = s.moving_average_cross_analysis(26, 70, ["EMA", "SMA"])
    print(ticker, ":", timestamps)

# Grab historical data for past 70 days
# calculate moviving averages

#
