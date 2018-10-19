import unittest
from api import app
from api.models.products import my_products


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
