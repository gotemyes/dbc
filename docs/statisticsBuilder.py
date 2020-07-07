import pandas as pd
import sys
sys.path.append('../')

import data.teamDict as td

batData = pd.read_csv('../data/dbc_stats - batting.csv')
bowlData = pd.read_csv('../data/dbc_stats - batting.csv')

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


### CONSTRUCT HTML
statisticsHTML = f'''<!DOCTYPE html>
<html>
  <head>
    <title>Statistics</title>
    <link href="style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <header>
      <h1>Statistics</h1>
      <nav>
        <ul>
          <li><a href="#runs" target="_self">Runs Scored</a></li>
          <li><a href="#average" target="_self">Batting Averages</a></li>
        <ul>
      </nav>
      <h3><a href="./index.html" target="_self">Back To Home</a></h3>
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
    </main>
  </body>
</html>
'''


html_file= open("statistics.html","w")
html_file.write(statisticsHTML)
html_file.close()
