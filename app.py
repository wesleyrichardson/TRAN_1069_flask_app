from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    try:
        with app.open_resource('static/data.json') as f:
            data = json.load(f)
            return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "JSON File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 500


if __name__ == '__main__':
    app.run(debug=True)