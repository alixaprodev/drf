import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")
django.setup()

from faker import Faker
from api.models import Category  # Import the Category model

def generate_fake_categories(num_categories, parent_category=None):
    fake = Faker()

    for _ in range(num_categories):
        fake_name = fake.word()  # Generates a random word for the category name

        # Create a new category with an optional parent category
        category = Category.objects.create(
            name=fake_name,
            parent=parent_category,
        )

        # Create subcategories for the current category
        if fake.random_element(elements=(True, False)):
            generate_fake_categories(fake.random_int(min=1, max=5), parent_category=category)

if __name__ == "__main__":
    num_categories_to_generate = 5  # Change this to the number of categories you want to create
    generate_fake_categories(num_categories_to_generate)
