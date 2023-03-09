import random
from .models import Customer, CustomerPayment

PRODUCTS = [
    {
        'unit_price': 799.0,
        'name': 'HyperX Cloud Stinger',
    },
    {
        'unit_price': 1189.31,
        'name': 'Logitech G502',
    },
    {
        'unit_price': 1253.25,
        'name': 'Logitech G435',
    },
    {
        'unit_price': 1799.0,
        'name': 'Logitech MX Master 3S',
    },
    {
        'unit_price': 1496.0,
        'name': 'Blue Yeti Micrófono',
    },
    {
        'unit_price': 199.0,
        'name': 'HyperX Fury S Speed Edition',
    },
    {
        'unit_price': 469.59,
        'name': 'Cooler Master PBT',
    },
    {
        'unit_price': 626.0,
        'name': 'Logitech CAMLOG480',
    },
    {
        'unit_price': 782.58,
        'name': 'Lenovo Mochila Gaming',
    },
    {
        'unit_price': 899.0,
        'name': 'Funda Gaming OMEN',
    },
]


def create_customer_payments(customer_id: int):
    """function for create fake payments"""
    customer = Customer.objects.get(pk=customer_id)
    n = random.randint(5,20)
    payments = []

    for i in range(n):
        elements = random.randint(1,10)
        index = random.randint(0,9)
        payments.append(
            CustomerPayment(
                amount=PRODUCTS[index]['unit_price']*elements,
                customer_id=customer,
                product_name=PRODUCTS[index]['name'],
                quantity=elements,
            )
        )
    CustomerPayment.objects.bulk_create(payments)
