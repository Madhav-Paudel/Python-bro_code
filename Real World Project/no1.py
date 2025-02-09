import requests
import time
from datetime import datetime
import sqlite3
import json

class CryptoTracker:
    def __init__(self):
        self.db_conn = sqlite3.connect('crypto_data.db')
        self.setup_database()
        
    def setup_database(self):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS price_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                price REAL,
                timestamp DATETIME,
                is_ath BOOLEAN,
                is_atl BOOLEAN
            )
        ''')
        self.db_conn.commit()

    def get_coincap_data(self, symbol):
        try:
            url = f"https://api.coincap.io/v2/assets/{symbol.lower()}"
            response = requests.get(url)
            data = response.json()
            return float(data['data']['priceUsd'])
        except Exception as e:
            print(f"Error fetching data from CoinCap: {e}")
            return None

    def check_price_extremes(self, symbol, current_price):
        cursor = self.db_conn.cursor()
        
        # Get historical high and low
        cursor.execute('''
            SELECT MAX(price), MIN(price) 
            FROM price_history 
            WHERE symbol = ?
        ''', (symbol,))
        
        ath, atl = cursor.fetchone()
        
        if ath is None or current_price > ath:
            self.send_notification(symbol, "ATH", current_price)
            return True, False
        elif atl is None or current_price < atl:
            self.send_notification(symbol, "ATL", current_price)
            return False, True
        
        return False, False

    def send_notification(self, symbol, extreme_type, price):
        # Placeholder for notification system
        message = f"ALERT: {symbol} has reached a new {extreme_type} at ${price:.2f}"
        print(message)
        # TODO: Implement preferred notification method (email, SMS, push notification)

    def track_coin(self, symbol, interval=60):
        """Track a coin's price and check for ATH/ATL"""
        try:
            current_price = self.get_coincap_data(symbol)
            if current_price:
                is_ath, is_atl = self.check_price_extremes(symbol, current_price)
                
                cursor = self.db_conn.cursor()
                cursor.execute('''
                    INSERT INTO price_history (symbol, price, timestamp, is_ath, is_atl)
                    VALUES (?, ?, ?, ?, ?)
                ''', (symbol, current_price, datetime.now(), is_ath, is_atl))
                
                self.db_conn.commit()
                return current_price
            return None
        except Exception as e:
            print(f"Error tracking {symbol}: {e}")
            return None

def main():
    tracker = CryptoTracker()
    
    # Example usage
    symbols = ["bitcoin", "ethereum"]  # Add more coins as needed
    
    while True:
        for symbol in symbols:
            price = tracker.track_coin(symbol)
            if price:
                print(f"{symbol.upper()}: ${price:.2f}")
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()