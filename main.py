import time
import os
import requests
import json
from datetime import datetime
from menu import *

class CryptoTrader:
    def __init__(self):
        # Load configuration from JSON file
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            
        # Initialize instance variables using configuration
        self.buy_threshold = config["buy_threshold"]  # Percentage below bought price to trigger a buy
        self.sell_threshold = config["sell_threshold"]  # Percentage above bought price to trigger a sell
        self.bank_balance = config["bank_balance"]  # Initial amount of money available for trading
        self.crypto_symbol = config["crypto_symbol"]  # Symbol of the cryptocurrency (e.g., "bitcoin")
        self.wait_time = config["wait_time"]  # Time interval in seconds between trading actions
        self.api_url = "https://api.coingecko.com/api/v3"  # API endpoint for cryptocurrency data
        self.crypto_balance = 0  # Current balance of cryptocurrency
        self.trade_history = []  # List to store trading history
        self.last_price = None  # Price at which the cryptocurrency was last bought or sold
        self.initial_bank = self.bank_balance  # Initial bank balance for profit calculation

    # Check if the API is online
    def APICheck(self):
        response = requests.get(f"{self.api_url}/ping")
        
        if(response.status_code == 200):
            data = response.json()

            if(data.get('gecko_says') == '(V3) To the Moon!'):
                # If API is online
                return True
            else:
                # If API is offline
                return False

    # Clear the terminal screen
    def ClearScreen(self):
        # Clears the terminal screen (works on both Windows and Unix-like systems)
        os.system('cls' if os.name == 'nt' else 'clear')

    # Get the current timestamp
    def GetTimestamp(self):
        now = datetime.now()
        timestamp = now.strftime('%H:%M:%S')
        return timestamp

    # Fetch the current price of the cryptocurrency from CoinGecko
    def GetPrice(self):
        response = requests.get(f"{self.api_url}/simple/price?ids={self.crypto_symbol}&vs_currencies=usd")
        price_info = response.json()
        return price_info[self.crypto_symbol]['usd']

    # Determine whether to buy, sell, or hold based on thresholds
    def DeterminMove(self, current_price):
        if current_price <= self.bought_price - (self.buy_threshold * self.bought_price):
            result = "Buy"
        elif current_price >= (self.sell_threshold * self.bought_price) + self.bought_price:
            result = "Sell"
        else:
            result = "Hold"
        return result

    # Perform a trade and update trade history
    def PerformTrade(self, action, current_price):
        timestamp = self.GetTimestamp()
        if action == "Buy" and self.crypto_balance == 0:
            self.crypto_balance = self.bank_balance / current_price
            self.trade_history.append(f"BUY: {self.crypto_balance:.8f}BTC @ ${current_price:.2f} [{timestamp}]")
            self.bank_balance = 0
            self.bought_price = current_price
        elif action == "Sell" and self.bank_balance == 0:
            self.bank_balance = self.crypto_balance * current_price
            self.trade_history.append(f"SELL: {self.crypto_balance:.8f}BTC @ ${current_price:.2f} [{timestamp}]")
            self.crypto_balance = 0
            self.bought_price = current_price

    # Main trading loop
    def bot_loop(self):
        print(crypto_graphics)
        action = self.APICheck()
        if action:
            if self.crypto_balance == 0:
                timestamp = self.GetTimestamp()
                current_price = self.GetPrice()
                self.crypto_balance = self.bank_balance / current_price
                self.bank_balance = 0
                self.bought_price = current_price
                profit = self.bank_balance - self.initial_bank
                self.ClearScreen()
                self.trade_history.append(f"INITIAL BUY: {self.crypto_balance:.8f}BTC @ ${current_price:.2f} [{timestamp}]")
                action = "Buy"
                InfoMenu(self.bank_balance, action, profit, self.crypto_balance, self.trade_history)

                time.sleep(int(self.wait_time))

                while True:
                    current_price = self.GetPrice()
                    timestamp = self.GetTimestamp()

                    action = self.DeterminMove(current_price)
                    if action:
                        self.PerformTrade(action, current_price)

                    profit = self.bank_balance - self.initial_bank
                    self.ClearScreen()
                    InfoMenu(self.bank_balance, action, profit, self.crypto_balance, self.trade_history)

                    time.sleep(int(self.wait_time))
        else:
            self.ClearScreen()
            print(crypto_graphics)
            print("API has failed to connect. Press enter to continue...")
            choice = input()

# Run the bot when the script is executed
if __name__ == "__main__":
    trader = CryptoTrader()
    trader.ClearScreen()
    trader.bot_loop()
