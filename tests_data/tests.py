import json
import unittest
import requests

data_one = 'data_three.json'
data_two = 'data_four.json'


def read_json(json_f):
    with open(json_f, "r") as f:
        data_obj = json.load(f)
    return data_obj


class TestActionType(unittest.TestCase):

    def setUp(self):
        self.url = 'https://census-toy.nceng.net/prod/toy-census'

    def test_count_by_gender(self):
        request_json = read_json(data_one)
        response = requests.post(self.url, json=request_json)

        actual = response.json()
        expected = [{"name": "male", "value": 5}]
        self.assertEqual(expected, actual)

    def test_count_by_gender_data2(self):
        request_json = read_json(data_two)
        response = requests.post(self.url, json=request_json)

        actual = response.json()
        expected = [{"name": "male", "value": 7}, {"name": "female", "value": 3}]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
