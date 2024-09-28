from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"Hello World Python v2\"}"

from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to convert USD to EUR
def convert_currency(amount, rate=0.85):
    return amount * rate

# Main route (home)
@app.route('/', methods=['GET'])
def home():
    return "Currency Converter API - Convert USD to EUR"

# Route for currency conversion
@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()

    # Handle if 'amount' is not provided
    try:
        amount = float(data['amount'])
    except KeyError:
        return jsonify({"error": "Amount not provided"}), 400

    # Convert USD to EUR
    converted_amount = convert_currency(amount)
    return jsonify({"usd": amount, "eur": converted_amount})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
