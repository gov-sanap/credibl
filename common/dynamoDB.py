import boto3
def getUserfromUserName(userName, password):
    dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
    table = dynamodb.Table('test')
    response = table.query(
        IndexName="testcompositekey-id-index",
        KeyConditionExpression=Key('testcompositekey').eq('saurabh123'),
        FilterExpression=Attr(userName).eq(password)
    )
    items = response['Items']
    if not items:
        print("Incorrect userName or password")
    