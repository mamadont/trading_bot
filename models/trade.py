from importlib.metadata import entry_points
from time import time
from urllib3 import Retry


class Trade:
    def __init__(self, ticker_symbol, type, entry_price, time_of_entry):
        self._ticker_symbol = ticker_symbol
        self._type = type
        self._entry_price = entry_price
        self._time_of_entry = time_of_entry
        self._exit_price = 0
        self._profit = 0

    @property
    def ticker_symbol(self):
        return self.ticker_symbol
    
    @ticker_symbol.setter
    def ticker_symbol(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
    
    @property
    def type(self):
        return self.type
    
    @type.setter
    def tpye(self, type):
        self.type = type

    @property
    def entry_price(self):
        return self.entry_price
    
    @entry_price.setter
    def entry_price(self, entry_price):
        self.entry_price = entry_price

    @property
    def time_of_entry(self):
        return self.time_of_entry
    
    @time_of_entry.setter
    def property(self, time_of_entry):
        self.time_of_entry = time_of_entry

    @property
    def exit_price(self):
        return self.exit_price
    
    @exit_price.setter
    def property(self, exit_price):
        self.exit_price = exit_price


    

    