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

    # status code for single json as an input
    def test_status_code_single_json(self):
        data = read_json(test_data_source[0])
        data["data"]["actionType"] = "CountByGender"
        response = requests.post(url, json=data["data"])
        assert response.status_code == 200

    # Testing field json parameters
    def test_bad_data(self):
        response = requests.post(url, json=[])
        assert response.status_code == 400

    # Testing field json parameters: no value provided for actionType
    def test_bad_data_missing_action_type_value(self):
        data = read_json(test_data_source[0])
        # empty action type
        data["data"]["actionType"] = ""
        response = requests.post(url, json=data["data"])
        assert response.status_code == 400

    # Testing filed json parameters: no value provided for users
    def test_bad_data_missing_users_value(self):
        data = read_json(test_data_source[0])
        data["data"]["actionType"] = "CountByGender"
        data["data"]["users"] = ""
        response = requests.post(url, json=data["data"])
        assert response.status_code == 400

    # Testing json field top: top > 0
    def test_optional_parameter_top(self):
        data = read_json(test_data_source[0])
        data["data"]["actionType"] = "CountByCountry"
        data["data"]["top"] = "3"
        response = requests.post(url, json=data["data"])
        assert len(response.json()) == 3

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
