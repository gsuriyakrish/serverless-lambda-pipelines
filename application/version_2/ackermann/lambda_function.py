"""
This module is intended to be used for
the response output to API GATEWAY in AWS
for finding ackermann using LAMBDA function
"""

from application.utilities.utils import json_response


# Function to the AWS lambda to serve purpose of server less
def lambda_handler(event, context=None):
    try:
        m = str(event['queryStringParameters']['m'])
        n = str(event['queryStringParameters']['n'])
        ackermann_validators(m, n)
        calculation_output = calculate_ackermann(int(m), int(n))
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
def ackermann_validators(input_value_m, input_value_n):
    if int(input_value_m) < 0 or not str(input_value_m).isdecimal():
        raise ValueError()
    if int(input_value_n) < 0 or not str(input_value_n).isdecimal():
        raise ValueError()
    else:
        return True


# Function which contains the logic to calculate factorial
def calculate_ackermann(m, n):
    output = []
    while True:
        if not m:
            try:
                i = output.index(0)
            except ValueError:
                return n + 1
            n += len(output[i:])
            output = output[:i]
            try:
                m, n = output.pop(), n + 1
            except IndexError:
                return n + 1
        else:
            m -= 1
            output.extend([m] * n)
            n = 1


