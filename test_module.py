import json
import requests
import pytest

url = 'https://census-toy.nceng.net/prod/toy-census'


def read_json(json_f):
    with open(json_f, "r") as f:
        data_obj = json.load(f)
    return data_obj


test_data_source = [
    'test_data/gender_country_password_10_user.json',
    'test_data/gender_country_password_5_user.json',
    'test_data/gender_country_password_1_user.json',
    'test_data/gender_country_password_0_users.json',
    'test_data/gender_country_password_15_user.json'
]


class Tests:

    # Testing if the length of expected = length of actual
    @pytest.mark.parametrize("source", test_data_source)
    def test_length_count_by_gender(self, source):
        data = read_json(source)
        data["data"]["actionType"] = "CountByGender"
        response = requests.post(url, json=data["data"])
        assert len(response.json()) == len(data["expected_gender"])

    # Testing if the values are in descending order
    @pytest.mark.parametrize("source", test_data_source)
    def test_count_by_gender_values_descending(self, source):
        data = read_json(source)
        data["data"]["actionType"] = "CountByGender"
        response = requests.post(url, json=data["data"])

        actual = []
        for obj in response.json():
            actual.append(obj["value"])
        assert sorted(actual, reverse=True) == actual

    # Testing if (key, value) in expected is equal to (key, value) in actual
    @pytest.mark.parametrize("source", test_data_source)
    def test_count_by_gender_name_value(self, source):
        data = read_json(source)
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
    @pytest.mark.parametrize("source", test_data_source)
    def test_length_count_by_country(self, source):
        data = read_json(source)
        data["data"]["actionType"] = "CountByCountry"
        response = requests.post(url, json=data["data"])
        assert len(response.json()) == len(data["expected_country"])

    # Testing if the values are in descending order
    @pytest.mark.parametrize("source", test_data_source)
    def test_count_by_country_values_descending(self, source):
        data = read_json(source)
        data["data"]["actionType"] = "CountByCountry"
        response = requests.post(url, json=data["data"])

        actual = []
        for obj in response.json():
            actual.append(obj["value"])
        assert sorted(actual, reverse=True) == actual

    # Testing if (key, value) in expected is equal to (key, value) in actual
    @pytest.mark.parametrize("source", test_data_source)
    def test_count_by_country_name_value(self, source):
        data = read_json(source)
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
    @pytest.mark.parametrize("source", test_data_source)
    def test_length_count_password_complexity(self, source):
        data = read_json(source)
        data["data"]["actionType"] = "CountPasswordComplexity"
        response = requests.post(url, json=data["data"])
        # todo: simplify this assertion
        assert len(response.json()) == len(data["expected_password_complexity"])

    # Testing if the values are in descending order
    @pytest.mark.parametrize("source", test_data_source)
    def test_count_password_complexity_values_descending(self, source):
        data = read_json(source)
        data["data"]["actionType"] = "CountPasswordComplexity"
        response = requests.post(url, json=data["data"])

        actual = []
        for obj in response.json():
            actual.append(obj["value"])
        assert sorted(actual, reverse=True) == actual

    # Testing if (key, value) in expected is equal to (key, value) in actual
    @pytest.mark.parametrize("source", test_data_source)
    def test_count_password_complexity_name_value(self, source):
        data = read_json(source)
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
