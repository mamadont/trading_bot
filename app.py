from models.trading_bot import TradingBot
import yfinance as yf
from models.stock import Stock

tickers = ["SPY", "AAPL", "MSFT", "NVDA"]
trading_bot = TradingBot(tickers, 1000)

df = yf.download("SPY", period="1d", interval="5m")
stock = Stock("SPY", df)

trading_bot.run_strategy()
 