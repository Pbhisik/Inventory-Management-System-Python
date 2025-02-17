from models.product import Product
from models.inventory import Inventory
from models.sale import Sale
from models._return1 import Return
from models.invoice import Invoice
from Scripts.generate import ReportGenerator

def setup_inventory():
    inventory = Inventory()

    # Add some product
    product1 = Product(id=1,name="widget",price=1999,category="Gadgets",quantity=100)
    product2 = Product(id=2,name="Gizmo",price=2490,category="Gadgets",quantity=50)

    inventory.add_product(product1)
    inventory.add_product(product2)
    return inventory

# Record Sales and returns
def record_sales_return():
    sale1 = Sale(id=1,product_id=1,quantity=5,price=1999)
    sale2 = Sale(id=2,product_id=2,quantity=2,price=1999)

def generate_invoice(inventory):
    product_ids = [1,2]
    for product_id in product_ids:
        invoice = Invoice(product_id,inventory)
        invoice.generate_invoice()

def check_csv_report():
    report_generator = ReportGenerator()
    report_generator.generate_report()

def run_all():
    inventory = setup_inventory()
    
    record_sales_return()

    generate_invoice(inventory)

    check_csv_report()

    print("All opration completed successfully...")


if __name__ == "__main__":
    run_all()


