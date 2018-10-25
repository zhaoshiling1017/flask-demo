import unittest
from myapp import create_app
import config

app = create_app(config)


class SampleTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_hello(self):
        with app.test_client() as client:
            response = client.get('/', follow_redirects=True)
            assert '<h1>Hello World from app factory!</h1>' == response.data

if __name__ == '__main__':
    unittest.main()
