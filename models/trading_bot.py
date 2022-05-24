import yfinance as yf
from models.stock import Stock

class TradingBot:
    def __init__(self, tickers, captial):
        self._tickers = tickers
        self._watchlist = []
        self._current_trades = []
        self._capital = captial
        
        for ticker in tickers:
            df = yf.download(ticker, period = "1d", interval = "5m")
            self._watchlist.append(Stock(ticker, df))

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
            df = yf.download(stock._ticker_symbol, period = "1d", interval = "5m")
            stock._price_action = df

    def calculate_rsi(self, window=14, adjust=False):
        for stock in self._watchlist:
            delta = stock._price_action['Close'].diff(1).dropna()
            loss = delta.copy()
            gains = delta.copy()

            gains[gains < 0] = 0
            loss[loss > 0] = 0

            gain_ewm = gains.ewm(com=window - 1, adjust=adjust).mean()
            loss_ewm = abs(loss.ewm(com=window - 1, adjust=adjust).mean())

            RS = gain_ewm / loss_ewm
            RSI = 100 - 100 / (1 + RS)

            stock._rsi = RSI.tail(1)[-1]

