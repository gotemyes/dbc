import pandas as pd
import time
import math

from matplotlib import pyplot as plt
import seaborn as sns

stats = pd.read_csv('./data/dbc_stats - batting.csv')


aa = stats[stats['controller']=='AA'].copy()
rm = stats[stats['controller']=='RM'].copy()

aa.reindex()
rm.reindex()

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

aaCol = colors[0]
rmCol = colors[1]


aa['cumRuns'] = aa['runs'].cumsum()
rm['cumRuns'] = rm['runs'].cumsum()

aa['dismissed'] = aa.apply(lambda row: 0 if row['dismissal']=='not_out' else 1, axis = 1)
rm['dismissed'] = rm.apply(lambda row: 0 if row['dismissal']=='not_out' else 1, axis = 1)

aa['totalDismissals'] = aa['dismissed'].cumsum()
rm['totalDismissals'] = rm['dismissed'].cumsum()

aa['average'] = aa['cumRuns']/aa['totalDismissals']
rm['average'] = rm['cumRuns']/rm['totalDismissals']

fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(10,8))


## career manhattan
width = 0.5
ax[0,0].bar(
    x = [el - width/2 for el in range(aa.shape[0])],
    height = aa['runs'],
    width = width,
    color=aaCol)
ax[0,0].bar(
    x = [el + width/2 for el in range(rm.shape[0])],
    height = rm['runs'],
    width = width,
    color=rmCol)
ax[0,0].set_xlabel('Innings')
ax[0,0].set_ylabel('Runs')
ax[0,0].legend(['AA','RM'])
ax[0,0].set_title('Career Manhattan')

## career runs
ax[0,1].plot(
    range(aa.shape[0]),
    aa['cumRuns'],
    color=aaCol)
ax[0,1].plot(
    range(rm.shape[0]),
    rm['cumRuns'],
    color=rmCol)
ax[0,1].set_xlabel('Innings')
ax[0,1].set_ylabel('Runs')
ax[0,1].set_title('Career Runs (Current Inset)')
ax[0,1].plot(
    aa.shape[0]-1,
    aa['cumRuns'].values[-1],
    marker = 'o',
    color = aaCol)
ax[0,1].plot(
    rm.shape[0]-1,
    rm['cumRuns'].values[-1],
    marker = 'o',
    color = rmCol)
ax[0,1].legend([
    'AA: {}'.format(aa['cumRuns'].values[-1]),
    'RM: {}'.format(rm['cumRuns'].values[-1])])

## career averages
ax[1,0].plot(
    range(aa.shape[0]),
    aa['average'],
    color=aaCol)
ax[1,0].plot(
    range(rm.shape[0]),
    rm['average'],
    color=rmCol)
ax[1,0].set_xlabel('Innings')
ax[1,0].set_ylabel('Average Runs')
ax[1,0].set_title('Average Runs (Current Inset)')
ax[1,0].plot(
    aa.shape[0]-1,
    round(aa['average'].values[-1],2),
    marker = 'o',
    color = aaCol)
ax[1,0].plot(
    rm.shape[0]-1,
    round(rm['average'].values[-1],2),
    marker = 'o',
    color = rmCol)
ax[1,0].legend([
    'AA: {}'.format(round(aa['average'].values[-1],2)),
    'RM: {}'.format(round(rm['average'].values[-1],2))])


## distribution of innings
binSize = 20
maxBin = int(math.ceil(stats['runs'].max()/binSize)*binSize)
numBins = round(maxBin/binSize)

ax[1,1].hist(
    aa['runs'],
    density = True,
    bins = numBins,
    range = (0,maxBin),
    histtype='step',
    linewidth=2,
    color=aaCol)
ax[1,1].hist(
    rm['runs'],
    density = True,
    bins = numBins,
    range = (0,maxBin),
    histtype='step',
    linewidth=2,
    color=rmCol)
ax[1,1].set_xlabel('Runs')
ax[1,1].set_ylabel('% of Innings')
ax[1,1].set_yticklabels([round(el*100,1) for el in ax[1,1].get_yticks()])
ax[1,1].set_title('Innings Distribution')

plt.subplots_adjust(wspace=0.3,hspace=0.3)

if __name__ == '__main__':
    plt.savefig('./figures/careerSummary.png')
    plt.show()
else:
    plt.savefig('./figures/careerSummary.png')
    plt.close()
