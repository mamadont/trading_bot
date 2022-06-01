import yfinance as yf
from models.stock import Stock
import pandas_ta as ta

class TradingBot:
    def __init__(self, tickers, captial):
        self._watchlist = []
        self._current_trades = []
        self._capital = captial

        for ticker in tickers:
            df = yf.download(ticker, period="1d", interval="5m")
            self._watchlist.append(Stock(ticker, df))
        
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

    def calc_rsi(self, stock: Stock):
        rsi = ta.rsi(stock._df["Close"])
        stock._rsi = rsi.tail()[-1]
     
    def calc_vwap(self, stock: Stock):
        vwap = ta.vwap(high= stock._df["High"], low= stock._df["Low"], close= stock._df["Close"], volume= stock._df["Volume"])
        stock._vwap = vwap.tail()[-1]

    def calc_ema(self, stock: Stock):
        ema = ta.ema(stock._df["Close"], length= 5)
        stock._ema = ema.tail()[-1]
    
    def calc_macd(self, stock: Stock):
        macd = ta.macd(stock._df["Close"])
        stock._macd = macd["MACD_12_26_9"].tail()[-1]
        stock._macd_slow = macd["MACDs_12_26_9"].tail()[-1]

    def calc_technicals(self):
        for stock in self._watchlist:
            self.calc_macd(stock)
            self.calc_rsi(stock)
            self.calc_vwap(stock)
            self.calc_ema(stock)

    def run_strategy(self):
        self.calc_technicals()

        for stock in self._watchlist:
            if self.isBullish(stock):
                print(f"Bullish trade for: {stock._ticker_symbol}")
            elif self.isBearish(stock):
                print(f"Bearish trade for: {stock._ticker_symbol}")
            else:
                print(f"Not trading {stock._ticker_symbol}")
    
    def isBullish(self, stock: Stock):
        if (stock._macd > stock._macd_slow):
            if (stock._rsi > 50):
                if (stock._ema > stock._vwap):
                    return True

    def isBearish(self, stock: Stock):
        if (stock._macd < stock._macd_slow):
            if (stock._rsi < 50):
                if (stock._ema < stock._vwap):
                    return True

    def enter_calls():
        pass

    def enter_puts():
        pass
