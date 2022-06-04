import yfinance as yf
from models.stock import Stock
from models.strategy import Strategy
import alpaca_trade_api as tradeapi
from keys import api_key, secret_key


class TradingBot:
    def __init__(self, tickers, captial):
        self._watchlist = []
        self._current_trades = []
        self._capital = captial
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

    def add_trade(self, trade):
        self._current_trades.append(trade)

    @property
    def captial(self):
        return self._captial

    @captial.setter
    def capital(self, captial):
        self._captial = captial

    def run_strategy(self):
        self.strategy.calc_technicals(self._watchlist)

        for stock in self._watchlist:
            if self.strategy.isBullish(stock):
                print(f"Bullish trade for: {stock._ticker_symbol}")
                # buy calls here, make sure you're not already in a trade with the same ticker
            elif self.strategy.isBearish(stock):
                print(f"Bearish trade for: {stock._ticker_symbol}")
                # buy puts here, make sure you're not already in a trade with the same ticker
            else:
                print(f"Not trading {stock._ticker_symbol}")

    def enter_calls(self, stock: Stock):
        BASE_URL = "https://paper-api.alpaca.markets"
        api = tradeapi.REST(key_id=self.api_key, secret_key=self.secret_key, 
                    base_url=BASE_URL, api_version='v2')
        api.submit_order(symbol=stock.ticker_symbol, qty=1, side='buy', type='market', time_in_force='day')


    def enter_puts(self, stock: Stock):
        BASE_URL = "https://paper-api.alpaca.markets"
        api = tradeapi.REST(key_id=self.api_key, secret_key=self.secret_key, 
                    base_url=BASE_URL, api_version='v2')
        api.submit_order(symbol=stock.ticker_symbol, qty=1, side='sell', type='market', time_in_force='day')

    def exit_position():
        pass
    
    def monitor_trades():
        pass
    