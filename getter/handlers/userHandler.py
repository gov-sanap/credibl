import boto3
ddb = boto3.client("dynamodb")
import pyjwt

def login(event):
    data = event['body-json']
    if not data:
        logging.error("Validation Failed")
        raise Exception("User must be specified.", 422)
    if 'userName' not in data:
        logging.error("Validation Failed")
        raise Exception("userName must be specified.", 422)
    if 'password' not in data:
        logging.error("Validation Failed")
        raise Exception("Password must be specified.", 422)
    
    user = getUserIfExists(data.get('userName'), data.get('password'))
    print(user)
    if not user:
        print("Incorrect userName or password")

    return {"message": "Successfully came in user login"}

def getUserIfExists(userName, password):
    dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
    table = dynamodb.Table('test')
    response = table.query(
        IndexName="testcompositekey-id-index",
        KeyConditionExpression=Key('testcompositekey').eq(userName),
        FilterExpression=Attr('paasword').eq(password)
    )
    return response['Items']
    


def getUser(event):
    return {"message": "Successfully came in getUser"}