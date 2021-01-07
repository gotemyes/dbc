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

players = stats.iloc[:11]['player'].values

stats['dismissed'] = stats.apply(lambda row: 0 if row['dismissal']=='not_out' else 1, axis = 1)

aa = stats[stats['controller']=='AA'].copy()
rm = stats[stats['controller']=='RM'].copy()

aaPlayers = aa.groupby('player').sum()
rmPlayers = rm.groupby('player').sum()


aa_runs = []
rm_runs = []
aa_balls_faced = []
rm_balls_faced = []
aa_fours = []
rm_fours = []
aa_count = []
rm_count = []

def zero_insert(key,df,col,list):
    try:
        list.append(df.loc[key][col])
    except KeyError:
        list.append(0)

for player in players:
    zero_insert(player,aaPlayers,'runs',aa_runs)
    zero_insert(player,rmPlayers,'runs',rm_runs)
    zero_insert(player,aaPlayers,'balls_faced',aa_balls_faced)
    zero_insert(player,rmPlayers,'balls_faced',rm_balls_faced)
    zero_insert(player,aaPlayers,'fours',aa_fours)
    zero_insert(player,rmPlayers,'fours',rm_fours)
    aa_count.append(aa[aa['player']==player].shape[0])
    rm_count.append(rm[rm['player']==player].shape[0])





fig, ax = plt.subplots(nrows=1,ncols=3,figsize=(12,6))

## player innings
ax[0].barh(
    y = range(len(players)),
    width = aa_count[::-1],
    color=aaCol)
ax[0].barh(
    y = range(len(players)),
    width = rm_count[::-1],
    left = aa_count[::-1],
    color=rmCol)
ax[0].set_yticks(range(len(players)))
ax[0].set_yticklabels(players[::-1])
ax[0].set_xlim((0,stats.groupby('gameID').count().shape[0]+1))
ax[0].set_xticks(range(stats.groupby('gameID').count().shape[0]+1))
ax[0].set_xlabel('Innings played')

## player runs
ax[1].barh(
    y = range(len(players)),
    width = aa_runs[::-1],
    color=aaCol)
ax[1].barh(
    y = range(len(players)),
    width = rm_runs[::-1],
    left = aa_runs[::-1],
    color=rmCol)
ax[1].set_yticklabels(['' for el in range(len(players))])
ax[1].set_xlabel('Runs scored')

## player balls faced
ax[2].barh(
    y = range(len(players)),
    width = aa_balls_faced[::-1],
    color=aaCol)
ax[2].barh(
    y = range(len(players)),
    width = rm_balls_faced[::-1],
    left = aa_balls_faced[::-1],
    color=rmCol)
ax[2].set_yticklabels(['' for el in range(len(players))])
ax[2].set_xlabel('Balls faced')
ax[2].legend(['AA','RM'])

plt.subplots_adjust(wspace=0)


ax[1].set_title('Player contributions')



if __name__ == '__main__':
    plt.savefig('./figures/playerBreakdown.png')
    plt.show()
else:
    plt.savefig('./figures/playerBreakdown.png')
    plt.close()
