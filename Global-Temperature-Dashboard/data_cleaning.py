import pandas as pd

url = "https://datahub.io/core/global-temp/_r/-/data/monthly.csv"
df = pd.read_csv(url)

df['Year'] = pd.to_datetime(df['Year'])
df['YearOnly'] = df['Year'].dt.year


df = df.dropna()
print(df)
