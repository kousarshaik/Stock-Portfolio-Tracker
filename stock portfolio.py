import os
class Stock:
    def __init__(self, symbol, quantity, purchase_price):
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.current_price =None #Placeholder for real-time price
    def update_price(self, api_client):
        # Replace this with code to call the API and update self.current_price
        # based on the provided symbol
        print(f"API not implemented yet. Please update price for {self.symbol} manually.")
    def get_current_value(self):
      if self.current_price is None:
        return None
      return self.current_price * self.quantity
    def get_performance(self):
      if self.current_price is None or self.purchase_price == 0:
        return None
      return ((self.current_price - self.purchase_price) / self.purchase_price) * 100
class Portfolio:
    def __init__(self):
      self.holdings = []
    def add_stock(self, symbol, quantity, purchase_price):
      self.holdings.append{Stock(symbol, quantity, purchase_price)}
    def remove_stock(self, symbol):
      for stock in self.holdings:
        if stock.symbol == symbol:
          self.holdings.remove(stock)
          return
      print(f"Stock '(symbol)' not found in portfolio.")
    def update_prices(self, api_client):
      for stock in self.holdings:
        stock.update_price(api_client)
    def get_total_value(self):
      total_value = 0
      for stock in self.holdings:
        value = stock.get_current_value()
        if value is not None:
          total_value +=value
      return total-value
    def get_overall_performance(self):
      total_performance = 0
      total_weight = 0
      for stock in self.holdings:
        performance = stock.get_current_value()
        if performance is not None:
          total_performance += performance * value 
          total_weight += value 
      if total_performance / total_weight
    def display_portfolio(self):
      print("-" * 80)
      print("{:<15s} {:<10s} {:<20s} {:<20s} {:<20s}".format(
          "Symbol", "Quantity", "Purchase Price", "Current Price", "Performance (%)"))
      print("-" * 80)
      for stock in self.holdings:
        print("{:<15s} {:<10d} ${:<10.2f} ${:<10.2f} {:>+7.2f}%".format(
            stock.symbol, stock.quantity, stock.purchase_price, stock.current_price, stock.get_performance()))
      print("-" * 80)
      print("Total Value: ${:.2f}".format(self.get_total_value()))
      overall_performance + self.get 
            