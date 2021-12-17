import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import matplotlib.pyplot as plt
import matplotlib as mpl

import api_key  # imports API Keys

class Stock():

    def __init__(self, ticker: str):
        self.ticker = ticker
        # grab stock data

        # time_start = today minus 84 minus weekends to get 85 rows. 85 = 70 + 14 + 1
        time_start = (date.today() - pd.tseries.offsets.BusinessDay(200)).strftime("%Y-%m-%d")
        time_end = date.today().strftime("%Y-%m-%d")

        self.stock_data = yf.Ticker(self.ticker).history(start=time_start, end=time_end).drop(columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"], errors="ignore")


    def moving_average_analysis(self):
        self.moving_average_table = self.stock_data.copy()
        self.moving_average_table["26 Day"] = self.stock_data["Close"].ewm(span=26).mean()
        self.moving_average_table["70 Day"] = self.stock_data["Close"].rolling(window=70).mean()
        # At this point we only really care about the most recent 14 days, since rolling is done
        self.moving_average_table["diff"] = abs(self.moving_average_table["26 Day"] - self.moving_average_table["70 Day"])
        # TEST
        self.moving_average_table["Signal"] = 0
        self.moving_average_table["Signal"] = np.where(self.moving_average_table["26 Day"] > self.moving_average_table["70 Day"], 1, 0)
        self.moving_average_table["Position"] = self.moving_average_table["Signal"].diff()

        results = self.moving_average_table.loc[self.moving_average_table["diff"] < 0.2]

        # returns timestamps
        print(self.moving_average_table)
        return results.index.tolist()

    def display(self):
        plt.plot(self.moving_average_table["Close"], label="Price")
        plt.plot(self.moving_average_table["26 Day"], label="26 Day EMA")
        plt.plot(self.moving_average_table["70 Day"], label="70 Day SMA")

        plt.plot(self.moving_average_table[self.moving_average_table["Position"] == 1].index,
                 self.moving_average_table["26 Day"][self.moving_average_table["Position"] == 1],
                 "^", color="g", label='buy')

        plt.plot(self.moving_average_table[self.moving_average_table["Position"] == -1].index,
                 self.moving_average_table["26 Day"][self.moving_average_table["Position"] == -1],
                 "v", color="r", label='sell')

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.show()




    def buy_stock(self):
        # import alpaca_trade_api as tradeapi
        # api = tradeapi.REST('AKR09R521SWTPGN5YAUI',
        #                 'ijRiw9bHL1HuLpD0k9uxfW020DVJhayK5rpToN5v')
        # order = api.submit_order(
        #     symbol='ALPACA',
        #     qty=15,
        #     type='limit',
        #     side='buy',
        #     limit_price=25.34,
        #     time_in_force='day',
        # )
        pass

# Debug
s = Stock("MRK")
timestamps = s.moving_average_analysis()
print(timestamps)

# while True:
#     inputed = input("See graph?: ").upper()[0]
#     if inputed == "Y":
s.display()
#     else:
#         break