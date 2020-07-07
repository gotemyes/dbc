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

fig, ax = plt.subplots(1,1)
## career runs
plt.plot(
    range(aa.shape[0]),
    aa['cumRuns'],
    color=aaCol)
plt.plot(
    range(rm.shape[0]),
    rm['cumRuns'],
    color=rmCol)
ax.set_xlabel('Innings')
ax.set_ylabel('Runs')
ax.set_title('Career Runs (Current Inset)')
plt.plot(
    aa.shape[0]-1,
    aa['cumRuns'].values[-1],
    marker = 'o',
    color = aaCol)
plt.plot(
    rm.shape[0]-1,
    rm['cumRuns'].values[-1],
    marker = 'o',
    color = rmCol)
plt.legend([
    'AA: {}'.format(aa['cumRuns'].values[-1]),
    'RM: {}'.format(rm['cumRuns'].values[-1])])

plt.savefig('./figures/runProgression')
