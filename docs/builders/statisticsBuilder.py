import pandas as pd
import sys
sys.path.append('../../')

import data.teamDict as td

batData = pd.read_csv('../../data/dbc_stats - batting.csv')
bowlData = pd.read_csv('../../data/dbc_stats - bowling.csv')

### RUNS
totalRuns = batData.groupby('player').sum().reset_index().sort_values('runs',ascending=False)
runsTagList=[]
for ind, row in totalRuns.iterrows():
    if row['player']=='Extras':
        continue
    runsTagList.append(
        ' '*16+f"<tr>\n"+
        ' '*18+f"<td>{row['player']}</td>\n"+
        ' '*18+f"<td>{row['runs']}</td>\n"+
        ' '*16+f"<tr>")
totalRunsTag = '\n'.join(runsTagList)

aaRuns = batData[batData['controller']=='AA'].groupby('player').sum().reset_index().sort_values('runs',ascending=False)
runsTagList=[]
for ind, row in aaRuns.iterrows():
    if row['player']=='Extras':
        continue
    runsTagList.append(
        ' '*16+f"<tr>\n"+
        ' '*18+f"<td>{row['player']}</td>\n"+
        ' '*18+f"<td>{row['runs']}</td>\n"+
        ' '*16+f"<tr>")
aaRunsTag = '\n'.join(runsTagList)

rmRuns = batData[batData['controller']=='RM'].groupby('player').sum().reset_index().sort_values('runs',ascending=False)
runsTagList=[]
for ind, row in rmRuns.iterrows():
    if row['player']=='Extras':
        continue
    runsTagList.append(
        ' '*16+f"<tr>\n"+
        ' '*18+f"<td>{row['player']}</td>\n"+
        ' '*18+f"<td>{row['runs']}</td>\n"+
        ' '*16+f"<tr>")
rmRunsTag = '\n'.join(runsTagList)

### AVERAGE
totalRuns['innings'] = totalRuns.apply(lambda row:batData[batData['player']==row['player']].shape[0] ,axis=1)
totalRuns['not_outs'] = totalRuns.apply(
    lambda row:batData[(batData['player']==row['player'])&(batData['dismissal']=='not_out')].shape[0] ,axis=1)
totalRuns['average'] = totalRuns['runs']/(totalRuns['innings']-totalRuns['not_outs'])
totalRuns.sort_values('average',ascending=False,inplace=True)
totalRuns['average'] = ['{:.2f}'.format(el) for el in totalRuns['average']]
aveTagList = []
for ind, row in totalRuns.iterrows():
    if row['player']=='Extras':
        continue
    aveTagList.append(
        ' '*16+f"<tr>\n"+
        ' '*18+f"<td>{row['player']}</td>\n"+
        ' '*18+f"<td>{row['average']}</td>\n"+
        ' '*16+f"<tr>")
totalAveTag = '\n'.join(aveTagList)

aaRuns['innings'] = aaRuns.apply(lambda row:batData[(batData['controller']=='AA')&(batData['player']==row['player'])].shape[0] ,axis=1)
aaRuns['not_outs'] = aaRuns.apply(
    lambda row:batData[(batData['controller']=='AA')&(batData['player']==row['player'])&(batData['dismissal']=='not_out')].shape[0] ,axis=1)
aaRuns['average'] = aaRuns['runs']/(aaRuns['innings']-aaRuns['not_outs'])
aaRuns.sort_values('average',ascending=False,inplace=True)
aaRuns['average'] = ['{:.2f}'.format(el) for el in aaRuns['average']]
aveTagList = []
for ind, row in aaRuns.iterrows():
    if row['player']=='Extras':
        continue
    aveTagList.append(
        ' '*16+f"<tr>\n"+
        ' '*18+f"<td>{row['player']}</td>\n"+
        ' '*18+f"<td>{row['average']}</td>\n"+
        ' '*16+f"<tr>")
aaAveTag = '\n'.join(aveTagList)

rmRuns['innings'] = rmRuns.apply(lambda row:batData[(batData['controller']=='RM')&(batData['player']==row['player'])].shape[0] ,axis=1)
rmRuns['not_outs'] = rmRuns.apply(
    lambda row:batData[(batData['controller']=='RM')&(batData['player']==row['player'])&(batData['dismissal']=='not_out')].shape[0] ,axis=1)
