from modules.misc_functions import get_input, load_tickers
from modules.pretty_print import Print_Log
from modules.stock_analysis import
from datetime import date, timedelta

# Initialize Logging
PL = Print_Log(0)
PL.print("Started Logging!", 1)

# Load Tickers
load_tickers()

# Main thing
# 200 times per minute - multithreaded
from alpaca_trade_api.rest import REST, TimeFrame
api = REST()

today = date.today()
time_start = (today - timedelta(days=71)).strftime("%Y-%m-%d")
time_end = today.strftime("%Y-%m-%d")

print(api.get_bars("AAPL", TimeFrame.Day, time_start, time_end).df)


# Grab historical data for past 70 days
# calculate moviving averages

#
