import pytest


def pytest_addoption(parser):
    parser.addoption("--format", action="store", default="json",
                     help="Format for REST response: xml or json")


@pytest.fixture
def output_format(request):
    return request.config.getoption("--format")


@pytest.fixture
def api_key():
    return "&key=AIzaSyCEF5uFW7KYGLUpzqpgWwYrlqXpqjz8PCw"


@pytest.fixture
def fake_api_key():
    return "&key=FaKeApIKeY"


@pytest.fixture
def geocode_schema():
    return open('tests/support/schemas/geocode_schema.json').read()


@pytest.fixture
def reverse_geocode_schema():
    return open('tests/support/schemas/reverse_geocode_schema.json').read()


@pytest.fixture
def request_denied_zero_results_invalid_request_schema():
    return open('tests/support/schemas/request_denied_zero_results_invalid_request_schema.json').read()


@pytest.fixture
def https_url(output_format):
    return "https://maps.googleapis.com/maps/api/geocode/" + output_format


@pytest.fixture
def http_url(output_format):
    return "http://maps.googleapis.com/maps/api/geocode/" + output_format
