import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def handle_post():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'No data provided or invalid JSON format'}), 400
    return jsonify({
        'received_data': data,
        'message': 'Data received successfully'
    }), 200

# Vercel 無伺服器入口點
def handler(event, context):
    from werkzeug.wrappers import Request, Response
    from werkzeug.serving import run_simple
    from flask import make_response

    # 將 Vercel 事件轉換為 WSGI 請求
    environ = {
        'REQUEST_METHOD': event['httpMethod'],
        'PATH_INFO': event['path'],
        'QUERY_STRING': event.get('queryString', ''),
        'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
        'wsgi.input': event.get('body', b''),
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'REMOTE_ADDR': event.get('headers', {}).get('x-forwarded-for', ''),
    }

    # 處理請求並返回響應
    with Request(environ) as req:
        response = app(req)
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)