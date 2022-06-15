from models.trading_bot import TradingBot

tickers = ["SPY", "QQQ"]
trading_bot = TradingBot(tickers)
trading_bot.run()
