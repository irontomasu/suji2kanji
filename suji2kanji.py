import json
from kanjize import int2kanji, kanji2int


def lambda_handler(event, context):
    try:
        arguments: dict = event["queryStringParameters"]
        number: int = int(arguments["number"])
        print("NUMBER: ", number)
    except KeyError:
        print("KeyError Detected")
        print("EVENT: ")
        print(event)
        number: int = 0
    responseBody: dict = {
        'kanji': int2kanji(number)
    }
    print("RESULT: ", responseBody)
    response: dict = {
        'statusCode': 200,
        'headers': {
            "x-custom-header": "my custom header value",

        },
        'body': json.dumps(responseBody)
    }
    return response
