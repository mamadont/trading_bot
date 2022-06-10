from models.trading_bot import TradingBot
import yfinance as yf


tickers = ["SPY", "QQQ"]
trading_bot = TradingBot(tickers)
trading_bot.run_strategy()
