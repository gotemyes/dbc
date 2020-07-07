import pandas as pd
import sys
sys.path.append('../')

import data.teamDict as td

batData = pd.read_csv('../data/dbc_stats - batting.csv')
bowlData = pd.read_csv('../data/dbc_stats - batting.csv')

### CAREER STATS

##innings
totalInnings = batData[batData['position']!=0].shape[0]
aaInnings = batData[batData['controller']=='AA'].shape[0]
rmInnings = batData[batData['controller']=='RM'].shape[0]
if aaInnings>rmInnings:
    aaInnings='<strong>'+str(aaInnings)+'</strong>'
elif aaInnings<rmInnings:
    rmInnings='<strong>'+str(rmInnings)+'</strong>'
else:
    aaInnings='<strong>'+str(aaInnings)+'</strong>'
    rmInnings='<strong>'+str(rmInnings)+'</strong>'

##NOs
totalNOs = batData[batData['dismissal']=='not_out'].shape[0]
aaNOs = batData[(batData['controller']=='AA')&(batData['dismissal']=='not_out')].shape[0]
rmNOs = batData[(batData['controller']=='RM')&(batData['dismissal']=='not_out')].shape[0]
if aaNOs>rmNOs:
    aaNOs='<strong>'+str(aaNOs)+'</strong>'
elif aaNOs<rmNOs:
    rmNOs='<strong>'+str(rmNOs)+'</strong>'
else:
    aaNOs='<strong>'+str(aaNOs)+'</strong>'
    rmNOs='<strong>'+str(rmNOs)+'</strong>'

##runs
totalRuns = batData['runs'].sum()
aaRuns = batData[batData['controller']=='AA']['runs'].sum()
rmRuns = batData[batData['controller']=='RM']['runs'].sum()
if aaRuns>rmRuns:
    aaRuns='<strong>'+str(aaRuns)+'</strong>'
elif aaRuns<rmInnings:
    rmRuns='<strong>'+str(rmRuns)+'</strong>'
else:
    aaRuns='<strong>'+str(aaRuns)+'</strong>'
    rmRuns='<strong>'+str(rmRuns)+'</strong>'

##HS
totalHSDis = batData.sort_values('runs',ascending=False).iloc[0][['runs','dismissal']]
aaHSDis = batData[batData['controller']=='AA'].sort_values('runs',ascending=False).iloc[0][['runs','dismissal']]
rmHSDis = batData[batData['controller']=='RM'].sort_values('runs',ascending=False).iloc[0][['runs','dismissal']]
if totalHSDis['dismissal']=='not_out':
    totalHS=str(totalHSDis['runs'])+'*'
else:
    totalHS=str(totalHSDis['runs'])
if aaHSDis['dismissal']=='not_out':
    aaHS=str(aaHSDis['runs'])+'*'
else:
    aaHS=str(aaHSDis['runs'])
if rmHSDis['dismissal']=='not_out':
    rmHS=str(rmHSDis['runs'])+'*'
else:
    rmHS=str(rmHSDis['runs'])

if aaHSDis['runs']>rmHSDis['runs']:
    aaHS='<strong>'+aaHS+'</strong>'
elif aaHSDis['runs']<rmHSDis['runs']:
    rmHS='<strong>'+rmHS+'</strong>'
else:
    aaHS='<strong>'+aaHS+'</strong>'
    rmHS='<strong>'+rmHS+'</strong>'

##ave
totalAve = round(batData['runs'].sum()/batData[batData['dismissal']!="not_out"].shape[0],2)
aaAve = round(batData[batData['controller']=='AA']['runs'].sum()/batData[(batData['controller']=='AA')&(batData['dismissal']!="not_out")].shape[0],2)
rmAve = round(batData[batData['controller']=='RM']['runs'].sum()/batData[(batData['controller']=='RM')&(batData['dismissal']!="not_out")].shape[0],2)
if aaAve>rmAve:
    aaAve='<strong>'+str(aaAve)+'</strong>'
elif aaAve<rmAve:
    rmAve='<strong>'+str(rmAve)+'</strong>'
