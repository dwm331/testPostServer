def handler(event, context):
    if event.get('httpMethod') != 'POST' or event.get('path') != '/api/post':
        return {
            'statusCode': 405,
            'body': '{"error": "Method Not Allowed"}',
            'headers': {'Content-Type': 'application/json'}
        }
    
    try:
        import json
        body = event.get('body', '{}')
        data = json.loads(body)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'received_data': data,
                'message': 'Data received successfully'
            }),
            'headers': {'Content-Type': 'application/json'}
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': '{"error": "Invalid JSON format"}',
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'{{"error": "Server error: {str(e)}"}}',
            'headers': {'Content-Type': 'application/json'}
        }