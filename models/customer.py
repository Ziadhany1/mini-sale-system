from models.base import BaseModel

class Customer(BaseModel):
    def __init__(self, name, email):
        super().__init__(name)
        self._email = email
        self.sale_orders = []
        self.invoices = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    def total_spent(self):
        return sum(order.total() for order in self.sale_orders)

    def total_invoiced(self):
        return sum(inv.total() for inv in self.invoices)

    def __str__(self):
        return f"{super().__str__()}, email={self.email}, total_spent={self.total_spent()}"
