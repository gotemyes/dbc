import pandas as pd
import time
import math

from matplotlib import pyplot as plt
import seaborn as sns

stats = pd.read_csv('./data/dbc_stats - batting.csv')

stats['dismissed'] = stats.apply(lambda row: 0 if row['dismissal']=='not_out' else 1, axis = 1)

aa = stats[stats['controller']=='AA'].copy()
rm = stats[stats['controller']=='RM'].copy()

#print(aa.groupby('handedness').sum()[['runs','balls_faced','dismissed']])
#print(rm.groupby('handedness').sum()[['runs','balls_faced','dismissed']])

fig, ax = plt.subplots(nrows=2,ncols=3,figsize=(10,6))

startangle = 90
labeldistance  = 1

ax[0,0].pie(
    aa.groupby('handedness').sum()['runs'],
    autopct = '%0.1f%%',
    startangle = startangle
)
ax[1,0].pie(
    rm.groupby('handedness').sum()['runs'],
    autopct = '%0.1f%%',
    startangle = startangle
)

ax[0,1].pie(
    aa.groupby('handedness').sum()['dismissed'],
    autopct = '%0.1f%%',
    startangle = startangle
)
ax[1,1].pie(
    rm.groupby('handedness').sum()['dismissed'],
    autopct = '%0.1f%%',
    startangle = startangle
)

ax[0,2].pie(
    aa.groupby('handedness').sum()['balls_faced'],
    autopct = '%0.1f%%',
    startangle = startangle
)
ax[1,2].pie(
    rm.groupby('handedness').sum()['balls_faced'],
    autopct = '%0.1f%%',
    startangle = startangle
)

ax[0,0].set_ylabel('AA')
ax[1,0].set_ylabel('RM')
ax[0,0].set_title('Runs')
ax[0,1].set_title('Dismissals')
ax[0,2].set_title('Balls faced')


ax[1,1].legend(['left','right'],loc='upper center',bbox_to_anchor=(0.5, 1.25))

plt.suptitle('Left vs Right Composition')

if __name__ == '__main__':
    plt.savefig('./figures/leftVsRight.png')
    plt.show()
else:
    plt.savefig('./figures/leftVsRight.png')
    plt.close()
