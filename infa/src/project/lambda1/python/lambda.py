import json
from decimal import Decimal
import requests


def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

def lambda_handler(event, context):
    url = "https://ufsjj3gw67.execute-api.us-east-2.amazonaws.com/python2"
    fetch_resp = requests.get(url).json()['message']

    my_dict = {
        1: "Hi this is a dict inside Python1!",
        2: [

        ]
    }

    resp = {
        "message": my_dict[1] + " Python2 says " + fetch_resp,
    }

    return {
        'statusCode': 200,
        'body' : json.dumps(resp, default=default)
    }