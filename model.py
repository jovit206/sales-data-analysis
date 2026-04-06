import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("superstore.csv", encoding='latin1')

# Data Cleaning (remove outliers)
df = df[df["Profit"] > -100]

# Features & target
X = df[["Sales", "Discount"]]
y = df["Profit"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print("Model Accuracy (R^2):", score)
