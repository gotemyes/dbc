import pandas as pd
import time
import math

from matplotlib import pyplot as plt
import seaborn as sns

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
aaCol = colors[0]
rmCol = colors[1]

stats = pd.read_csv('./data/dbc_stats - batting.csv')

stats['dismissed'] = stats.apply(lambda row: 0 if row['dismissal']=='not_out' else 1, axis = 1)



aaDismissals = 0
rmDismissals = 0
for ind, row in stats.sort_values(['gameID','fow']).dropna().iterrows():
    if row['controller']=='AA':
        aaDismissals+=1
    elif row['controller']=='RM':
        rmDismissals+=1
    stats.at[ind,'totalDismissalsAA'] = aaDismissals
    stats.at[ind,'totalDismissalsRM'] = rmDismissals



aa = stats[stats['controller']=='AA'].copy()
rm = stats[stats['controller']=='RM'].copy()


orderedDismissals = stats.sort_values(['gameID','fow']).dropna().copy()
orderedDismissals.reset_index(inplace=True)

orderedDismissals.plot(
    y = 'totalDismissalsAA',
    marker = 'o',
    color = aaCol)
orderedDismissals.plot(
    y = 'totalDismissalsRM',
    ax = plt.gca(),
    marker = 'o',
    color = rmCol)
plt.legend(['AA','RM'])


plt.show()
