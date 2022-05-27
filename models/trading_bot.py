import yfinance as yf
from models.stock import Stock
import pandas_ta as ta
import pandas as pd


class TradingBot:
    def __init__(self, tickers, captial):
        self._tickers = tickers
        self._watchlist = []
        self._current_trades = []
        self._capital = captial

        print("Trading bot initialized...")

    @property
    def tickers(self):
        return self.tickers

    @tickers.setter
    def tickers(self, tickers):
        self.tickers = tickers

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
        return self.captial

    @captial.setter
    def watchlist(self, captial):
        self.captial = captial

    def download_data(self):
        for stock in self._watchlist:
            df = yf.download(stock._ticker_symbol, period="1d", interval="5m")
            stock._price_action = df

    def run_strategy(self):
        Strategy = ta.Strategy(
            name="My Strategy",
            description="Uses MACD, RSI, VWAP, and EMA",
            ta=[
                {"kind": "ema", "length": 9},
                {"kind": "vwap", "length": 21},
                {"kind": "rsi"},
                {"kind": "macd", "fast": 8, "slow": 21,
                 "col_names": ("MACD", "MACD_H", "MACD_S")}
            ]
        )

        df = pd.DataFrame()

        for stock in self._tickers:            
            df = df.ta.ticker(stock, period="1d", interval="30m")
            df.ta.strategy(Strategy)
            
        print('Data downloaded...')
