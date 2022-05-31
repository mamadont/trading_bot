from models.trading_bot import TradingBot
import yfinance as yf
from models.stock import Stock




tickers = ["MSFT", "NVDA"]
trading_bot = TradingBot(tickers, 1000)

df = yf.download("SPY", period="1d", interval="5m")
stock = Stock("MSFT", df)

trading_bot.calc_vwap(stock)
 