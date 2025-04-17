from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product
from django.contrib.auth.models import User

class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('admin', 'admin@test.com', 'adminpass')
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Desc",
            price=100.0,
            stock=5
        )

    def test_product_list(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_create_admin_only(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post('/api/products/', {
            'name': 'New Item',
            'description': 'New Desc',
            'price': 50,
            'stock': 20
        })
        self.assertEqual(response.status_code, 201)

    def test_unauth_create_denied(self):
        response = self.client.post('/api/products/', {
            'name': 'Blocked Item',
            'description': 'Desc',
            'price': 20,
            'stock': 10
        })
        self.assertEqual(response.status_code, 403)
