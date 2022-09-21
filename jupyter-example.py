import pandas as pd

apps_data = pd.read_csv('AppleStore.csv')

first_rows = apps_data.head()

print (first_rows)