import factory

from faker import Faker
from .models import Customer

fake = Faker()


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.LazyAttribute(lambda _: fake.name())
    paternal_surname = factory.LazyAttribute(lambda _: fake.name())
    email= factory.LazyAttribute(lambda _: fake.email())
