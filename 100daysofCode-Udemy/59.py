import time

from kiteconnect import KiteConnect

# Set your Zerodha API key and access token
api_key = "your_api_key"
api_secret = "your_api_secret"
access_token = "your_access_token"

# Create a Kite Connect object
kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

# Define the instrument token for the stock you want to trade (e.g., Reliance)
instrument_token = "RELIANCE_INSTRUMENT_TOKEN"

# Define the quantity for trading
quantity = 1


# Function to place a market order
def execute_market_order(symbol, qty, side):
    order_info = kite.place_order(
        variety="regular",
        exchange=kite.EXCHANGE_NSE,
        tradingsymbol=symbol,
        transaction_type=side,
        quantity=qty,
        order_type=kite.ORDER_MARKET,
        product=kite.PRODUCT_MIS
    )
    return order_info


# Algorithmic trading loop
while True:
    try:
        # Get current price of the stock
        instrument_info = kite.ltp('NSE:' + instrument_token)
        current_price = instrument_info['NSE:' + instrument_token]['last_price']

        # Your trading logic goes here (e.g., moving averages, RSI, etc.)

        # Place a buy order if the condition is met
        if your_buy_condition:
            execute_market_order(instrument_token, quantity, 'BUY')
            print(f"Buy order placed for {instrument_token} at {current_price}")

        # Place a sell order if the condition is met
        if your_sell_condition:
            execute_market_order(instrument_token, quantity, 'SELL')
            print(f"Sell order placed for {instrument_token} at {current_price}")

        # Sleep for a certain interval (e.g., 1 minute)
        time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error as needed

# Remember to handle exceptions, manage rate limits, and thoroughly test your strategy in a simulated environment before using real money.
