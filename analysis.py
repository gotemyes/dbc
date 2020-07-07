import pandas as pd
import time

from matplotlib import pyplot as plt



stats = pd.read_csv('./data/dbc_stats - batting.csv')


leftRM = stats[
    (stats['handedness']=='left')&
    (stats['controller']=='RM')
].copy()
leftAA = stats[
    (stats['handedness']=='left')&
    (stats['controller']=='AA')
].copy()
rightRM = stats[
    (stats['handedness']=='right')&
    (stats['controller']=='RM')
].copy()
rightAA = stats[
    (stats['handedness']=='right')&
    (stats['controller']=='AA')
].copy()

## averages
print(
    "RM average LH",
    round(leftRM['runs'].sum()/leftRM[~leftRM['dismissal'].isnull()]['runs'].count(),2))
print(
    "AA average LH",
    round(leftAA['runs'].sum()/leftAA[~leftAA['dismissal'].isnull()]['runs'].count(),2))
print(
    "RM average RH",
    round(rightRM['runs'].sum()/rightRM[~rightRM['dismissal'].isnull()]['runs'].count(),2))
print(
    "AA average RH",
    round(rightAA['runs'].sum()/rightAA[~rightAA['dismissal'].isnull()]['runs'].count(),2))

## strike rates
print(
    "RM SR LH",
    round(100*leftRM['runs'].sum()/leftRM['balls_faced'].sum(),2))
print(
    "AA SR LH",
    round(100*leftAA['runs'].sum()/leftAA['balls_faced'].sum(),2))
print(
    "RM SR RH",
    round(100*rightRM['runs'].sum()/rightRM['balls_faced'].sum(),2))
print(
    "AA SR RH",
    round(100*rightAA['runs'].sum()/rightAA['balls_faced'].sum(),2))


stats[stats['controller']=='AA'].plot(kind='scatter',x='runs',y='sr',color='b')
stats[stats['controller']=='RM'].plot(kind='scatter',x='runs',y='sr',ax=plt.gca(),color='r')
plt.legend(['AA','RR'])



plt.show()
