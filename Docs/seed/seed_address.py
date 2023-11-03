import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")
django.setup()

from faker import Faker
from api.models import Address, CustomUser  # Import the Address and CustomUser models

def generate_fake_addresses(num_addresses):
    fake = Faker()

    for _ in range(num_addresses):
        fake_user = CustomUser.objects.first()  # Get the first user (you can customize this)
        fake_address = fake.street_address()
        fake_city = fake.city()
        fake_postal_code = fake.postcode()
        fake_country = fake.country()

        address = Address.objects.create(
            user=fake_user,
            address=fake_address,
            city=fake_city,
            postal_code=fake_postal_code,
            country=fake_country,
        )

if __name__ == "__main__":
    num_addresses_to_generate = 10  # Change this to the number of addresses you want to create
    generate_fake_addresses(num_addresses_to_generate)
