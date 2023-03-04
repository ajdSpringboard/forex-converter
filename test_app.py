import unittest
from app import app

class HomeTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Currency Converter!</h1>', response.data)
        
    def test_currency_conversion(self):
        data = {
            'curr_from': 'USD',
            'curr_to': 'EUR',
            'curr_amt': 100
        }
        response = self.client.post('/', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Currency Converter!</h1>', response.data)
        self.assertIn(b'Your result is:', response.data)
        

if __name__ == '__main__':
    unittest.main()
