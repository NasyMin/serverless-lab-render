from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Serverless! 🚀\n", 200, {'Content-Type': 'text/plain'}

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        "status": "received",
        "you_sent": data,
        "length": len(str(data)) if data else 0
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render подставит свой порт
    app.run(host='0.0.0.0', port=port)
