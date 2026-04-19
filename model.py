import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("superstore.csv", encoding='latin1')

df = df[df["Profit"] > -100]

X = df[["Sales", "Discount"]]
y = df["Profit"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print("Model Accuracy (R^2):", score)
