from flask import Flask, request, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)
CORS(app)

# Test
@app.route('/submit', methods=['POST'])
def submit_text():
    data = request.json  # Get JSON data from request
    text = data.get("finalText")  # Extract text field content
    print("Received text:", text)  # Print in Flask console
    return jsonify({"message": "Text received!", "received_text": text})  # Send response

if __name__ == '__main__':
    app.run(debug=True)
