from utils import utils

resource, table = utils.get_table_resource('todo-table')


def lambda_handler(event, context):
    try:
        todo_obj = utils.get_req_body(event)

        item = {
            'id': todo_obj.id,
            'title': todo_obj.title,
            'description': todo_obj.description
        }

        response = table.put_item(Item=item,
                                  ConditionExpression="attribute_not_exists(id)",
                                  )
        return utils.get_response(response, 'creation')
    except resource.meta.client.exceptions.ClientError:
        return {'status': 400,
                'error': 'There was an error during the creation of the To-Do object.'}
