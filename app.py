from models.trading_bot import TradingBot
import yfinance as yf
from models.stock import Stock

tickers = ["SPY", "MSFT", "AAPL"]
trading_bot = TradingBot(tickers, 1000)
trading_bot.run_strategy()
 