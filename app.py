from flask import Flask, request, jsonify
from main import calculate_probability

app = Flask(__name__)

@app.route('/probability', methods=['GET'])
def get_probability():
    k = request.headers.get('k')
    if k is None:
        probabilities = calculate_probability(99)
    else:
        probabilities = calculate_probability(int(k))
    return jsonify(probabilities)

if __name__ == '__main__':
    app.run(debug=True)