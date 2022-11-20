from utils import utils

resource, table = utils.get_table_resource('todo-table')


def lambda_handler(event, context):
    try:
        todo_id = utils.get_req_param(event)
        todo_obj = utils.get_req_body(event)

        response = table.update_item(Key={
            'id': todo_id,
            },
            UpdateExpression="Set title = :title, description = :description",
            ExpressionAttributeValues={
                ':title': todo_obj.title,
                ':description': todo_obj.description
            },
            ConditionExpression="attribute_exists(id)"
        )
        return utils.get_response(response, 'update')
    except resource.meta.client.exceptions.ClientError:
        return {'status': 400,
                'error': 'There was an error during the update of the To-Do object.'}
