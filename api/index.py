from flask import Flask, request, jsonify

app = Flask(__name__)

# 定義 POST API
@app.route('/api/post', methods=['POST'])
def handle_post():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'No data provided or invalid JSON format'}), 400
    return jsonify({
        'received_data': data,
        'message': 'Data received successfully'
    }), 200

# Vercel 需要的入口點
def handler(request):
    from wsgi import wsgi_handler
    return wsgi_handler(app, request)

# 如果直接運行（本地測試）
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)