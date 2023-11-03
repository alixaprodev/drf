import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")
django.setup()

from faker import Faker
from api.models import Review, CustomUser, Product  # Import the Review, CustomUser, and Product models

def generate_fake_reviews(num_reviews):
    fake = Faker()

    for _ in range(num_reviews):
        fake_user = CustomUser.objects.first()  # Get the first user (you can customize this)
        fake_product = Product.objects.first()  # Get the first product (you can customize this)
        fake_content = fake.paragraph(nb_sentences=3)
        fake_rating = fake.pydecimal(left_digits=1, right_digits=2, positive=True)

        review = Review.objects.create(
            user=fake_user,
            product=fake_product,
            content=fake_content,
            rating=fake_rating,
        )

if __name__ == "__main__":
    num_reviews_to_generate = 15  # Change this to the number of reviews you want to create
    generate_fake_reviews(num_reviews_to_generate)
