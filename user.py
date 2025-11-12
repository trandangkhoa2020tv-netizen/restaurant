# user.py

class User:
    def __init__(self, name, phone, email, password, role="customer"):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.role = role


class Customer(User):
    def __init__(self, name, phone, email, password):
        super().__init__(name, phone, email, password, "customer")


class Staff(User):
    def __init__(self, name, phone, email, password):
        super().__init__(name, phone, email, password, "staff")


class Admin(User):
    def __init__(self, name, phone, email, password):
        super().__init__(name, phone, email, password, "admin")
