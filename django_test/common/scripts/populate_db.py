import random
from django.db import transaction

from faker import Faker

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission

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
    print("¡Superadmin have been created successfully!")
    print("")
    print("username: superadmin")
    print("email: superadmin@paycode.com")
    print("password: superadmin_pass")
    print("")

    user = User.objects.create_user(
        username='admin',
        email='admin@paycode.com',
        password='admin_pass'
    )
    user.is_staff = True
    user.save()

    # Assing permissions
    content_type = ContentType.objects.get_for_model(Payment)
    permissions = Permission.objects.filter(content_type=content_type)

    for perm in permissions:
        if perm.codename == "view_payment":
            user.user_permissions.add(perm)

    content_type = ContentType.objects.get_for_model(Customer)
    permissions = Permission.objects.filter(content_type=content_type)

    for perm in permissions:
        if perm.codename == "view_customer":
            user.user_permissions.add(perm)

    print("¡Admin have been created successfully!")
    print("")
    print("username: admin")
    print("email: admin@paycode.com")
    print("password: admin_pass")
    print("")
    