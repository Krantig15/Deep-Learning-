# -*- coding: utf-8 -*-
"""iris_2class.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kSOBGwfUQlK4C1pE2m_G3jBm-xSss2w-
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features (4 features)
y = iris.target  # Target classes (3 classes: 0, 1, 2)

# Select only two classes (linearly separable) and two features for simplicity
X = X[y != 2, :2]  # Use features 0 and 1, and exclude class 2
y = y[y != 2]      # Use only classes 0 and 1

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data for better gradient updates
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize weights and bias
w = np.zeros(2)  # Two weights for two features
b = 0.0          # Bias

# Step activation function
def step_activation(z):
    return 1 if z >= 0 else 0

# Hyperparameters
learning_rate = 0.1
epochs = 10

# Training loop
for epoch in range(epochs):
    total_loss = 0  # Track loss for logging

    for i in range(X_train.shape[0]):  # Loop through each training example
        x_i = X_train[i]  # Single input pair (e.g., [feature1, feature2])
        y_i = y_train[i]  # Corresponding target output (0 or 1)

        # Forward pass
        z = np.dot(w, x_i) + b  # Linear combination
        y_pred = step_activation(z)  # Step activation function

        # Compute error
        error = y_i - y_pred  # Error: (target - predicted)
        total_loss += abs(error)  # Accumulate absolute error for logging

        # Backward pass (Weight and bias update)
        dw = learning_rate * error * x_i  # Gradient w.r.t weights
        db = learning_rate * error       # Gradient w.r.t bias

        # Update weights and bias
        w += dw
        b += db

    # Print loss for the epoch
    print(f"Epoch {epoch + 1}/{epochs}, Total Error: {total_loss}")

# Final weights and bias
print("Final weights:", w)
print("Final bias:", b)

# Testing the model
print("\nTesting on test set:")
correct_predictions = 0
for i in range(X_test.shape[0]):
    x_i = X_test[i]
    y_i = y_test[i]
    z = np.dot(w, x_i) + b
    y_pred = step_activation(z)
    print(f"Input: {x_i}, Predicted: {y_pred}, Actual: {y_i}")
    if y_pred == y_i:
        correct_predictions += 1

# Accuracy
accuracy = correct_predictions / X_test.shape[0]
print(f"Accuracy: {accuracy * 100:.2f}%")