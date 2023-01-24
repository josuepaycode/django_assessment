import random
from django.db import transaction

from faker import Faker

from customers.models import Customer
from payments.models import Payment

from django.contrib.auth.models import User

fake = Faker()

@transaction.atomic
def run():
    # Creating custormers
    for i in range(0, 5):
        Customer.objects.create(
            name=fake.name(),
            paternal_surname=fake.name(),
            email=fake.email(),
        )

    # Creating payments
    customers = Customer.objects.all()
    for i in range(0, 10):
        Payment.objects.create(
            amount=fake.pyfloat(left_digits=3, right_digits=3), 
            product_name=fake.name(), 
            quantity=fake.pyint(),
            customer=random.choice(customers)
        )

    # Creating super administrator
    User.objects.create_superuser("superadmin", "superadmin@paycode.com", "superadmin_pass")
    print("¡Admins created successfully!")
    print("")
    print("New super user was added:")
    print("username: superadmin")
    print("email: superadmin@paycode.com")
    print("password: superadmin_pass")
    print("")

