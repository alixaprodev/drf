import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")
django.setup()

from faker import Faker
from api.models import OrderItem, Order, Product  # Import the OrderItem, Order, and Product models

def generate_fake_order_items(num_order_items):
    fake = Faker()

    for _ in range(num_order_items):
        fake_order = Order.objects.first()  # Get the first order (you can customize this)
        fake_product = Product.objects.first()  # Get the first product (you can customize this)
        fake_quantity = fake.random_int(min=1, max=10)  # Generate a random quantity

        order_item = OrderItem.objects.create(
            order=fake_order,
            product=fake_product,
            quantity=fake_quantity,
        )

if __name__ == "__main__":
    num_order_items_to_generate = 20  # Change this to the number of order items you want to create
    generate_fake_order_items(num_order_items_to_generate)
