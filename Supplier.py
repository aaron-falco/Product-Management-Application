from Products import Products

class Supplier:
    def __init__(self, name, region, address, products):
        self.name = name
        self.region = region
        self.address = address
        self.products = Products(products)
        self.profit = 0
    
    def process_cart(self, cart):
        for order in cart.orders:
            order.product.sell(order.quantity)
        self.profit += cart.get_total_cost()
    
    def __str__(self):
        return f"{self.name} ({self.region}), {self.address}"