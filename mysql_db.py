import pandas as pd
import mysql.connector

df = pd.read_csv("superstore.csv", encoding='latin1')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="sales_db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_data (
    Order_ID VARCHAR(50),
    Region VARCHAR(50),
    Category VARCHAR(50),
    Sales FLOAT,
    Quantity INT,
    Discount FLOAT,
    Profit FLOAT
)
""")

for i, row in df.head(500).iterrows():
    cursor.execute("""
    INSERT INTO sales_data 
    (Order_ID, Region, Category, Sales, Quantity, Discount, Profit)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        str(row["Order ID"]),
        row["Region"],
        row["Category"],
        float(row["Sales"]),
        int(row["Quantity"]),
        float(row["Discount"]),
        float(row["Profit"])
    ))

conn.commit()
print("Data inserted into MySQL!")

cursor.execute("""
SELECT Region, SUM(Sales)
FROM sales_data
GROUP BY Region
""")

print("\nSQL Result:")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()