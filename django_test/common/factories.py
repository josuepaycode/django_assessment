# in my_project/current_app/tests/factories.py

import factory

from faker import Faker
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    is_active = True
    username = factory.LazyAttribute(lambda _: fake.unique.email())
    email = factory.LazyAttribute(lambda _: fake.unique.email())
    password = make_password("password")
    is_staff = True
    is_superuser = True
