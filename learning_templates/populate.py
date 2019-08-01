import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning_templates.settings')

import django
django.setup()

from basic_app.models import user

from faker import Faker
fake_gen = Faker()

def add_user(N=5):
    for i in range(N):
        fake_first = fake_gen.first_name()
        fake_last = fake_gen.last_name()
        email = fake_gen.email()
        u = user.objects.get_or_create(first_name = fake_first,last_name = fake_last,email = email)[0]

if __name__ == '__main__':
    add_user(20)
