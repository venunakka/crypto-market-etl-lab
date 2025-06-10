import psycopg2
from datetime import datetime
import json

# Load raw crypto data from JSON file
with open("crypto_data.json", "r") as f:
    all_crypto_data = json.load(f)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Venu5754$",
    host="localhost"
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS crypto_quotes (
    id SERIAL PRIMARY KEY,
    symbol TEXT,
    name TEXT,
    price NUMERIC,
    volume_24h NUMERIC,
    market_cap NUMERIC,
    percent_change_24h NUMERIC,
    timestamp TIMESTAMP
)
""")

# Insert data
for symbol in all_crypto_data:
    item = all_crypto_data[symbol]
    quote = item["quote"]["USD"]
    name = item["name"]
    price = quote["price"]
    volume_24h = quote["volume_24h"]
    market_cap = quote["market_cap"]
    percent_change_24h = quote["percent_change_24h"]
    timestamp = datetime.fromisoformat(quote["last_updated"].replace("Z", "+00:00"))

    cur.execute("""
        INSERT INTO crypto_quotes (symbol, name, price, volume_24h, market_cap, percent_change_24h, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (symbol, name, price, volume_24h, market_cap, percent_change_24h, timestamp))

    print(f"✅ Inserted {symbol}")

# Finalize
conn.commit()
conn.close()
print("✅ All data inserted into PostgreSQL")
