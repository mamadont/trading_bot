from models.trading_bot import TradingBot

tickers = ["MSFT", "AAPL", "NVDA", "AMD", "DAL"]
trading_bot = TradingBot(tickers, 1000)
trading_bot.calculate_rsi()
print(trading_bot._watchlist[0]._rsi)