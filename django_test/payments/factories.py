import random
import factory

from faker import Faker
from .models import Payment

fake = Faker()


class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment

    amount = factory.LazyAttribute(lambda _: fake.pyfloat(left_digits=3, right_digits=3))
    product_name = factory.LazyAttribute(lambda _: fake.name())
    quantity = factory.LazyAttribute(lambda _: fake.pyint())
