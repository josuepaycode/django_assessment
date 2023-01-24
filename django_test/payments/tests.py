from common.tests import BaseTestCase
from common.factories import UserFactory
from customers.factories import CustomerFactory

from .factories import PaymentFactory


# Create your tests here.
class TeamViewsetTestCase(BaseTestCase):
    def setUp(self):
        self.user = UserFactory()
        self.customer = CustomerFactory()
        self.payment_1 = PaymentFactory(
            customer = self.customer
        )

        self.url = "/api/payments/"

    def test_list_view(self):
        """Test that the list view works correctly"""
        token = self.authenticate(self.user)
        response = self.client.get(self.url, HTTP_AUTHORIZATION=token)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["count"], 11)

    def test_detail_view(self):
        """Test that the detail view works correctly"""
        token = self.authenticate(self.user)
        response = self.client.get(
            f"{self.url}{self.payment_1.id}/", HTTP_AUTHORIZATION=token
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEquals(data["product_name"], self.payment_1.product_name)
        self.assertEquals(data["amount"], self.payment_1.amount)
        self.assertEquals(data["quantity"], self.payment_1.quantity)
