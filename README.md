Structure suggestion for your mini Odoo project:
# Mini Odoo Project

A simplified Odoo-like system implemented in Python, featuring basic models for customers, products, sales orders, and invoices.

## Features

- Create customers with email validation
- Create products with price validation
- Create sale orders linked to customers
- Confirm sale orders and generate invoices
- Post invoices and track totals per customer
- Simple command-line menu interface

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Ziadhany1/mini-sale-system.git
cd mini-sale-system

**Create a virtual environment:
python -m venv .venv

Activate the virtual environment:
Windows PowerShell:
.venv\Scripts\Activate.ps1

Run the project:
python main.py
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Usage:
- Follow the command-line menu to create customers, products, sale orders, and invoices.
- Confirm sale orders to generate invoices.
- Post invoices to finalize them.
- View customer totals for spent and invoiced amounts.


---

## **Document Each Model**

### **BaseModel**
- Base class for all models
- Auto-incrementing `id`
- `name` attribute with getter/setter
- Provides a string representation of objects

### **Customer**
- Inherits from `BaseModel`
- Attributes:
  - `email` (validated)
  - `sale_orders` (list of sale orders)
  - `invoices` (list of invoices)
- Methods:
  - `total_spent()`
  - `total_invoiced()`

### **Product**
- Inherits from `BaseModel`
- Attributes:
  - `price` (validated)
- Represents products that can be added to orders

### **SaleOrder**
- Inherits from `BaseModel`
- Attributes:
  - `customer` (Customer object)
  - `lines` (list of SaleOrderLine)
  - `state` ("draft", "confirmed")
  - `invoice` (generated Invoice)
- Methods:
  - `add_line(product, quantity)`
  - `total()`
  - `confirm()` → creates an Invoice

### **SaleOrderLine**
- Helper class for `SaleOrder`
- Attributes:
  - `product`
  - `quantity`
  - `subtotal`

### **Invoice**
- Inherits from `BaseModel`
- Attributes:
  - `customer` (Customer object)
  - `lines` (list of InvoiceLine)
  - `state` ("draft", "posted")
- Methods:
  - `total()`
  - `post()`

### **InvoiceLine**
- Helper class for `Invoice`
- Attributes:
  - `product`
  - `quantity`
  - `unit_price`
  - `subtotal`

---

## **Workflow & Relationships**

```text
Customer ---< SaleOrder ---< SaleOrderLine >--- Product
Customer ---< Invoice ---< InvoiceLine >--- Product
SaleOrder.confirm() -> generates Invoice for the Customer
Invoice.post() -> finalizes the invoice

