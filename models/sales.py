from models.base import BaseModel
from models.invoice import Invoice, InvoiceLine

class SaleOrderLine:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity
        self._unit_price = product.price
        self._subtotal = self._unit_price * self._quantity

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
    def subtotal(self):
        return self._subtotal

    def __str__(self):
        return f"SaleOrderLine (product={self.product.name}, quantity={self.quantity}, subtotal={self.subtotal})"

class SaleOrder(BaseModel):
    def __init__(self, customer):
        self.customer = customer  
        name = f"SaleOrder-{BaseModel._next_id}"
        super().__init__(name)
        self.lines = []
        self.state = "draft"
        self.invoice = None
        customer.sale_orders.append(self)


    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from models.customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Invalid customer")
        self._customer = value

    def add_line(self, product, quantity):
        line = SaleOrderLine(product, quantity)
        self.lines.append(line)

    def total(self):
        return sum(line.subtotal for line in self.lines)
    
    def confirm(self):
        if self.state == "confirmed":
            print(f"SaleOrder {self.name} already confirmed.")
            return self.invoice  # ترجع نفس الفاتورة الموجودة
        self.state = "confirmed"
        self.invoice = Invoice(self.customer, order_name=self.name)
        for line in self.lines:
            inv_line = InvoiceLine(line.product, line.quantity, line._unit_price)
            self.invoice.lines.append(inv_line)
        self.customer.invoices.append(self.invoice)
        return self.invoice

    def __str__(self):
        return f"{super().__str__()}, state={self.state}, total={self.total()}"
