import json
import requests

data_5_users = 'tests_data/gender_5_users.json'
data_10_users = 'tests_data/gender_10_users.json'
url = 'https://census-toy.nceng.net/prod/toy-census'


def read_json(json_f):
    with open(json_f, "r") as f:
        data_obj = json.load(f)
    return data_obj


class TestsGender:

    def test_count_by_gender_5_users(self):
        request_json = read_json(data_5_users)
        response = requests.post(url, json=request_json)
        assert [{"name": "male", "value": 5}] == response.json()

    def test_count_by_gender_10_users(self):
        request_json = read_json(data_10_users)
        response = requests.post(url, json=request_json)
        assert [{"name": "male", "value": 7}, {"name": "female", "value": 3}]

