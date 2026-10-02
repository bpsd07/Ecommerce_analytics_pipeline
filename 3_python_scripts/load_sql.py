import pandas as pd
import sqlite3

df = pd.read_csv('../2_cleaned_data/clean_superstore.csv')

conn = sqlite3.connect('../4_sql_dbs/ecommerce.db')

df.to_sql('sales', conn, if_exists='replace', index=False)

query = """
SELECT category, SUM(sales) AS total_revenue 
FROM sales 
GROUP BY category
ORDER BY total_revenue DESC;
"""

print("Executing SQL Query...\n")
print(pd.read_sql(query, conn))

conn.close()