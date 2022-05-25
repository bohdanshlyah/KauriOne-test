import unittest

from main import get_data
from requests.exceptions import MissingSchema, InvalidURL


class TestGetDataFucntion(unittest.TestCase):
    def setUp(self):
        self.correct_url = 'https://coinpay.org.ua/api/v1/currency'
        self.incorect_url = 'https://coinpay.org.ua/api/v1/curr'
        self.data = get_data(self.correct_url)

    def test_correct_answer(self):
        correct_answer = {'Success': {'status': 'success', 'currencies': [
            'BTC', 'EUR', 'UAH', 'USD', 'ETH', 'USDT', 'LTC', 'BNB', 'DOGE']}}
        self.assertEqual(self.data, correct_answer)

    def test_correct_data_type(self):
        self.assertEqual(type(self.data), dict)

    def test_correct_url(self):
        correct_data = {'status': 'success', 'currencies': [
            'BTC', 'EUR', 'UAH', 'USD', 'ETH', 'USDT', 'LTC', 'BNB', 'DOGE']}
        self.assertEqual(self.data['Success'], correct_data)

    def test_incorrect_url(self):
        error_text = {
            'Error': '404\n<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'}
        self.assertEqual(get_data(self.incorect_url), error_text)

    def test_errors(self):
        with self.assertRaises(MissingSchema):
            get_data("")
        with self.assertRaises(MissingSchema):
            get_data("abcd")
        with self.assertRaises(MissingSchema):
            get_data(123)
        with self.assertRaises(InvalidURL):
            get_data(["1", "one"])


if __name__ == "__main__":
    unittest.main()
