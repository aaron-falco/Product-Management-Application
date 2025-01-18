from User import User

class Customer(User):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)

    def __str__(self):
        return super().get_full_name()