import pandas as pd

df = pd.read_csv('power_plants_germany.csv')
print(df.head())
print(df.columns)

capacity_by_fuel = df.groupby('energy_source')['capacity_net_bnetza'].sum().sort_values(ascending=False)
print(capacity_by_fuel)

import matplotlib.pyplot as plt

capacity_by_fuel.plot(kind='bar')
plt.title('Installed Capacity by Energy Source in Germany in 2020')
plt.ylabel('MW')
plt.show()
