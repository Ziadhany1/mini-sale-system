from models.customer import Customer
from models.product import Product
from models.sales import SaleOrder
from models.invoice import Invoice

customers = []
products = []
sale_orders = []
invoices = []

def create_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    customer = Customer(name, email)
    customers.append(customer)
    print(f"Customer created: {customer}")

def create_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    product = Product(name, price)
    products.append(product)
    print(f"Product created: {product}")

def create_sale_order():
    if not customers:
        print("No customers available. Create a customer first.")
        return
    if not products:
        print("No products available. Create a product first.")
        return

    print("Select customer:")
    for i, cust in enumerate(customers, 1):
        print(f"{i}. {cust.name}")
    cust_index = int(input("Enter number: ")) - 1
    customer = customers[cust_index]

    order = SaleOrder(customer)

    while True:
        print("Select product to add to order (0 to finish):")
        for i, prod in enumerate(products, 1):
            print(f"{i}. {prod.name} - ${prod.price}")
        choice = int(input("Enter number: "))
        if choice == 0:
            break
        qty = int(input("Enter quantity: "))
        product = products[choice - 1]
        order.add_line(product, qty)

    sale_orders.append(order)
    print(f"Sale order created: {order}")

def confirm_sale_order():
    if not sale_orders:
        print("No sale orders to confirm.")
        return
    print("Select sale order to confirm:")
    for i, order in enumerate(sale_orders, 1):
        print(f"{i}. {order.name} (state: {order.state})")
    choice = int(input("Enter number: ")) - 1
    order = sale_orders[choice]
    invoice = order.confirm()
    invoices.append(invoice)
    print(f"Invoice created: {invoice}")

def post_invoice():
    if not invoices:
        print("No invoices to post.")
        return
    print("Select invoice to post:")
    for i, inv in enumerate(invoices, 1):
        print(f"{i}. {inv.name} (state: {inv.state})")
    choice = int(input("Enter number: ")) - 1
    invoice = invoices[choice]
    invoice.post()
    print(f"Invoice posted: {invoice.name}, state: {invoice.state}")

def show_customer_totals():
    if not customers:
        print("No customers available.")
        return
    for cust in customers:
        print(f"{cust.name} - total spent: {cust.total_spent()}, total invoiced: {cust.total_invoiced()}")

def main_menu():
    while True:
        print("\n==============================")
        print(" Mini Odoo Mini Project Menu")
        print("==============================")
        print("1. Create Customer")
        print("2. Create Product")
        print("3. Create Sale Order")
        print("4. Confirm Sale Order / Create Invoice")
        print("5. Post Invoice")
        print("6. Show Customer Totals")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_product()
        elif choice == "3":
            create_sale_order()
        elif choice == "4":
            confirm_sale_order()
        elif choice == "5":
            post_invoice()
        elif choice == "6":
            show_customer_totals()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
