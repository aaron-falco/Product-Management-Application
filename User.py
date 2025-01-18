from abc import ABC

class User(ABC):
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.purchases = []
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def add_purchase(self, cart):
        self.purchases.append(cart)
 