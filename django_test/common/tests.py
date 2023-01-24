from django.test import TestCase
from django.contrib.auth.models import User


class BaseTestCase(TestCase):
    def authenticate(self, user: User):
        response = self.client.post(
            "/api/token/",
            data={"username": user.username, "password": "password"},
        )
        _token = response.json().get("access")
        return f"Bearer {_token}"
