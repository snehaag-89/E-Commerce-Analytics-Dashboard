import sqlite3
import pandas as pd

# Database se connect karenge
conn = sqlite3.connect('ecommerce.db')

print("==================================================")
print("          SQL DATA ANALYSIS REPORT                ")
print("==================================================")

# Query 1: Kaun sa shehar sabse zyada revenue generate kar raha hai?
print("\n🔥 1. TOP 5 PERFORMING CITIES BY TOTAL SALES")
q1 = """
SELECT City, 
       ROUND(SUM(TotalSales), 2) as TotalRevenue, 
       COUNT(OrderID) as TotalOrders
FROM sales_analytics
GROUP BY City
ORDER BY TotalRevenue DESC
LIMIT 5;
"""
print(pd.read_sql_query(q1, conn).to_string(index=False))


# Query 2: Kis mahine me sabse zyada sales hoti hai? (Sales Trend)
print("\n📈 2. MONTHLY SALES TREND (FIRST 5 MONTHS SAMPLE)")
q2 = """
SELECT strftime('%m', OrderDate) as Month, 
       ROUND(SUM(TotalSales), 2) as MonthlyRevenue
FROM sales_analytics
GROUP BY Month
ORDER BY Month
LIMIT 5;
"""
print(pd.read_sql_query(q2, conn).to_string(index=False))


# Query 3: Hamaare high-value customers kaun hain? (Jo bade khiladi hain)
print("\n👑 3. HIGH-VALUE CUSTOMERS (TOP 5 SPENDERS)")
q3 = """
SELECT CustomerID, 
       COUNT(OrderID) as TotalVisits, 
       ROUND(SUM(TotalSales), 2) as TotalSpent
FROM sales_analytics
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT 5;
"""
print(pd.read_sql_query(q3, conn).to_string(index=False))

# Connection close
conn.close()