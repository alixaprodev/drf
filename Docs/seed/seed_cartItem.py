import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")
django.setup()

from faker import Faker
from api.models import CartItem, Cart, Product  # Import the CartItem, Cart, and Product models

def generate_fake_cart_items(num_cart_items):
    fake = Faker()

    for _ in range(num_cart_items):
        fake_cart = Cart.objects.first()  # Get the first cart (you can customize this)
        fake_product = Product.objects.first()  # Get the first product (you can customize this)
        fake_quantity = fake.random_int(min=1, max=10)  # Generate a random quantity

        cart_item = CartItem.objects.create(
            cart=fake_cart,
            product=fake_product,
            quantity=fake_quantity,
        )

if __name__ == "__main__":
    num_cart_items_to_generate = 20  # Change this to the number of cart items you want to create
    generate_fake_cart_items(num_cart_items_to_generate)
