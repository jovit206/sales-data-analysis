import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("superstore.csv", encoding='latin1')

# Preview
print(df.head())

# Total Sales
print("Total Sales:", df["Sales"].sum())

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

# Plot
region_sales.plot(kind='bar', title="Sales by Region")
plt.show()