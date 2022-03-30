API_KEY = "yourapikey"
SECRET_KEY = "yoursecretkey"

SYMBOL = "ETH/USD"
POSITION_SIZE = 0.001  # 0.001 ETH

# gridbot settings
NUM_BUY_GRID_LINES = 5  # Amount of Buy Orders
NUM_SELL_GRID_LINES = 5  # Amount of Sell Orders
GRID_SIZE = 2  # How much to add to the price of the previous order

CHECK_ORDERS_FREQUENCY = 1  # How often to check for closed orders
CLOSED_ORDER_STATUS = 'closed'  # Status of closed orders