rmRuns['average'] = rmRuns['runs']/(rmRuns['innings']-rmRuns['not_outs'])
rmRuns.sort_values('average',ascending=False,inplace=True)
rmRuns['average'] = ['{:.2f}'.format(el) for el in rmRuns['average']]
aveTagList = []
for ind, row in rmRuns.iterrows():
    if row['player']=='Extras':
        continue
    aveTagList.append(
        ' '*16+f"<tr>\n"+
        ' '*18+f"<td>{row['player']}</td>\n"+
        ' '*18+f"<td>{row['average']}</td>\n"+
        ' '*16+f"<tr>")
rmAveTag = '\n'.join(aveTagList)

### PLAYER HIGH SCORES
players = batData.sort_values(['gameID','position'],ascending=[False,True]).reset_index()['player'].unique()

hsTagList = []
for player in players:
    if player =='Extras':
        continue
    aaHS = batData[(batData['player']==player)&(batData['controller']=='AA')].groupby('player').max()['runs']
    rmHS = batData[(batData['player']==player)&(batData['controller']=='RM')].groupby('player').max()['runs']

    if len(aaHS.values)==0:
        aaHS = '-'
    else:
        aaHS = str(aaHS.values[0])

    if len(rmHS.values)==0:
        rmHS = '-'
    else:
        rmHS = str(rmHS.values[0])

    if rmHS=='-':
        aaHS='<strong>'+aaHS+'</strong>'
    elif aaHS=='-':
        rmHS='<strong>'+rmHS+'</strong>'
    elif int(aaHS)>int(rmHS):
        aaHS='<strong>'+aaHS+'</strong>'
    elif int(aaHS)<int(rmHS):
        rmHS='<strong>'+rmHS+'</strong>'
    else:
        aaHS='<strong>'+aaHS+'</strong>'
        rmHS='<strong>'+rmHS+'</strong>'

    hsTagList.append(
        ' '*10+f"<tr>\n"+
        ' '*12+f"<td>{player}</td>\n"+
        ' '*12+f"<td>{aaHS}</td>\n"+
        ' '*12+f"<td>{rmHS}</td>\n"+
        ' '*10+f"<tr>")
hsTag = '\n'.join(hsTagList)

### 10 BIGGEST PARTNERSHIPS

## list of partnerships
partnerships = batData[batData['player']!='Extras'].sort_values(['gameID','wicket'])[
    ['gameID','player','controller','fow','wicket','position','opponent','season']]

gameIDs = batData['gameID'].unique()


partnershipsList = []
for id in gameIDs:
    previousFOW = 0
    position1 = 1
    position2 = 2

    for ind, row in partnerships[partnerships['gameID']==id].iterrows():
        player1 = partnerships[(partnerships['gameID']==id)&(partnerships['position']==position1)]['player'].values[0]
        player2 = partnerships[(partnerships['gameID']==id)&(partnerships['position']==position2)]['player'].values[0]

        partnershipsList.append([row['gameID'],player1,  player2,  int(row['fow']-previousFOW),int(row['wicket']),row['opponent'],row['season']])
        previousFOW=row['fow']

        if row['controller']=='AA':
            position1 = max(position1,position2)+1
        if row['controller']=='RM':
            position2 = max(position1,position2)+1

        if (position1==12) | (position2 == 12):
            break

partnershipsCollated = pd.DataFrame(partnershipsList,columns = ['gameID','playerAA','playerRM','runs','wicket','opponent','season'])

## find top partnerships
top10Partnerships = partnershipsCollated.sort_values('runs',ascending=False).head(10)

top10PartnershipsTagList = []
for ind, row in top10Partnerships.iterrows():
    top10PartnershipsTagList.append(
        ' '*10+f"<tr>\n"+
        ' '*12+f"<td>{row['playerAA']}</td>\n"+
        ' '*12+f"<td>{row['playerRM']}</td>\n"+
        ' '*12+f"<td>{row['runs']}</td>\n"+
        ' '*12+f"<td>{row['wicket']}</td>\n"+
        ' '*12+f"<td>v {row['opponent']}, Season {row['season']}</td>\n"+
        ' '*10+f"<tr>")
top10PartnershipsTag = '\n'.join(top10PartnershipsTagList)

### TOP 10 BOWLING
i = 10
while i > 0:
    numAboveThres = bowlData[bowlData['wickets']>=i].shape[0]
    numAtThres = bowlData[bowlData['wickets']==i].shape[0]

    if numAboveThres > 10:
        break
    i-=1


