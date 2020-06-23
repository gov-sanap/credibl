import boto3
ddb = boto3.client("dynamodb")

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
    
    user = loginuser(data.get('userName'), data.get('password'))

    return {"message": "Successfully came in user login"}

def loginuser(userName, password):
    try:
        ex="testcompositekey = : "+ userName
        print(ex)
        ey ="paasword = :"+ password
        print(ey)
        data = ddb.query(
            TableName="test",
            KeyConditionExpression=ex,
            FilterExpression="paasword = :"+ password
        )
    except BaseException as e:
        print(e)
        raise(e)
    


def getUser(event):
    return {"message": "Successfully came in getUser"}