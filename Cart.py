from InvalidQuantityException import InvalidQuantityException
from Organisation import Organisation
from Manager import Manager

class Cart:
    def __init__(self, supplier, user):
        self.orders = []
        self.supplier = supplier
        self.user = user
        self.catalogue = supplier.products.get_available_products()
    
    def add_order(self, order):
        if not order.product.has(order.quantity) or order.quantity < 1:
            raise InvalidQuantityException()
        self.orders.append(order)

    def remove_order(self, order):
        self.orders.remove(order)
    
    def get_total_cost(self):
        if isinstance(Organisation.logged_in_user, Manager):
            return 0
        sum1 = 0
        for order in self.orders:
            sum1 += order.get_profit()
        return sum1

    def __str__(self):
        s =  f"Order from {self.supplier.region}: \n" 
        for order in self.orders:
            s += f"{order}\n"
        s += f"Total Cost: {self.get_total_cost()}"
        return s