else:
    aaAve='<strong>'+str(aaAve)+'</strong>'
    rmAve='<strong>'+str(rmAve)+'</strong>'

##balls_faced
totalBF = int(batData['balls_faced'].sum())
aaBF = int(batData[batData['controller']=='AA']['balls_faced'].sum())
rmBF = int(batData[batData['controller']=='RM']['balls_faced'].sum())
if aaBF>rmBF:
    aaBF='<strong>'+str(aaBF)+'</strong>'
elif aaBF<rmBF:
    rmBF='<strong>'+str(rmBF)+'</strong>'
else:
    aaBF='<strong>'+str(aaBF)+'</strong>'
    rmBF='<strong>'+str(rmBF)+'</strong>'

##SR
totalSR = round(batData['runs'].sum()/batData['balls_faced'].sum()*100,2)
aaSR = round(batData[batData['controller']=='AA']['runs'].sum()/batData[batData['controller']=='AA']['balls_faced'].sum()*100,2)
rmSR = round(batData[batData['controller']=='RM']['runs'].sum()/batData[batData['controller']=='RM']['balls_faced'].sum()*100,2)
if aaSR>rmSR:
    aaSR='<strong>'+str(aaSR)+'</strong>'
elif aaSR<rmSR:
    rmSR='<strong>'+str(rmSR)+'</strong>'
else:
    aaSR='<strong>'+str(aaSR)+'</strong>'
    rmSR='<strong>'+str(rmSR)+'</strong>'

##100s
total100s = batData[batData['runs']>=100].shape[0]
aa100s = batData[(batData['controller']=='AA')&(batData['runs']>=100)].shape[0]
rm100s = batData[(batData['controller']=='RM')&(batData['runs']>=100)].shape[0]
if aa100s>rm100s:
    aa100s='<strong>'+str(aa100s)+'</strong>'
elif aa100s<rm100s:
    rm100s='<strong>'+str(rm100s)+'</strong>'
else:
    aa100s='<strong>'+str(aa100s)+'</strong>'
    rm100s='<strong>'+str(rm100s)+'</strong>'

##50s
total50s = batData[(batData['runs']>=50)&(batData['runs']<100)].shape[0]
aa50s = batData[(batData['controller']=='AA')&(batData['runs']>=50)&(batData['runs']<100)].shape[0]
rm50s = batData[(batData['controller']=='RM')&(batData['runs']>=50)&(batData['runs']<100)].shape[0]
if aa50s>rm50s:
    aa50s='<strong>'+str(aa50s)+'</strong>'
elif aa50s<rm50s:
    rm50s='<strong>'+str(rm50s)+'</strong>'
else:
    aa50s='<strong>'+str(aa50s)+'</strong>'
    rm50s='<strong>'+str(rm50s)+'</strong>'

##4s
total4s = int(batData['fours'].sum())
aa4s = int(batData[batData['controller']=='AA']['fours'].sum())
rm4s = int(batData[batData['controller']=='RM']['fours'].sum())
if aa4s>rm4s:
    aa4s='<strong>'+str(aa4s)+'</strong>'
elif aa4s<rm4s:
    rm4s='<strong>'+str(rm4s)+'</strong>'
else:
    aa4s='<strong>'+str(aa4s)+'</strong>'
    rm4s='<strong>'+str(rm4s)+'</strong>'

##6s
total6s = int(batData['sixes'].sum())
aa6s = int(batData[batData['controller']=='AA']['sixes'].sum())
rm6s = int(batData[batData['controller']=='RM']['sixes'].sum())
if aa6s>rm6s:
    aa6s='<strong>'+str(aa6s)+'</strong>'
elif aa6s<rm6s:
    rm6s='<strong>'+str(rm6s)+'</strong>'
else:
    aa6s='<strong>'+str(aa6s)+'</strong>'
    rm6s='<strong>'+str(rm6s)+'</strong>'

##ducks
total0s = batData[(batData['runs']==0)&(batData['position']!=0)].shape[0]
aa0s = batData[(batData['controller']=='AA')&(batData['runs']==0)].shape[0]
rm0s = batData[(batData['controller']=='RM')&(batData['runs']==0)].shape[0]
if aa0s>rm0s:
    aa0s='<strong>'+str(aa0s)+'</strong>'
