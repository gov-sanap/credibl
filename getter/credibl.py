import boto3
import logging
from getter.handlers import contentHandler,userHandler

def handler(event, context):

    eventContext = event.get('context')
    print(eventContext)
    method = eventContext.get('http-method')
    print(method)
    path = eventContext.get('resource-path')
    print(path)
    operation = (path + '_' + method).lower()
    print(operation)
    
    operations = {
        '/users/login_post': lambda x: userHandler.login(x),
        '/users/{id}_get': lambda x: userHandler.getUser(x)
    }

    if operation in operations:
        return operations[operation](event)
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
    '''
    return {"message": "Successfully executed"}
    '''