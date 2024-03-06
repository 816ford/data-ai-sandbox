import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/baby_names/merged.csv')

grant = df[df['Name'] == 'Kwon']

grant_by_year = grant.groupby('Year').sum()

plt.plot(grant_by_year.index, grant_by_year['Count'])
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Grant by Year')
plt.show()