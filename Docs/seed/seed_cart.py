import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")
django.setup()

from faker import Faker
from api.models import Cart, CustomUser, Product, CartItem  # Import the Cart, CustomUser, Product, and CartItem models

def generate_fake_carts(num_carts):
    fake = Faker()

    for _ in range(num_carts):
        fake_user = CustomUser.objects.first()  # Get the first user (you can customize this)
        fake_cart = Cart.objects.create(user=fake_user)

        # Select a random subset of products
        fake_products = Product.objects.all()[:fake.random_int(min=1, max=5)]

        # Create cart items for the selected products
        for product in fake_products:
            fake_quantity = fake.random_int(min=1, max=10)  # Generate a random quantity
            CartItem.objects.create(cart=fake_cart, product=product, quantity=fake_quantity)

if __name__ == "__main__":
    num_carts_to_generate = 10  # Change this to the number of carts you want to create
    generate_fake_carts(num_carts_to_generate)
