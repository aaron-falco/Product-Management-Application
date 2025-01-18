from Customer import Customer
from Manager import Manager
#from Organisation import Organisation
from NoSuchUserException import NoSuchUserException

class Users:
    def __init__(self, users=[]):
        self.users = users
    
    def seed_data(self, stores):
        self.users.append(Customer("David", "Dyer", "davey", "pass"))
        self.users.append(Customer("Aziz", "Shavershian", "1", "1"))
        self.users.append(Customer("Lee", "Yeoreum", "lee123", "wjsn"))
        self.users.append(Customer("Kim", "Dahyun", "dah-yun", "twice"))

        self.users.append(Manager("David", "Dyer", "2", "2", [
            stores.get_by_region("Penshurst"),
            stores.get_by_region("Hurstville"),
            stores.get_by_region("Allawah"),
            stores.get_by_region("Carlton"),
            stores.get_by_region("Kogarah"),
            stores.get_by_region("Waterfall"),
            stores.get_by_region("Engadine")
            ]))
        self.users.append(Manager("Big", "Paulie", "paul89", "huge", [
            stores.get_by_region("Heathcote"),
            stores.get_by_region("Loftus"),
            stores.get_by_region("Sutherland"),
            stores.get_by_region("Mortdale")
            ]))
        self.users.append(Manager("Rishik", "Sood", "rishik", "pass", [
            stores.get_by_region("Banksia"),
            stores.get_by_region("Arncliffe")
            ]))
        self.users.append(Manager("Angela", "Huo", "admin", "admin", [
            stores.get_by_region("Wolli Creek"),
            stores.get_by_region("Sydenham")
            ]))
        self.users.append(Manager("Zohair", "Gandhi", "zohair45", "ted", [
            stores.get_by_region("Redfern"),
            stores.get_by_region("Central")
            ]))
        if len(self.users[4].__dict__) < 6:
            print("Exception occured when attempting to seed data.\nHave you implemented the Manager constructor?")
        return self
    
    def validate_user(self, username, password):
        for u in self.users:
            if u.username == username and u.password == password:
                return u
        raise NoSuchUserException()