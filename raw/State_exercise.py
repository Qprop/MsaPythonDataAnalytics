pop = pd.read_csv('data/state-population.csv')
areas = pd.read_csv('data/state-areas.csv')
abbrevs = pd.read_csv('data/state-abbrevs.csv')


merged = pd.merge(pop, abbrevs, how='outer',
                  left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', 1) # drop duplicate info
merged.head()


merged.isnull().any()


merged[merged['population'].isnull()].head()



merged.loc[merged['state'].isnull(), 'state/region'].unique()


merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
merged.isnull().any()



final = pd.merge(merged, areas, on='state', how='left')
final.head()


final.isnull().any()

final['state'][final['area (sq. mi)'].isnull()].unique()



final.dropna(inplace=True)
final.head()





data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']


density.sort_values(ascending=False, inplace=True)
density.head()

density.tail()