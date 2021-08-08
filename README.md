# Automation-Engineer-Project
This project is about testing an API endpoint  https://census-toy.nceng.net/prod/toy-census that takes a list of users from https://randomuser.me/api  and returns some statistics about them.  
### Program and Framework:
* I used [pytest](https://pypi.org/project/pytest/) framework because it is mainly used for testing APIs, less syntax, running tests in parallel, gives enough information about errors, and allows writing test codes in `Python` programming language which I used for this project.

* I also used [pytest.mark.parametrize](https://docs.pytest.org/en/6.2.x/parametrize.html) decorator to parametrize my test data json files to reuse test functions.

### Test Data
`test_data` folder includes 5 different json files.
Each file has the following structure:   

```buildoutcfg
* "description": The description of json data
* "data": The data that sent to api includes "actionType", "top", and list of "users"
* "expected_gender": A list of expected count users by gender
* "expected_country": A list of expected count by country
* "expected_password_complexity": A list of expected count by password complexity
```
### What I tested
In `test_module.py` I wrote 14 test functions and ran 50 tests. 44 tests passed, and 6 failed.

Complete test report is available at [Samaneh Ghafouri-NC API  test report](https://docs.google.com/spreadsheets/d/1KcwUPNbdl2S6f6Tnvk7WjgKoXQYIjvT5N9xF7REJbZg/edit?usp=sharing)

#### 6 failed tests about:
* 3 failed tests for `status code`: 400 for bad data expected but got 200.
* 1 failed test`top`: The number of returned results are not consistent.
* 2 failed test `CountByCountry`: Values not in descending order.
