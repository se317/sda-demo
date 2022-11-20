from utils import utils
from boto3.dynamodb.conditions import Key

resource, table = utils.get_table_resource('todo-table')


def lambda_handler(event, context):
    try:
        todo_id = utils.get_req_param(event)
        response = table.query(KeyConditionExpression=Key('id').eq(todo_id))['Items']
        if not response:
            return {'status': 404,
                    'message': 'Object not found.'}
        else:
            return response
    except resource.meta.client.exceptions.ClientError:
        return {'status': 400,
                'error': 'There was an error while loading the To-Do object.'}

