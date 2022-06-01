from models.trading_bot import TradingBot

tickers = ["SPY", "QQQ"]
trading_bot = TradingBot(tickers, 1000)
trading_bot.run_strategy()
 