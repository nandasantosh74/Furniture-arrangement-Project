import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset/furniture_data.csv")

# Features & labels
X = df[["room_width", "room_height", "num_furniture"]].values
y = df.iloc[:, 3:].values  # All position values (x1, y1, x2, y2...)

# Normalize the dataset for better learning
X = X / np.max(X, axis=0)  # Scale room dimensions
if y.shape[1] > 0:
    y = y / np.max(y, axis=0)  # Scale furniture positions

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model with improved architecture
model = keras.Sequential([
    keras.layers.Dense(32, activation="relu", input_shape=(3,)),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(y.shape[1])  # Output layer matches position count
])

# Compile model with better loss function & optimizer
model.compile(optimizer="adam", loss="mse", metrics=["mae"])

# Train model with more epochs & batch normalization
model.fit(X_train, y_train, epochs=150, batch_size=16, validation_data=(X_test, y_test))

# Save model
model.save("furniture_model.keras")

print("✅ Model trained & saved as 'furniture_model.keras'")
