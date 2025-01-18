
class Order:
    def __init__(self, product, quantity, cart):
        self.product = product
        self.quantity = quantity
        self.cart = cart
    
    def get_profit(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"