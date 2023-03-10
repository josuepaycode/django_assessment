import json
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import (
    APIClient,
    APITestCase,
    URLPatternsTestCase,
)
from authentication.models import Administrator
from webApp.models import Customer, CustomerPayment


class TestCustomerServices(APITestCase, URLPatternsTestCase):
    """ Test module for Customer Services"""

    urlpatterns = [
        path('api/', include('webApp.urls')),
        path('api/auth/', include('authentication.urls')),
    ]

    def setUp(self):
        """ create token for both administrator and super_administrator """
        # create admin and get token
        url_registry = reverse('create-admin')
        admin_data = {
            "username": "test-admin@dev.com",
            "email": "test-admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "Admin"
        }
        admin_response = self.client.post(url_registry, admin_data)

        url_login = reverse('login')
        admin_data_login = {
            "email": "test-admin@dev.com",
            "password": "J2GkLnAccCHm"
        }
        response_login_admin = self.client.post(url_login, admin_data_login)
        response = json.loads(response_login_admin.content)
        self.admin_token = response.get('token')

        # create super admin and get token
        super_admin_data = {
            "username": "test-super-admin@dev.com",
            "email": "test-super-admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "SuperAdmin",
            "role": "super_administrator"
        }
        super_admin_response = self.client.post(url_registry, super_admin_data)

        super_admin_data_login = {
            "email": "test-super-admin@dev.com",
            "password": "J2GkLnAccCHm"
        }
        response_login_super = self.client.post(url_login, super_admin_data_login)

        response_data = json.loads(response_login_super.content)
        self.super_admin_token = response_data.get('token')

    def test_create_customer_as_admin(self):
        """ Test if admin can add new customer """
        client = APIClient()
        customer_data = {
            "name": "John",
            "paternal_surname": "Parker",
            "email": "john-parker@marvel.com"
        }
        response = client.post(
            reverse('add-customer'),
            customer_data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('detail'), 'Token not valid')

        # adding token to header
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        response = client.post(
            reverse('add-customer'),
            customer_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, ['Insufficient permissions'])

    def test_create_customer_as_super_admin(self):
        """ Test if super admin can add new customer """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.super_admin_token}")
        customer_data = {
            "name": "John",
            "paternal_surname": "Parker",
            "email": "john-parker@marvel.com"
        }
        response = client.post(
            reverse('add-customer'),
            customer_data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)
        self.assertTrue(response_data.get('id'))
        self.assertEqual(
            response_data.get('name'),
            customer_data.get('name'),
        )
        self.assertEqual(
            response_data.get('paternal_surname'),
            customer_data.get('paternal_surname'),
        )
        self.assertEqual(
            response_data.get('email'),
            customer_data.get('email'),
        )

    def test_verify_payments_have_been_created_after_customer_was_created(self):
        """ Test if super admin can add new customer """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.super_admin_token}")
        customer_data = {
            "name": "John",
            "paternal_surname": "Parker",
            "email": "john-parker@marvel.com"
        }
        response = client.post(
            reverse('add-customer'),
            customer_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)

        customer_payments = CustomerPayment.objects.filter(customer_id=response_data.get('id'))
        self.assertTrue(customer_payments.exists())
        self.assertTrue(customer_payments.count() > 1)

    def test_get_customer_info_by_admin(self):
        """
        Test if Admin can get info from endpoints:
         - view-customers 
         - view-customer-payment
        """
        # create customer
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.super_admin_token}")
        customer_data = {
            "name": "John",
            "paternal_surname": "Parker",
            "email": "john-parker@marvel.com"
        }
        response = client.post(
            reverse('add-customer'),
            customer_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get all customers
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        response_customers = client.get(reverse('view-customers'))
        self.assertEqual(response_customers.status_code, status.HTTP_200_OK)
        customers = json.loads(response_customers.content)
        self.assertTrue(len(customers) > 0)

        # get customer payments
        response_payments = client.get( 
            reverse(
                'view-customer-payment',
                kwargs={'pk': customers[0].get('id')},
            )
        )
        self.assertEqual(response_payments.status_code, status.HTTP_200_OK)
        payments = json.loads(response_payments.content)
        self.assertTrue(len(payments) > 0)
        first_payment = payments[0]
        self.assertTrue(first_payment.get('amount'))
        self.assertTrue(first_payment.get('product_name'))
        self.assertTrue(first_payment.get('quantity'))

    def test_raises_error_when_admin_modify_customer_info(self):
        """ Test if Admin can update and delete customer instance """
        # create customer
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.super_admin_token}")
        customer_data = {
            "name": "John",
            "paternal_surname": "Parker",
            "email": "john-parker@marvel.com"
        }
        response = client.post(
            reverse('add-customer'),
            customer_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        customer = Customer.objects.get(email=customer_data.get('email'))

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")

        # try update
        response = client.patch(
            reverse('update-customer', kwargs={'pk':customer.id}),
            {"name": "Peter"},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, ['Insufficient permissions'])

        # try delete
        response = client.delete(
            reverse('delete-customer', kwargs={'pk':customer.id}),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, ['Insufficient permissions'])

    def test_get_update_delete_customer_info_by_super_admin(self):
        """
        Test if Super Admin can get, update and delete customer info
        """
        # create customer
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.super_admin_token}")
        customer_data = {
            "name": "John",
            "paternal_surname": "Parker",
            "email": "john-parker@marvel.com"
        }
        response = client.post(
            reverse('add-customer'),
            customer_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get all customers
        response_customers = client.get(reverse('view-customers'))
        self.assertEqual(response_customers.status_code, status.HTTP_200_OK)
        customers = json.loads(response_customers.content)
        self.assertTrue(len(customers) > 0)

        # get customer payments
        response_payments = client.get(
            reverse(
                'view-customer-payment',
                kwargs={'pk': customers[0].get('id')},
            )
        )
        self.assertEqual(response_payments.status_code, status.HTTP_200_OK)

        # update
        response = client.patch(
            reverse('update-customer', kwargs={'pk': customers[0].get('id')}),
            {"name": "Peter"},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get('name'), 'Peter')

        # delete
        response = client.delete(
            reverse('delete-customer', kwargs={'pk': customers[0].get('id')}),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.all().count(), 0)
