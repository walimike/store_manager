import unittest
from api import app
from api.models.products import my_products, Product


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.test_question = {"question":"What is up?"}

    def tearDown(self):
        pass

    def test_welcome_message(self):
        response = self.client.get('/v1/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to Store Manager.', str(response.data))

    def test_empty_product_list(self):
        response = self.client.get('/v1/api/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product list is currently empty', str(response.data))

    def test_product_list(self):
        new_product = Product("Detergent","soap",1500)
        my_products.product_list.append(new_product.to_json())
        response = self.client.get('/v1/api/products')
        self.assertEqual(response.status_code, 200)
