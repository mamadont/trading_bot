from models.stock import Stock
import pandas_ta as ta

class Strategy:
    def __init__(self):
        pass

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

    def calc_technicals(self, watchlist):
        for stock in watchlist:
            self.calc_macd(stock)
            self.calc_rsi(stock)
            self.calc_vwap(stock)
            self.calc_ema(stock)

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