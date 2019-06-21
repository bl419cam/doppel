import random
import pickle
from flask import Flask, request, render_template, jsonify
from model import Model

# Custom class to extract features - wm 2019.06.21
from image_feature_extractor import ImageFeatureExtractor

# Instantiate the extractor
extractor = ImageFeatureExtractor()

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
    
    # Pass URL to extractor to get features
    features = extractor([data['user_input']])
    
    # Predict on features
    prediction = model.predict(features)
    return jsonify({'prediction': prediction})

