from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS for handling cross-origin requests
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Load the trained model
model = joblib.load('aqi_model.pkl')  # Ensure the model is in the same directory

# The actual features your model expects
FEATURES = ['temperature', 'humidity', 'wind_speed']  # Replace with actual features

@app.route('/api/predict', methods=['POST'])
def predict_aqi():
    # Get the JSON data sent in the POST request
    data = request.get_json()

    # Ensure the data contains the required features
    input_data = [data[feature] for feature in FEATURES]

    # Convert input data to a pandas DataFrame (needed for prediction)
    input_df = pd.DataFrame([input_data], columns=FEATURES)

    # Make the prediction
    prediction = model.predict(input_df)

    # Return the prediction as JSON
    return jsonify({'predicted_aqi': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
