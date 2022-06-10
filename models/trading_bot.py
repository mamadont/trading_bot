import yfinance as yf
from models.stock import Stock
from models.strategy import Strategy
from keys import api_key, secret_key
from models.trade import Trade
import time

class TradingBot:
    def __init__(self, tickers):
        self._watchlist = []
        self._current_trades = []
        self.strategy = Strategy()
        self.api_key = api_key
        self.secret_key = secret_key
    
        for ticker in tickers:
            df = yf.download(ticker, period="5d", interval= "5m")
            stock = Stock(ticker, df)
            self._watchlist.append(stock)
        
    @property
    def watchlist(self):
        return self._watchlist

    @watchlist.setter
    def watchlist(self, watchlist):
        self._watchlist = watchlist

    @property
    def current_trades(self):
        return self._current_trades

    def update_prices(self):
        for stock in self._watchlist:
            stock._df = yf.download(
                stock._ticker_symbol, 
                period="5d", 
                interval= "5m")

    def run_strategy(self):
        self.update_prices()
        self.strategy.calc_technicals(self._watchlist)

        for stock in self._watchlist:
            # check if stock merits calls
            if self.strategy.isBullish(stock):
                print(f"Bullish trade for: {stock._ticker_symbol}")

                if self.already_in_trade(stock._ticker_symbol):
                    print("But you are already in a call for this ticker")
                else:
                    self.enter_calls(stock)

            # check if stock merits puts
            elif self.strategy.isBearish(stock):
                print(f"Bearish trade for: {stock._ticker_symbol}")

                if self.already_in_trade(stock._ticker_symbol):
                    print("But you are already in a put for this ticker")
                else:
                    self.enter_puts(stock)
            else:
                print(f"Not trading {stock._ticker_symbol}")

            self.monitor_trades(self._watchlist)

    def enter_calls(self, stock: Stock):
        stock._current_trade = Trade("call", stock._df["Close"][-1], time.localtime())
        print(f"Entry price for call: ", stock._df["Close"][-1])

    def enter_puts(self, stock: Stock):
        stock._current_trade = Trade("put", stock._df["Close"][-1], time.localtime())
        print(f"Entry price for put: ", stock._df["Close"][-1])

    def already_in_trade(self, ticker_symbol):
        for trade in self.current_trades:
            if trade.ticker_symbol == ticker_symbol:
                return True
        return False

    def monitor_trades(self, stocks):            
        for stock in stocks:
            self.take_profits(
                stock._current_trade._type, 
                stock._current_trade._entry_price, 
                stock._df["Close"][-1])
            self.cut_losses(
                stock._current_trade._type, 
                stock._current_trade._entry_price, 
                stock._df["Close"][-1])

    def take_profits(self, type, entry_price, current_price):
        if type == "calls":
            profit = (entry_price * 100) / current_price
            if profit > 0.05:
                print("Taking profits at: ", current_price)
        
        elif type == "puts":
            profit = (current_price * 100) / entry_price
            if profit > 0.05:
                print("Taking profits at: ", current_price)

    def cut_losses(self, type, entry_price, current_price):
        if type == "calls":
            profit = (entry_price * 100) / current_price
            if profit < 0.05:
                print("Taking profits at: ", current_price)
        
        elif type == "puts":
            profit = (current_price * 100) / entry_price
            if profit < 0.05:
                print("Taking profits at: ", current_price)

    def run(self):
        # while the time is not 4 o'clock run the strategy
        pass