"""
This module is intended to be used for
the response output to API GATEWAY in AWS
for finding factorial using LAMBDA function
"""

from application.utilities.utils import json_response


# Function to the AWS lambda to serve purpose of server less
def lambda_handler(event, context=None):
    try:
        n = str(event['queryStringParameters']['n'])
        factorial_validators(n)
        calculation_output = calculate_factorial(int(n))
        response_output = json_response(message="Success",
                                        data=calculation_output,
                                        status=200)

    except ValueError:
        response_output = json_response(message="Error",
                                        data="Wrong input value...Value must be an Integer and should not have "
                                             "negative value and should start from 0",
                                        status=400)

    except (IOError, TimeoutError, Exception):
        response_output = json_response(message="Error",
                                        data="Check or pass the input and execution",
                                        status=500)

    return response_output


# Function to validate the input value
def factorial_validators(input_value):
    if int(input_value) < 0 or not str(input_value).isdecimal():
        raise ValueError()
    else:
        return True


# Function which contains the logic to calculate factorial
def calculate_factorial(n):
    if n in (0, 1):
        return 1
    return n * calculate_factorial(n - 1)
