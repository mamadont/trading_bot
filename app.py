from models.trading_bot import TradingBot
from models.stock import Stock

tickers = ["MSFT", "AAPL", "NVDA", "AMD", "DAL"]
trading_bot = TradingBot(tickers, 1000)
