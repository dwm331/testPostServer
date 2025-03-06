def handler(event, context):
    return {
        'statusCode': 200,
        'body': '{"message": "Hello from Vercel!"}',
        'headers': {'Content-Type': 'application/json'}
    }