import pandas as pd 

df = pd.read_csv("mubawab_marrakech.csv")
numeric_prices= pd.to_numeric(df['Price'],errors='coerce')


avg_price = numeric_prices.mean()
max_price = numeric_prices.max()
min_price = numeric_prices.min()
total_ads = len(df)


print("=" * 40)
print("📊 Summary of Marrakech real estate analysis (Mubawab)")
print("=" * 40)
print(f"Total aggregated ads {total_ads}")
print(f"Avrage rental price {avg_price:,.2f} DH")
print(f"Highest rental price: {max_price:,.0f} DH")
print(f"Cheapest rental price:{min_price:,.0f}DH")
print("=" * 40)

