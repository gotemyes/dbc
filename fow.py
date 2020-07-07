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

fowArray = []
for opponent in stats['opponent'].unique():
    #fowArray.append([opponent]+stats[stats['opponent']==opponent].sort_values('fow')['fow'].dropna().values.tolist())
    for score, wicket in zip(stats[stats['opponent']==opponent].sort_values('fow')['fow'].dropna().values,range(1,11)):
        fowArray.append([opponent,score,wicket])

#fowDF = pd.DataFrame(data = fowArray, columns = ['opponent']+['fow'+str(num) for num in range(1,11)])
fowDF = pd.DataFrame(data = fowArray, columns = ['opponent','score','wicket'])
fowDF['partnership'] = fowDF.apply(
    lambda row: row['score'] - fowDF[
        (fowDF['opponent']==row['opponent'])&
        (fowDF['wicket']==row['wicket']-1)]['score'].values[0] if row['wicket']>1 else row['score'], axis = 1)

fig, ax = plt.subplots(nrows=2,ncols=1,figsize=(10,8))



sns.boxplot(
    x = 'wicket',
    y = 'score',
    data = fowDF,
    ax = ax[0]
)


sns.boxplot(
    x = 'wicket',
    y = 'partnership',
    data = fowDF,
    ax = ax[1]
)

fig.subplots_adjust(hspace = 0)
ax[0].set_ylabel('Fall of Wicket')
ax[1].set_ylabel('Partnership')
ax[0].set_xlabel('')
ax[1].set_xlabel('Wicket')
ax[0].set_xticks([])
ax[0].set_title('Partnership and FOW Distributions')


if __name__ == '__main__':
    plt.show()
else:
    plt.savefig('./figures/fowPartnerships.png')
    plt.close()
