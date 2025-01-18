from Suppliers import Suppliers
from Users import Users

class Organisation:
    logged_in_user = None
    def __init__(self):
        self.suppliers = Suppliers().seed_data()
        self.users = Users().seed_data(self.suppliers)