elif aa0s<rm0s:
    rm0s='<strong>'+str(rm0s)+'</strong>'
else:
    aa0s='<strong>'+str(aa0s)+'</strong>'
    rm0s='<strong>'+str(rm0s)+'</strong>'

### CURRENT SEASON LINKS
currentSeason = batData['season'].max()
opponents = batData[batData['season']==currentSeason].groupby('opponent').mean().sort_values('gameID',ascending=True).index.tolist()
oppTags = []
for opp in opponents:
    tag = f'<li><a href="./games/s{currentSeason}/{td.teamCodes[opp]}.html" target="_self">{opp}</a></li>'
    oppTags.append(tag)

seasonTag = '\n          '.join(oppTags)


### CONSTRUCT HTML
indexHTML = f'''
<!DOCTYPE html>
<html>
  <head>
    <title>DBC - The Quest For 1000</title>
    <link href="style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <header>
      <h1>DBC - The Quest For 1000</h1>
      <p> Join Barbarooza and haast_schist as they strive for greatness in the world of virtual cricket!</p>
      <h3><a href="./archive.html" target="_self">Previous Seasons</a></h3>
    </header>
    <main>
      <section>
        <h2>Current Season ({currentSeason})</h2>
        <ol>
          {seasonTag}
        </ol>
      </section>
          <h2>Career Statistics</h2>
            <table>
                <tr>
                    <td></td>
                    <th scope="col">Barbarooza</th>
                    <th scope="col">haast_schist</th>
                    <th scope="col">Overall</th>
                </tr>
                <tr>
                    <th scope="row">Innings</th>
                    <td>{aaInnings}</td>
                    <td>{rmInnings}</td>
                    <td>{totalInnings}</td>
                </tr>
                <tr>
                    <th scope="row">Not Outs</th>
                    <td>{aaNOs}</td>
                    <td>{rmNOs}</td>
                    <td>{totalNOs}</td>
                </tr>
                <tr>
                    <th scope="row">Runs</th>
                    <td>{aaRuns}</td>
                    <td>{rmRuns}</td>
                    <td>{totalRuns}</td>
                </tr>
                <tr>
                    <th scope="row">High Score</th>
                    <td>{aaHS}</td>
                    <td>{rmHS}</td>
                    <td>{totalHS}</td>
                </tr>
                <tr>
                    <th scope="row">Average</th>
                    <td>{aaAve}</td>
                    <td>{rmAve}</td>
                    <td>{totalAve}</td>
                </tr>
                <tr>
                    <th scope="row">Balls Faced</th>
                    <td>{aaBF}</td>
                    <td>{rmBF}</td>
                    <td>{totalBF}</td>
                </tr>
                <tr>
                    <th scope="row">Strike Rate</th>
                    <td>{aaSR}</td>
                    <td>{rmSR}</td>
                    <td>{totalSR}</td>
                </tr>
                <tr>
                    <th scope="row">Hundreds</th>
                    <td>{aa100s}</td>
                    <td>{rm100s}</td>
                    <td>{total100s}</td>
                </tr>
                <tr>
                    <th scope="row">Fifties</th>
                    <td>{aa50s}</td>
                    <td>{rm50s}</td>
                    <td>{total50s}</td>
                </tr>
                <tr>
                    <th scope="row">Fours</th>
                    <td>{aa4s}</td>
                    <td>{rm4s}</td>
                    <td>{total4s}</td>
                </tr>
                <tr>
                    <th scope="row">Sixes</th>
                    <td>{aa6s}</td>
                    <td>{rm6s}</td>
                    <td>{total6s}</td>
                </tr>
                <tr>
                    <th scope="row">Ducks</th>
                    <td>{aa0s}</td>
                    <td>{rm0s}</td>
                    <td>{total0s}</td>
                </tr>
            </table>
        </main>
    </body>
</html>
'''

print(indexHTML)

html_file= open("index.html","w")
html_file.write(indexHTML)
html_file.close()
