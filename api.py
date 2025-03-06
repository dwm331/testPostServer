from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def handle_post():
    # 獲取 POST 請求的數據
    data = request.get_json()
    
    # 檢查是否有數據
    if data is None:
        return jsonify({
            'error': 'No data provided or invalid JSON format'
        }), 400
    
    # 直接回傳接收到的數據
    return jsonify({
        'received_data': data,
        'message': 'Data received successfully'
    }), 200

# 錯誤處理
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)