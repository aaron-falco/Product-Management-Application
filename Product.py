
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.available = True
    
    def is_available(self):
        return self.available
    
    def has(self, stock):
        return self.stock >= stock
    
    def sell(self, amount):
        self.stock -= amount
        return amount * self.price
    
    def delist(self):
        self.available = False
    
    def __str__(self):
        return f"{self.name} at ${self.price:.2f} ({self.stock})"