import random
import pickle
from flask import Flask, request, render_template, jsonify
from model import Model

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__, static_url_path="")

@app.route('/') 
def index():
    """Return the main page."""
    return render_template('doppel.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a character image."""
    data = request.json
    prediction = model.predict([data['user_input']])
    return jsonify({'prediction': prediction})

