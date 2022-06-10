class Trade:
    def __init__(self, type, entry_price, time_of_entry):
        self._type = type
        self._entry_price = entry_price
        self._time_of_entry = time_of_entry
        self._exit_price = 0
        self._profit = 0

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
    def exit_price(self):
        return self.exit_price

    @exit_price.setter
    def property(self, exit_price):
        self.exit_price = exit_price

    # @property
    # def time_of_entry(self):
    #     return self.time_of_entry

    # @time_of_entry.setter
    # def property(self, time_of_entry):
    #     self.time_of_entry = time_of_entry

    # @property
    # def profit(self):
    #     return self._profit

    # @profit.setter
    # def profit(self, profit):
    #     self._profit = profit
