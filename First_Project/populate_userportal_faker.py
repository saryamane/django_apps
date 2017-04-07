import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','First_Project.settings')

import django
django.setup()

# FAKE POP SCRIPT

import random
from userportal.models import User
from faker import Faker

fakegen = Faker()

def populate_users(N=5):

    for entry in range(N):

        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # Create a new user record entry

        user_entry = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email_addr=fake_email)[0]

if __name__ == '__main__':
    print("Populating user entry script")
    populate_users(20)
    print("Successfully completed populating the script")
