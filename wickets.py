import pandas as pd
import time
import math

from matplotlib import pyplot as plt
import seaborn as sns

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
aaCol = colors[0]
rmCol = colors[1]

statsBowling = pd.read_csv('./data/dbc_stats - bowling.csv')
statsBatting = pd.read_csv('./data/dbc_stats - batting.csv').merge(statsBowling[['bowler','style']],on = 'bowler')


aa = statsBatting[statsBatting['controller']=='AA'].copy()
rm = statsBatting[statsBatting['controller']=='RM'].copy()
