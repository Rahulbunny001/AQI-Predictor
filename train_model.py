import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Replace this with the path to your AQI dataset (e.g., 'aqi_data.csv')
# Ensure your dataset has features and a target column for AQI prediction
data = pd.read_csv('aqi_data.csv')

# Example data preparation (adjust according to your dataset)
# Assume 'feature1', 'feature2', 'feature3' are feature columns
# and 'target' is the AQI value we want to predict.
X = data[['temperature', 'humidity', 'wind_speed']]  # Features
y = data['target']  # Target (AQI values)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestRegressor model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'aqi_model.pkl')

print("Model trained and saved as 'aqi_model.pkl'")
