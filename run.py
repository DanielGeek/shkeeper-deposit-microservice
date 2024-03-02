from flask import Flask, request, jsonify, abort

app = Flask(__name__)

API_KEY_EXPECTED = ''

@app.route('/payment-notification', methods=['POST'])
def payment_notification():
    # Authenticate the incoming request
    api_key_received = request.headers.get('X-Shkeeper-API-Key')
    if api_key_received != API_KEY_EXPECTED:
        abort(401)  # Unauthorized access

    print(f"api_key_received {api_key_received}")
    # Parse the JSON data received in the request body
    data = request.json
    external_id = data.get('external_id')
    crypto = data.get('crypto')
    fiat = data.get('fiat')
    balance_fiat = data.get('balance_fiat')
    balance_crypto = data.get('balance_crypto')
    fee_percent = data.get('fee_percent')
    paid = data.get('paid')
    transactions = data.get('transactions')

    # Here you would add your code to process the payment
    # Update your system with the payment information

    # Acknowledge the receipt of the payment notification
    print(api_key_received)
    return jsonify({'message': 'Payment notification received successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
