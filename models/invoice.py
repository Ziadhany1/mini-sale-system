from models.base import BaseModel

class InvoiceLine:
    def __init__(self, product, quantity, unit_price):
        self._product = product
        self._quantity = quantity
        self._unit_price = unit_price
        self._subtotal = self._quantity * self._unit_price

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value
        self._subtotal = self._quantity * self._unit_price

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        if value < 0:
            raise ValueError("Unit price cannot be negative")
        self._unit_price = value
        self._subtotal = self._quantity * self._unit_price

    @property
    def subtotal(self):
        return self._subtotal

    def __str__(self):
        return f"InvoiceLine(product={self.product.name}, qty={self.quantity}, subtotal={self.subtotal})"

class Invoice(BaseModel):
    def __init__(self, customer):
        super().__init__(f"INV-{self._id}")
        self._customer = customer
        self.lines = []
        self.state = "draft"

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from models.customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Invalid customer")
        self._customer = value

    def total(self):
        return sum(line.subtotal for line in self.lines)

    def post(self):
        self.state = "posted"

    def __str__(self):
        return f"{super().__str__()}, state={self.state}, total={self.total()}"
