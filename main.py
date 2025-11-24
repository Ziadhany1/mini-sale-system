from models.customer import Customer
from models.product import Product
from models.sales import SaleOrder
from models.invoice import Invoice

def main():
    p1 = Product("Laptop", 1500)
    p2 = Product("Mouse", 20)

    p2.price = 25

    print(p1)
    print(p2)
    print("")

    c1 = Customer("Ziad", "ziad@gmail.com")

    c1.email = "ziadh@email.com"

    print(c1)
    print("")

    order1 = SaleOrder(c1)
    order1.add_line(p1, 2)  
    order1.add_line(p2, 5)  

    print(order1)
    print("Order lines:")
    for line in order1.lines:
        print(line)
    print("")


    invoice1 = order1.confirm()

    print(invoice1)
    print("Invoice lines:")
    for line in invoice1.lines:
        print(line)
    print("")

    invoice1.post()
    print(f"Invoice state after posting: {invoice1.state}")
    print("-----------")


    print(f"Customer total spent: {c1.total_spent()}")
    print(f"Customer total invoiced: {c1.total_invoiced()}")

if __name__ == "__main__":
    main()
