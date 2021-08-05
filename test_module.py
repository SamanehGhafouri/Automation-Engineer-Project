import json
import requests
from parameterized import parameterized

url = 'https://census-toy.nceng.net/prod/toy-census'


def read_json(json_f):
    with open(json_f, "r") as f:
        data_obj = json.load(f)
    return data_obj


class Tests:

    @parameterized.expand([
        'test_data_1/gender_10_users.json',
        'test_data_1/gender_5_users.json',
        'test_data_1/gender_1_user.json',
        'test_data_1/gender_0_users.json',
        'test_data_1/gender_15_users.json'
    ])
    def test_gender(self, base):
        data = read_json(base)
        response = requests.post(url, json=data["data"])
        assert data["expected_gender"] == response.json()



