from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用 CORS

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_transactions')
def get_transactions():
    addresses = request.args.get('addresses', '')
    return jsonify({"message": f"Received addresses: {addresses}"})


if __name__ == '__main__':
    app.run(debug=True)
