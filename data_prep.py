import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. FAke Data Generation (1000 rows)
np.random.seed(42)
rows = 1000

categories = ['Electronics', 'Clothing', 'Home Decor', 'Books']
cities = ['Delhi', 'Mumbai', 'Bangalore', 'Varanasi', 'Pune']
payments = ['UPI', 'Credit Card', 'Debit Card', 'COD']

data = {
    'OrderID': range(1001, 1001 + rows),
    'OrderDate': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(rows)],
    'ProductID': [f"PROD{np.random.randint(100, 120)}" for _ in range(rows)],
    'Category': np.random.choice(categories, size=rows, p=[0.3, 0.4, 0.2, 0.1]),
    'Price': np.random.uniform(10, 500, size=rows).round(2),
    'Quantity': np.random.randint(1, 5, size=rows),
    'CustomerID': [f"CUST{np.random.randint(500, 600)}" for _ in range(rows)],
    'PaymentMethod': np.random.choice(payments, size=rows),
    'City': np.random.choice(cities, size=rows)
}

df = pd.DataFrame(data)

# Jaanbujhkar data me gadbadi daal rahe hain clean karne ke liye
df.loc[df.sample(20).index, 'Price'] = np.nan  # Missing values
df = pd.concat([df, df.sample(10)], ignore_index=True)  # Duplicates

print("--- RAW DATA GENERATED ---")
print("Original Shape (With Duplicates & NaNs):", df.shape)

# 2. DATA CLEANING
# Duplicates hatana
df.drop_duplicates(inplace=True)

# Missing Price ko uski Category ke median se fill karna
df['Price'] = df.groupby('Category')['Price'].transform(lambda x: x.fillna(x.median()))

# Total Sales calculate karna (Price * Quantity)
df['TotalSales'] = df['Price'] * df['Quantity']

print("\n--- DATA CLEANED ---")
print("Cleaned Shape:", df.shape)

# CSV me save karna
df.to_csv('cleaned_ecommerce_sales.csv', index=False)
print("\nSuccess: 'cleaned_ecommerce_sales.csv' file aapke folder me ban gayi hai!")