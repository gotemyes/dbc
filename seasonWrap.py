import pandas as pd
import numpy as np
import time
import math

from matplotlib import pyplot as plt
import seaborn as sns

import data.teamDict as td


statsBowling = pd.read_csv('./data/dbc_stats - bowling.csv')
statsBatting = pd.read_csv('./data/dbc_stats - batting.csv')
### team
def runs_team():

    totals = statsBatting[statsBatting['season']==1].groupby('opponent').sum().sort_values('gameID')
    totals['gameID'] = totals['gameID']/len(totals)

    plt.figure()
    ax = plt.subplot()
    plt.plot(totals['gameID'],totals['runs'],marker = 'o')

    ax.set_xticks(range(1,len(totals)+1))
    ax.set_xticklabels([td.teamCodes[el] for el in totals.index.tolist()],rotation=30)

def econ_team():

    bowlColumns =['country','overs']
    batColumns = ['opponent','runs','gameID']

    totalsBowl = statsBowling[statsBowling['season']==1].groupby('country').sum().reset_index()[bowlColumns]

    totalsBat = statsBatting[statsBatting['season']==1].groupby('opponent').sum().sort_values('gameID').reset_index()[batColumns]
    totalsBat['gameID'] = totalsBat['gameID']/len(totalsBat)

    totals = totalsBat.merge(totalsBowl,left_on='opponent',right_on='country').drop(columns=['country'])
    totals['balls'] = -4*np.floor(totals['overs'])+10*totals['overs']
    totals['econ'] = totals['runs']/totals['balls']*6

    plt.figure()
    ax = plt.subplot()
    plt.plot(totals['gameID'],totals['econ'],marker = 'o')

    ax.set_xticks(range(1,len(totals)+1))
    ax.set_xticklabels([td.teamCodes[el] for el in totals['opponent']],rotation=30)

def pct_boundary_team():

    batColumns = ['opponent','runs','gameID','fours','sixes']

    totalsBat = statsBatting[statsBatting['season']==1].groupby('opponent').sum().sort_values('gameID').reset_index()[batColumns]
    totalsBat['gameID'] = totalsBat['gameID']/len(totalsBat)

    totalsBat['runs_from_boundaries'] = totalsBat['fours']*4+totalsBat['sixes']*6
    totalsBat['pct_runs_from_boundaries'] = totalsBat['runs_from_boundaries']/totalsBat['runs']

    plt.figure()
    ax = plt.subplot()
    plt.plot(totalsBat['gameID'],totalsBat['pct_runs_from_boundaries'],marker = 'o')

    ax.set_xticks(range(1,len(totalsBat)+1))
    ax.set_xticklabels([td.teamCodes[el] for el in totalsBat['opponent']],rotation=30)

def overs_team():

    bowlColumns =['country','overs']
    batColumns = ['opponent','runs','gameID']

    totalsBowl = statsBowling[statsBowling['season']==1].groupby('country').sum().reset_index()[bowlColumns]

    totalsBat = statsBatting[statsBatting['season']==1].groupby('opponent').sum().sort_values('gameID').reset_index()[batColumns]
    totalsBat['gameID'] = totalsBat['gameID']/len(totalsBat)

    totals = totalsBat.merge(totalsBowl,left_on='opponent',right_on='country').drop(columns=['country'])

    totals['oversTrue'] = np.floor(totals['overs'])+(totals['overs']-np.floor(totals['overs']))*10/6

    plt.figure()
    ax = plt.subplot()
    plt.plot(totals['gameID'],totals['oversTrue'],marker = 'o')

    ax.set_xticks(range(1,len(totals)+1))
    ax.set_xticklabels([td.teamCodes[el] for el in totals['opponent']],rotation=30)

### players
def runs_players(extras=False):
    totals = statsBatting[statsBatting['season']==1].groupby('player').sum().sort_values('runs').reset_index()
    totals['gameID'] = totals['gameID']/len(totals)

    if not extras:
        totals = totals[totals['player']!='Extras']


    fig = plt.figure()
    ax = plt.subplot()
    plt.barh(range(len(totals)),totals['runs'],color='r')

    ax.axis('off')

    for i, v in enumerate(totals['runs']):
        ax.text(v + 3, i-0.15, str(v))

    for i,v in zip(range(11),totals['player']):
        ax.text(3, i-0.15, v, fontweight='bold')
    ax.set_title('Season 1 Runs')

def sr_players():
    totals = statsBatting[statsBatting['season']==1].groupby('player').sum().sort_values('runs').reset_index()
    totals['gameID'] = totals['gameID']/len(totals)
    totals = totals[totals['player']!='Extras']

    totals['sr'] = totals['runs']/totals['balls_faced']*100

    totals.sort_values('sr',inplace=True)


    fig = plt.figure()
    ax = plt.subplot()
    plt.barh(range(len(totals)),totals['sr'],color='r')

    ax.axis('off')

    for i, v in enumerate(totals['sr']):
        ax.text(v + 3, i-0.15, str(round(v,2)))

    for i,v in zip(range(11),totals['player']):
        ax.text(3, i-0.15, v, fontweight='bold')
    ax.set_title('Season 1 Strike Rate')

sr_players()

plt.show()
