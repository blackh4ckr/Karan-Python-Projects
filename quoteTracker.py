import yfinance as yf
import schedule
import time

# Define the list of stock symbols to track
symbols = ['AAPL', 'GOOG', 'TSLA']

# Define the interval between updates (in seconds)
update_interval = 60

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')
    return data['Close'][0]

def update_stock_prices():
    for symbol in symbols:
        current_price = get_stock_data(symbol)
        if current_price > prices[symbol]:
            print(f"{symbol} has moved up from {prices[symbol]:.2f} to {current_price:.2f}")
        elif current_price < prices[symbol]:
            print(f"{symbol} has moved down from {prices[symbol]:.2f} to {current_price:.2f}")
        prices[symbol] = current_price

# Initialize the dictionary of prices
prices = {}
for symbol in symbols:
    prices[symbol] = get_stock_data(symbol)

# Schedule periodic updates
schedule.every(update_interval).seconds.do(update_stock_prices)

while True:
    # Check if there are any scheduled jobs
    schedule.run_pending()
    # Wait for a short time before checking again
    time.sleep(1)
    




