# Question: Day 56: Create a simple inventory system using dataclasses.
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    quantity: int

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def total_value(self):
        return sum(p.price * p.quantity for p in self.products)

inventory = Inventory()
inventory.add_product(Product(1, "Laptop", 999.99, 5))
print(f"Total value: ${inventory.total_value():.2f}")
