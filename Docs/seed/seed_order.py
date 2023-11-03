import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")
django.setup()

from faker import Faker
from api.models import Order, CustomUser, Product, OrderItem

def generate_fake_orders(num_orders):
    fake = Faker()

    for _ in range(num_orders):
        fake_user = CustomUser.objects.first()  # Get the first user (you can customize this)
        fake_total_amount = fake.random_int(min=10, max=1000)  # Generates a random total amount
        fake_products = Product.objects.all()[:fake.random_int(min=1, max=5)]  # Select a random subset of products

        order = Order.objects.create(
            user=fake_user,
            total_amount=fake_total_amount,
        )

        # Create order items for the selected products
        for product in fake_products:
            fake_quantity = fake.random_int(min=1, max=10)  # Generate a random quantity
            OrderItem.objects.create(order=order, product=product, quantity=fake_quantity)

if __name__ == "__main__":
    num_orders_to_generate = 10  # Change this to the number of orders you want to create
    generate_fake_orders(num_orders_to_generate)
