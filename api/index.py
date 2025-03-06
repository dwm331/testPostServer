from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'Welcome to the root directory',
        'available_endpoints': ['/api/post']
    })

@app.route('/api/post', methods=['GET'])
def get_post():
    return jsonify({
        'message': 'This is a GET response from /api/post'
    })

@app.route('/api/post', methods=['POST'])
def post_post():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'Invalid JSON format'}), 400
    return jsonify({
        'received_data': data,
        'message': 'Data received successfully'
    })

# Vercel 會自動處理 WSGI 入口點
if __name__ == '__main__':
    app.run()