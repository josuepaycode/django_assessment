import json
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import (
    APITestCase,
    URLPatternsTestCase,
)
from authentication.models import Administrator


class TestAuthModel(APITestCase, URLPatternsTestCase):
    """ Test module for Administrator Model and Services"""

    urlpatterns = [
        path('api/auth/', include('authentication.urls')),
    ]

    def test_create_admin_with_administrator_role(self):
        """ Test if an admin can register with default administrator role"""
        url = reverse('create-admin')
        data = {
            "username": "test-admin@dev.com",
            "email": "test-admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "Admin"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)
        self.assertEqual(
            response_data.get('role'),
            Administrator.AdminRol.ADMINISTRATOR,
        )
        self.assertEqual(
            response_data.get('name'),
            data.get('name'),
        )

    def test_create_admin_with_super_administrator_role(self):
        """ Test if an admin can register with super administrator role"""
        url = reverse('create-admin')
        data = {
            "username": "test-super-admin@dev.com",
            "email": "test-super-admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "SuperAdmin",
            "role": "super_administrator"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)
        self.assertEqual(
            response_data.get('role'),
            Administrator.AdminRol.SUPER_ADMINISTRATOR,
        )
        self.assertEqual(
            response_data.get('name'),
            data.get('name'),
        )

    def test_login_admin(self):
        """ Test if an admin can login with credentials and obtain one token"""

        # create admin
        url = reverse('create-admin')
        data = {
            "username": "test-super-admin@dev.com",
            "email": "test-super-admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "SuperAdmin",
            "role": "super_administrator"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # login
        url = reverse('login')
        data = {
            "email": "test-super-admin@dev.com",
            "password": "J2GkLnAccCHm"            
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertIsNotNone(response_data)
        self.assertTrue('token' in response_data)

    def test_raises_error_when_no_username_is_supplied(self):
        """ Test if an admin can register without username"""
        url = reverse('create-admin')
        data = {
            "email": "test-admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "Admin"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_data = json.loads(response.content)
        self.assertIsNotNone(response_data)
        self.assertTrue('username' in response_data)
        self.assertEqual(
            response_data.get('username'),
            ['This field is required.'],
        )

    def test_raises_error_when_no_email_is_supplied(self):
        """ Test if an admin can register without email"""
        url = reverse('create-admin')
        data = {
            "username": "test-admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "Admin"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_data = json.loads(response.content)
        self.assertIsNotNone(response_data)
        self.assertTrue('email' in response_data)
        self.assertEqual(
            response_data.get('email'),
            ['This field is required.'],
        )

    def test_raises_error_when_no_password_is_supplied(self):
        """ Test if an admin can register without password"""
        url = reverse('create-admin')
        data = {
            "username": "test-admin@dev.com",
            "email": "test-admin@dev.com",
            "name": "Admin"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_data = json.loads(response.content)
        self.assertIsNotNone(response_data)
        self.assertTrue('password' in response_data)
        self.assertEqual(
            response_data.get('password'),
            ['This field is required.'],
        )
