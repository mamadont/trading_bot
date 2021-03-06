from models.trade import Trade
class Stock:
    def __init__(self, ticker_symbol, df):
        self._ticker_symbol = ticker_symbol
        self._rsi = 0
        self._vwap = 0
        self._ema = 0
        self._macd = 0
        self._macd_slow = 0
        self._df = df
        self._current_trade = Trade("n/a", 0, 0)
    
    @property
    def ticker_symbol(self):
        return self._ticker_symbol

    @ticker_symbol.setter
    def rsi(self, ticker_symbol):
        self._ticker_symbol = ticker_symbol

    @property
    def rsi(self):
        return self._rsi

    @rsi.setter
    def rsi(self, rsi):
        self._rsi = rsi

    @property
    def vwap(self):
        return self._vwap
        
    @vwap.setter
    def vwap(self, vwap):
        self._vwap = vwap

    @property
    def ema(self):
        return self._ema
        
    @ema.setter
    def ema(self, ema):
        self._ema = ema

    @property
    def macd(self):
        return self._macd
        
    @macd.setter
    def macd(self, macd):
        self._macd = macd

    @property
    def macd_slow(self):
        return self._macd_slow
        
    @macd_slow.setter
    def macd_slow(self, macd_slow):
        self._macd_slow = macd_slow
    
    @property
    def price_action(self):
        return self._price_action
    
    @price_action.setter
    def price_action(self, price_action):
        self._price_action = price_action

    @property
    def current_trade(self):
        return self._current_trade

    @current_trade.setter
    def current_trade(self, trade):
        self._current_trade = trade