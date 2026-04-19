import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superstore.csv", encoding='latin1')

print(df.head())

print("Total Sales:", df["Sales"].sum())

region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind='bar', title="Sales by Region")
plt.show()