import pandas as pd

df = pd.read_csv('../1_raw_data/superstore.csv', encoding='windows-1252')

df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')

df = df.drop_duplicates()
df = df.dropna()

df.to_csv('../2_cleaned_data/clean_superstore.csv', index=False)