from utils import utils

resource, table = utils.get_table_resource('todo-table')


def lambda_handler(event, context):
    try:
        todo_id = utils.get_req_param(event)
        response = table.delete_item(
            Key={
                'id': todo_id
            },
            ConditionExpression="attribute_exists(id)",
        )
        return utils.get_response(response, 'deletion')
    except resource.meta.client.exceptions.ClientError:
        return {'status': 400,
                'error': 'There was an error during the deletion of the To-Do object.'}
