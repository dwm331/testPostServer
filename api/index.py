def handler(event, context):
    method = event.get('httpMethod')
    path = event.get('path', '')

    # 處理 GET 請求
    if method == 'GET':
        if path == '/api/post':
            return {
                'statusCode': 200,
                'body': '{"message": "This is a GET response from /api/post"}',
                'headers': {'Content-Type': 'application/json'}
            }
        elif path == '/':
            return {
                'statusCode': 200,
                'body': '{"message": "Welcome to the root directory", "available_endpoints": ["/api/post"]}',
                'headers': {'Content-Type': 'application/json'}
            }
        else:
            return {
                'statusCode': 404,
                'body': '{"error": "Not Found"}',
                'headers': {'Content-Type': 'application/json'}
            }

    # 處理 POST 請求
    elif method == 'POST' and path == '/api/post':
        return {
            'statusCode': 200,
            'body': '{"message": "Hello from POST /api/post"}',
            'headers': {'Content-Type': 'application/json'}
        }

    # 其他情況
    else:
        return {
            'statusCode': 405,
            'body': '{"error": "Method Not Allowed"}',
            'headers': {'Content-Type': 'application/json'}
        }