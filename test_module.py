import json
import requests
from parameterized import parameterized

url = 'https://census-toy.nceng.net/prod/toy-census'


def read_json(json_f):
    with open(json_f, "r") as f:
        data_obj = json.load(f)
    return data_obj


class Tests:

    # Testing if the length of expected = length of actual
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_len_count_by_gender(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountByGender"
        response = requests.post(url, json=data["data"])
        if len(response.json()) != len(data["expected_gender"]):
            assert False
        assert True

    # Testing if the values are in descending order
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_count_by_gender_values_descending(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountByGender"
        response = requests.post(url, json=data["data"])

        actual = []
        for obj in response.json():
            actual.append(obj["value"])
        assert sorted(actual, reverse=True) == actual

    # Testing if (key, value) in expected is equal to (key, value) in actual
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_count_by_gender_name_value(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountByGender"
        response = requests.post(url, json=data["data"])

        actual = set()
        for obj in response.json():
            tuples = tuple([v for v in obj.values()])
            actual.add(tuples)

        expected = set()
        for obj in data["expected_gender"]:
            tuples = tuple([v for v in obj.values()])
            expected.add(tuples)
        assert expected == actual

    # Testing if the length of expected = length of actual
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_len_count_by_country(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountByCountry"
        response = requests.post(url, json=data["data"])
        if len(response.json()) != len(data["expected_country"]):
            assert False
        assert True

    # Testing if the values are in descending order
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_count_by_country_values_descending(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountByCountry"
        response = requests.post(url, json=data["data"])

        actual = []
        for obj in response.json():
            actual.append(obj["value"])
        assert sorted(actual, reverse=True) == actual

    # Testing if (key, value) in expected is equal to (key, value) in actual
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_count_by_country_name_value(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountByCountry"
        response = requests.post(url, json=data["data"])

        actual = set()
        for obj in response.json():
            tuples = tuple([v for v in obj.values()])
            actual.add(tuples)

        expected = set()
        for obj in data["expected_country"]:
            tuples = tuple([v for v in obj.values()])
            expected.add(tuples)
        assert expected == actual

    # Testing if the length of expected = length of actual
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_len_count_password_complexity(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountPasswordComplexity"
        response = requests.post(url, json=data["data"])
        if len(response.json()) != len(data["expected_password_complexity"]):
            assert False
        assert True

    # Testing if the values are in descending order
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_count_password_complexity_values_descending(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountPasswordComplexity"
        response = requests.post(url, json=data["data"])

        actual = []
        for obj in response.json():
            actual.append(obj["value"])
        assert sorted(actual, reverse=True) == actual

    # Testing if (key, value) in expected is equal to (key, value) in actual
    @parameterized.expand([
        'test_data/gender_country_password_10_user.json',
        'test_data/gender_country_password_5_user.json',
        'test_data/gender_country_password_1_user.json',
        'test_data/gender_country_password_0_users.json',
        'test_data/gender_country_password_15_user.json'
    ])
    def test_count_password_complexity_name_value(self, base):
        data = read_json(base)
        data["data"]["actionType"] = "CountPasswordComplexity"
        response = requests.post(url, json=data["data"])

        actual = set()
        for obj in response.json():
            tuples = tuple([v for v in obj.values()])
            actual.add(tuples)

        expected = set()
        for obj in data["expected_password_complexity"]:
            tuples = tuple([v for v in obj.values()])
            expected.add(tuples)
        assert expected == actual
