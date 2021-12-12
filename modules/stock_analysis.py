import pandas as pd

class Stock():

    def __init__(self, ticker):
        self.ticker = ticker
        # grab stock data
        self.stock_data = None

    def MovingAverageAnalysis():
        pass

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