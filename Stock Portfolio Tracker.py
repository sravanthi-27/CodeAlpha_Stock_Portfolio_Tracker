import random
class StockPortfolio:
    def __init__(self):
        self.stocks = {}
    def add_stock(self, symbol, price):
        if symbol not in self.stocks:
            self.stocks[symbol] = price
            print(f"Added {symbol}: ${price:.2f}")
        else:
            print(f"Stock {symbol} already in portfolio.")

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol}")
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def update_prices(self):
        for symbol in self.stocks:
            # Simulating price update by a random factor
            new_price = self.stocks[symbol] * random.uniform(0.9, 1.1)
            self.stocks[symbol] = new_price
        print("Prices updated.")

    def display_portfolio(self):
        print("\nStock Portfolio:")
        for symbol, price in self.stocks.items():
            print(f"{symbol}: ${price:.2f}")
        self.update_total_value()

    def update_total_value(self):
        total_value = sum(self.stocks.values())
        print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. Update Prices")
        print("4. Display Portfolio")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            price = float(input("Enter stock price: "))
            portfolio.add_stock(symbol, price)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            portfolio.remove_stock(symbol)
        elif choice == '3':
            portfolio.update_prices()
        elif choice == '4':
            portfolio.display_portfolio()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
