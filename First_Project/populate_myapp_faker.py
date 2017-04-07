import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','First_Project.settings')

import django
django.setup()

# FAKE POP SCRIPT

import random
from myapp.models import AccessRecord, Topic, WebPage
from faker import Faker

fakegen = Faker()

topics = ['Search','Social','Marketing','CRM','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create a new webpage entry

        webpg = WebPage.objects.get_or_create(category=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record

        access_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Successfully completed populating the script")
