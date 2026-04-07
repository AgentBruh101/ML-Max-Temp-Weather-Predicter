import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
# Replace 'your_dataset.csv' with the path to your weather dataset
# The dataset should have features related to weather and a target temperature column

data = pd.read_csv('your_dataset.csv')

# Preprocess the data
# Assuming 'Temperature' is the target variable and the rest are features
X = data.drop('Temperature', axis=1)
y = data['Temperature']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')