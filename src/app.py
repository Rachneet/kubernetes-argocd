from flask import Flask, jsonify, request


app = Flask(__name__)

country_list = [
    'London',
    'Germany',
    'Netherlands'
]

@app.route('/')
def index():
    response_dict = {
        "message": "Welcome to FlaskApp 2"
    }
    return jsonify(response_dict)

@app.route('/names')
def countries():
    country_dict = {
        'countries': country_list,
        'total': len(country_list)
    }
    return jsonify(country_dict)


@app.route('/predict', methods=['GET'])
def prediction():
    task = request.args.get("task")
    text = request.args.get("paragraph")
    language = request.args.get("language")
    pred_dict = {
        'prediction': text
    }
    return jsonify(pred_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)