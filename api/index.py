def handler(event, context):
    try:
        method = event.get('httpMethod', 'GET')
        path = event.get('path', '')

        if method == 'GET':
            if path == '/api/post':
                return {
                    'statusCode': 200,
                    'body': '{"message": "This is a GET response from /api/post"}',
                    'headers': {'Content-Type': 'application/json'},
                    'isBase64Encoded': False
                }
            elif path == '/':
                return {
                    'statusCode': 200,
                    'body': '{"message": "Welcome to the root directory", "available_endpoints": ["/api/post"]}',
                    'headers': {'Content-Type': 'application/json'},
                    'isBase64Encoded': False
                }
            else:
                return {
                    'statusCode': 404,
                    'body': '{"error": "Not Found"}',
                    'headers': {'Content-Type': 'application/json'},
                    'isBase64Encoded': False
                }
        elif method == 'POST' and path == '/api/post':
            return {
                'statusCode': 200,
                'body': '{"message": "Hello from POST /api/post"}',
                'headers': {'Content-Type': 'application/json'},
                'isBase64Encoded': False
            }
        else:
            return {
                'statusCode': 405,
                'body': '{"error": "Method Not Allowed"}',
                'headers': {'Content-Type': 'application/json'},
                'isBase64Encoded': False
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'{{"error": "Server error: {str(e)}"}}',
            'headers': {'Content-Type': 'application/json'},
            'isBase64Encoded': False
        }