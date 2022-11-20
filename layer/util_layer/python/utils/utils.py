import json
import boto3
from types import SimpleNamespace as Namespace


def get_table_resource(table_name):
    resource = boto3.resource('dynamodb')
    table = resource.Table(table_name)

    return resource, table


def get_req_param(event):
    if 'pathParameters' in event:
        return event['pathParameters'].get('id')
    else:
        raise KeyError('Path parameter not found')


def get_req_body(event):
    if 'body' in event:
        return json.loads(event['body'], object_hook=lambda d: Namespace(**d))
    else:
        raise KeyError('Body not found')


def get_response(response, action):
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {'status': 200,
                'message': 'To-Do object {} successful.'.format(action)}
    else:
        return {'status': 400,
                'error': 'There was an error during the {} of the To-Do object.'.format(action)}
