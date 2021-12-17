import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt

import api_key  # imports API Keys


class Stock():

    def __init__(self, ticker: str, window: int = 84):
        self.ticker = ticker

        # Load stock data
        time_start = (date.today() - pd.tseries.offsets.BusinessDay(window)).strftime("%Y-%m-%d")
        time_end = date.today().strftime("%Y-%m-%d")
        self.stock_data = yf.Ticker(self.ticker).history(start=time_start, end=time_end).drop(columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"], errors="ignore")
        self.stock_data.dropna(axis=0, inplace=True)  # remove any null rows 

    def moving_average_cross_analysis(self, short_window: int = 26, long_window: int = 70, moving_avg: list = ["EMA", "SMA"]):
        """Generate signals and return timeframe with position.

        Uses a variable short & long window, with interchangable moving_average styles.

        Args:
            short_window (int, optional): Window of days to use for short-term MA. Defaults to 26.
            long_window (int, optional): Window of days to use for long-term MA. Defaults to 70.
            moving_avg (list, optional): Defines type of moving average for short and long window respectively. Defaults to ["EMA", "SMA"].

        Returns:
            [type]: [description]
        """
        self.df_MA = self.stock_data.copy()
        if len(moving_avg) > 2 or ("EMA" not in moving_avg and "SMA" not in moving_avg):
            raise Exception("moving_avg invalid. Must be list containing either SMA or EMA respectively.")

        # Begin analysis
        if moving_avg[0] == "EMA":
            self.df_MA["short_window_col"] = self.stock_data["Close"].ewm(span=short_window, adjust=False).mean()
        elif moving_avg[0] == "SMA":
            self.df_MA["short_window_col"] = self.stock_data["Close"].rolling(span=short_window, min_periods=1).mean()

        if moving_avg[1] == "SMA":
            self.df_MA["long_window_col"] = self.stock_data["Close"].rolling(window=long_window, min_periods=1).mean()
        elif moving_avg[1] == "EMA":
            self.df_MA["long_window_col"] = self.stock_data["Close"].emw(window=long_window, adjust=False).mean()

        # Generates Signals and derives trading positions
        self.df_MA["Signal"] = 0
        self.df_MA["Signal"] = np.where(self.df_MA["short_window_col"] > self.df_MA["long_window_col"], 1, 0)
        self.df_MA["Position"] = self.df_MA["Signal"].diff()

        results = self.df_MA.loc[self.df_MA["Position"] != 0]
        # final_dict = {}
        # for timestamp in results.index.tolist():
        #     final_dict[timestamp] = results.at[timestamp, "Position"]

        final_dict = {timestamp: results.at[timestamp, "Position"] for timestamp in results.index.tolist() if ~np.isnan(results.at[timestamp, "Position"])}

        return final_dict

    def display(self, analysis_type: str):
        if analysis_type == "MA":
            plt.plot(self.df_MA["Close"], label="Price")
            plt.plot(self.df_MA["short_window_col"], label="short_window_col")
            plt.plot(self.df_MA["long_window_col"], label="long_window_col")

            plt.plot(self.df_MA[self.df_MA["Position"] == 1].index,
                     self.df_MA["short_window_col"][self.df_MA["Position"] == 1],
                     "^", color="g", label='buy')

            plt.plot(self.df_MA[self.df_MA["Position"] == -1].index,
                     self.df_MA["short_window_col"][self.df_MA["Position"] == -1],
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
# s = Stock("MRK", 84)
# timestamps = s.moving_average_cross_analysis(26, 70, ["EMA", "SMA"])
# print(timestamps)
# s.display("MA")
