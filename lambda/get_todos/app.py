from utils import utils

resource, table = utils.get_table_resource('todo-table')


def lambda_handler(event, context):
    try:
        response = table.scan()['Items']
        return response
    except resource.meta.client.exceptions.ClientError:
        return {'status': 400,
                'error': 'There was an error while loading the To-Do objects.'}
