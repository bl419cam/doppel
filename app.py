import random
import pickle
from flask import Flask, request, render_template, jsonify
<<<<<<< HEAD
from image_feature_extractor import ImageFeatureExtractor

=======
from model import Model

# Custom class to extract features - wm 2019.06.21
from image_feature_extractor import ImageFeatureExtractor

# Instantiate the extractor
extractor = ImageFeatureExtractor()

>>>>>>> 4d33cc7537ee897711f8b250c6c31a44c8c9ea1f
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
<<<<<<< HEAD
    extraction = ImageFeatureExtractor()
    features_for_web = extraction.transform([data['user_input']])
    prediction = model.predict(features_for_web)
    return jsonify({'prediction': prediction[0]})
=======
    
    # Pass URL to extractor to get features
    features = extractor([data['user_input']])
    
    # Predict on features
    prediction = model.predict(features)
    return jsonify({'prediction': prediction})
>>>>>>> 4d33cc7537ee897711f8b250c6c31a44c8c9ea1f