topBowling = bowlData.sort_values(['wickets','runs'],ascending=[False,True]).head(numAboveThres-numAtThres)
topBowlingTagList = []
for ind, row in topBowling.iterrows():
    topBowlingTagList.append(
        ' '*10+f"<tr>\n"+
        ' '*12+f"<td>{row['bowler']}</td>\n"+
        ' '*12+f"<td>{row['wickets']}/{row['runs']}</td>\n"+
        ' '*12+f"<td>{row['country']}, Season {row['season']}</td>\n"+
        ' '*10+f"<tr>")
topBowlingTagList.append(
    ' '*10+f"<tr>\n"+
    ' '*12+f"<td colspan='3'>{numAtThres} bowlers with {i} wickets</td>\n"+
    ' '*10+f"<tr>")
topBowlingTag = '\n'.join(topBowlingTagList)



### CONSTRUCT HTML
statisticsHTML = f'''<!DOCTYPE html>
<html>
  <head>
    <title>Statistics</title>
    <link href="../css/style.css" rel="stylesheet" type="text/css">
    <link rel="shortcut icon" type="image/x-icon" href="../images/cricket.ico">
  </head>
  <body>
    <header>
      <h1>Statistics</h1>
      <nav>
        <ul>
          <li><a href="#runs" target="_self">Runs Scored</a></li>
          <li><a href="#average" target="_self">Batting Averages</a></li>
          <li><a href="#high_scores" target="_self">High Scores</a></li>
          <li><a href="#partnerships" target="_self">Top 10 Partnerships</a></li>
          <li><a href="#bowling" target="_self">Best Bowling</a></li>
        <ul>
      </nav>
      <h3><a href="../../index.html" target="_self">Back To Home</a></h3>
    </header>
    <main>
      <section>
        <h2 id="runs">Runs Scored</h2>
        <table class="organiser">
          <tr class="organiser">
            <td class="organiser">
              <table>
                <tr>
                  <th scope="col" colspan="2">Overall</th>
                </tr>
                <tr>
                  <th scope="col">Player</th>
                  <th scope="col">Runs</th>
                </tr>
{totalRunsTag}
              </table>
            </td>
            <td class="organiser">
              <table>
                <tr>
                  <th scope="col" colspan="2">Barbarooza</th>
                </tr>
                <tr>
                  <th scope="col">Player</th>
                  <th scope="col">Runs</th>
                </tr>
{aaRunsTag}
              </table>
            </td>
            <td class="organiser">
              <table>
                <tr>
                  <th scope="col" colspan="2">haast_schist</th>
                </tr>
                <tr>
                  <th scope="col">Player</th>
                  <th scope="col">Runs</th>
                </tr>
{rmRunsTag}
                </table>
              </tr>
            </table>
      </section>
      <section>
        <h2 id="average">Batting Average</h2>
        <table class="organiser">
          <tr class="organiser">
            <td class="organiser">
              <table>
                <tr>
                  <th scope="col" colspan="2">Overall</th>
                </tr>
                <tr>
                  <th scope="col">Player</th>
                  <th scope="col">Average</th>
                </tr>
{totalAveTag}
              </table>
            </td>
            <td class="organiser">
              <table>
                <tr>
                  <th scope="col" colspan="2">Barbarooza</th>
                </tr>
                <tr>
                  <th scope="col">Player</th>
                  <th scope="col">Average</th>
                </tr>
{aaAveTag}
              </table>
            </td>
            <td class="organiser">
              <table>
                <tr>
                  <th scope="col" colspan="2">haast_schist</th>
                </tr>
                <tr>
                  <th scope="col">Player</th>
                  <th scope="col">Average</th>
                </tr>
{rmAveTag}
                </table>
              </tr>
            </table>
      </section>
      <section>
        <h2 id="high_scores">Player High Scores</h2>
        <table>
          <tr>
            <th scope="col">Player</th>
            <th scope="col">Barbarooza</th>
            <th scope="col">haast_schist</th>
          </tr>
{hsTag}
          </table>
      </section>
      <section>
        <h2 id="partnerships">Top 10 Partnerships</h2>
        <table>
          <tr>
            <th scope="col">Barbarooza</th>
            <th scope="col">haast_schist</th>
            <th scope="col">Runs</th>
            <th scope="col">Wicket</th>
            <th scope="col">Match</th>
          </tr>
{top10PartnershipsTag}
          </table>
      </section>
      <section>
        <h2 id="bowling">Best Bowling</h2>
        <table>
          <tr>
            <th scope="col">Bowler</th>
            <th scope="col">Figures</th>
            <th scope="col">Match</th>
          </tr>
{topBowlingTag}
          </table>
      </section>
    </main>
  </body>
</html>
'''


html_file= open("../resources/pages/statistics.html","w")
html_file.write(statisticsHTML)
html_file.close()
