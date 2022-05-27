class Stock:
    def __init__(self, ticker_symbol):
        self._ticker_symbol = ticker_symbol
        self._rsi = 0
        self._vwap = 0
        self._ema = 0
        self._macd = 0
        # self._price_action = df
    
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
    def price_action(self):
        return self._price_action
    
    @price_action.setter
    def price_action(self, price_action):
        self._price_action = price_action