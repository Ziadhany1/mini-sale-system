from models.base import BaseModel

class Product(BaseModel):
    def __init__(self, name, price):
        super().__init__(name)
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def __str__(self):
        return f"{super().__str__()}, price={self.price}"
    