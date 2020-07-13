from nose.tools import *
from application.version_1.ackermann.lambda_function import lambda_handler, calculate_ackermann, ackermann_validators


def test_lambda_handler_valid_status():
    event = {'queryStringParameters': {'n': 2, 'm': 2}}
    output = lambda_handler(event, None)
    assert output['statusCode'] == 200


@raises(Exception)
def test_lambda_handler_500():
    response = lambda_handler()
    assert response is not None
    assert response['statusCode'] == 500


@raises(ValueError)
def test_lambda_handler_400():
    m, n = -1, 0
    response = ackermann_validators(m, n)
    assert response is not None
    assert response['statusCode'] == 400


def test_calculate_ackermann_m_3_n_4():
    m, n = 3, 4
    output = calculate_ackermann(m, n)
    assert output == 125


def test_calculate_ackermann_m_1_n_1():
    m, n = 1, 1
    output = calculate_ackermann(m, n)
    assert output == 3


def test_calculate_ackermann_m_3_n_6():
    m, n = 3, 6
    output = calculate_ackermann(m, n)
    assert output == 509


def test_ackermann_validators_m_3_n_1():
    m, n = 3, 1
    output = ackermann_validators(m, n)
    assert output == True
