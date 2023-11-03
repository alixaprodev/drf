import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docs.settings")  # Replace 'your_project_name' with your actual project name
django.setup()

from faker import Faker
from api.models import CustomUser  # Import the CustomUser model from your app

def generate_fake_users(num_users):
    fake = Faker()

    for _ in range(num_users):
        fake_email = fake.email()
        fake_username = fake.user_name()
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()

        user = CustomUser.objects.create(
            email=fake_email,
            username=fake_username,
            first_name=fake_first_name,
            last_name=fake_last_name,
            is_active=True,
            is_staff=False,
        )
        user.set_password("Admin123.com")  # Set a password for the user
        user.save()

if __name__ == "__main__":
    num_users_to_generate = 10  # Change this to the number of users you want to create
    generate_fake_users(num_users_to_generate)
