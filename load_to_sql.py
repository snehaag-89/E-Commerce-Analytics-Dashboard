import pandas as pd
import sqlite3

print("--- SQL LOADING PROCESS STARTED ---")

# 1. CSV File ko read karna jo humne pichle step me banayi thi
try:
    df = pd.read_csv('cleaned_ecommerce_sales.csv')
    print("1. Cleaned CSV file successfully read.")
except FileNotFoundError:
    print("Error: 'cleaned_ecommerce_sales.csv' nahi mili! Pehle pichla step run karo.")
    exit()

# 2. SQL Database se connect karna (Ye 'ecommerce.db' naam ki file auto-create kar dega)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()
print("2. Database connection established (ecommerce.db created).")

# 3. Dataframe ko SQL table me convert/insert karna
# table ka naam hum rakh rahe hain: 'sales_analytics'
df.to_sql('sales_analytics', conn, if_exists='replace', index=False)
print("3. Data successfully inserted into 'sales_analytics' table.")

# 4. Connection close karna
conn.close()
print("\nSuccess: Aapka data SQL database me load ho chuka hai!")