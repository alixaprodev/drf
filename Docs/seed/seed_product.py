import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")
django.setup()

from faker import Faker
from api.models import Product, Category  # Import the Product and Category models

def generate_fake_products(num_products):
    fake = Faker()

    for _ in range(num_products):
        fake_name = fake.word()  # Generates a random word for the product name
        fake_price = fake.random_int(min=1, max=1000)  # Generates a random price
        fake_category = Category.objects.first()  # Get the first category (you can customize this)
        fake_description = fake.text(max_nb_chars=200)
        fake_rating = fake.pydecimal(left_digits=1, right_digits=2, positive=True)
        
        product = Product.objects.create(
            name=fake_name,
            price=fake_price,
            category=fake_category,
            description=fake_description,
            rating=fake_rating,
        )

if __name__ == "__main__":
    num_products_to_generate = 20  # Change this to the number of products you want to create
    generate_fake_products(num_products_to_generate)
