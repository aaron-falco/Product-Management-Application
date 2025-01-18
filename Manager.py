from User import User
from Suppliers import Suppliers

class Manager(User):
    def __init__(self, first_name, last_name, username, password, suppliers):
        super().__init__(first_name, last_name, username, password)
        self.suppliers = Suppliers(suppliers)

    def __str__(self):
        return f"{super().get_full_name()}, manager for: {self.suppliers.__str__()}"