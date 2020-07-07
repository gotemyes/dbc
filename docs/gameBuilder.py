from shutil import copyfile
import pandas as pd
import sys, os
sys.path.append('../')


import data.teamDict as td

batData = pd.read_csv('../data/dbc_stats - batting.csv')
bowlData = pd.read_csv('../data/dbc_stats - bowling.csv')



if not os.path.exists('games'):
    os.makedirs('games')

seasons = batData['season'].unique()

for season in seasons:
    if not os.path.exists(f'games/s{season}'):
        os.makedirs(f'games/s{season}')

    opponents = batData[batData['season']==season]['opponent'].unique()

    for opponent in opponents:

        thisGame = batData[(batData['season']==season)&(batData['opponent']==opponent)].copy()
        thisGame['balls_faced']=['' if pd.isnull(el) else int(el) for el in thisGame['balls_faced'].values]
        thisGame['fours']=['' if pd.isnull(el) else int(el) for el in thisGame['fours'].values]
        thisGame['sixes']=['' if pd.isnull(el) else int(el) for el in thisGame['sixes'].values]

        topBat = thisGame.sort_values('runs',ascending=False).iloc[:3]
        topBatList = []
        for ind, row in topBat.iterrows():
            performance = row['player']+'   '+str(row['runs'])
            topBatList.append(performance)

        thisGameBowl = bowlData[(bowlData['season']==season)&(bowlData['country']==opponent)].copy()
        topBowl = thisGameBowl.sort_values('wickets',ascending=False).iloc[:2]
        topBowlList = []
        for ind, row in topBowl.iterrows():
            performance = row['bowler']+'   '+str(row['wickets'])+'/'+str(row['runs'])
            topBowlList.append(performance)

        topBatStr = '<br>'.join(topBatList)
        topBowlStr = '<br>'.join(topBowlList)

        for ind, row in thisGameBowl.iterrows():
            '''<tr>
                <td>{thisGameBowl.iloc[0]['bowler']}</td>
                <td>{thisGameBowl.iloc[0]['overs']}</td>
                <td>{thisGameBowl.iloc[0]['maidens']}</td>
                <td>{thisGameBowl.iloc[0]['runs']}</td>
                <td>{thisGameBowl.iloc[0]['wickets']}</td>
                <td>{thisGameBowl.iloc[0]['rpo']}</td>
                <td>{thisGameBowl.iloc[0]['runs']}</td>
                <td>{thisGameBowl.iloc[0]['extras']}</td>
            </tr>'''

        gameHTML = f'''<!DOCTYPE html>
        <html>
          <head>
            <title>{opponent} - Season {season}</title>
            <link href="../../style.css" rel="stylesheet" type="text/css">
          </head>
          <body>
            <header>
              <h1>{opponent} - Season {season}</h1>
              <h3><a href="../../index.html" target="_self">Back To Home</a></h3>
            </header>
              <main>
                <h2>Highlights</h2>
                <h3>Batting</h3>
                  <p>{topBatStr}</p>
                <h3>Bowling</h3>
                  <p>{topBowlStr}</p>
                <h2>Scorecard</h3>
                  <table>
                  <tr>
                      <th scope="col">Batsman</th>
                      <th scope="col">Controller</th>
                      <th scope="col">Runs</th>
                      <th scope="col">Balls</th>
                      <th scope="col">Fours</th>
                      <th scope="col">Sixes</th>
                      <th scope="col">Strike Rate</th>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[0]['player']}</td>
                      <td>{thisGame.iloc[0]['controller']}</td>
                      <td>{thisGame.iloc[0]['runs']}</td>
                      <td>{thisGame.iloc[0]['balls_faced']}</td>
                      <td>{thisGame.iloc[0]['fours']}</td>
                      <td>{thisGame.iloc[0]['sixes']}</td>
                      <td>{thisGame.iloc[0]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[1]['player']}</td>
                      <td>{thisGame.iloc[1]['controller']}</td>
                      <td>{thisGame.iloc[1]['runs']}</td>
                      <td>{thisGame.iloc[1]['balls_faced']}</td>
                      <td>{thisGame.iloc[1]['fours']}</td>
                      <td>{thisGame.iloc[1]['sixes']}</td>
                      <td>{thisGame.iloc[1]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[2]['player']}</td>
                      <td>{thisGame.iloc[2]['controller']}</td>
                      <td>{thisGame.iloc[2]['runs']}</td>
                      <td>{thisGame.iloc[2]['balls_faced']}</td>
                      <td>{thisGame.iloc[2]['fours']}</td>
                      <td>{thisGame.iloc[2]['sixes']}</td>
                      <td>{thisGame.iloc[2]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[3]['player']}</td>
                      <td>{thisGame.iloc[3]['controller']}</td>
                      <td>{thisGame.iloc[3]['runs']}</td>
                      <td>{thisGame.iloc[3]['balls_faced']}</td>
                      <td>{thisGame.iloc[3]['fours']}</td>
                      <td>{thisGame.iloc[3]['sixes']}</td>
                      <td>{thisGame.iloc[3]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[4]['player']}</td>
                      <td>{thisGame.iloc[4]['controller']}</td>
                      <td>{thisGame.iloc[4]['runs']}</td>
                      <td>{thisGame.iloc[4]['balls_faced']}</td>
                      <td>{thisGame.iloc[4]['fours']}</td>
                      <td>{thisGame.iloc[4]['sixes']}</td>
                      <td>{thisGame.iloc[4]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[5]['player']}</td>
                      <td>{thisGame.iloc[5]['controller']}</td>
                      <td>{thisGame.iloc[5]['runs']}</td>
                      <td>{thisGame.iloc[5]['balls_faced']}</td>
                      <td>{thisGame.iloc[5]['fours']}</td>
                      <td>{thisGame.iloc[5]['sixes']}</td>
                      <td>{thisGame.iloc[5]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[6]['player']}</td>
                      <td>{thisGame.iloc[6]['controller']}</td>
                      <td>{thisGame.iloc[6]['runs']}</td>
                      <td>{thisGame.iloc[6]['balls_faced']}</td>
                      <td>{thisGame.iloc[6]['fours']}</td>
                      <td>{thisGame.iloc[6]['sixes']}</td>
                      <td>{thisGame.iloc[6]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[7]['player']}</td>
                      <td>{thisGame.iloc[7]['controller']}</td>
                      <td>{thisGame.iloc[7]['runs']}</td>
                      <td>{thisGame.iloc[7]['balls_faced']}</td>
                      <td>{thisGame.iloc[7]['fours']}</td>
                      <td>{thisGame.iloc[7]['sixes']}</td>
                      <td>{thisGame.iloc[7]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[8]['player']}</td>
                      <td>{thisGame.iloc[8]['controller']}</td>
                      <td>{thisGame.iloc[8]['runs']}</td>
                      <td>{thisGame.iloc[8]['balls_faced']}</td>
                      <td>{thisGame.iloc[8]['fours']}</td>
                      <td>{thisGame.iloc[8]['sixes']}</td>
                      <td>{thisGame.iloc[8]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[9]['player']}</td>
                      <td>{thisGame.iloc[9]['controller']}</td>
                      <td>{thisGame.iloc[9]['runs']}</td>
                      <td>{thisGame.iloc[9]['balls_faced']}</td>
                      <td>{thisGame.iloc[9]['fours']}</td>
                      <td>{thisGame.iloc[9]['sixes']}</td>
                      <td>{thisGame.iloc[9]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[10]['player']}</td>
                      <td>{thisGame.iloc[10]['controller']}</td>
                      <td>{thisGame.iloc[10]['runs']}</td>
                      <td>{thisGame.iloc[10]['balls_faced']}</td>
                      <td>{thisGame.iloc[10]['fours']}</td>
                      <td>{thisGame.iloc[10]['sixes']}</td>
                      <td>{thisGame.iloc[10]['sr']}</td>
                  </tr>
                  <tr>
                      <td>{thisGame.iloc[11]['player']}</td>
                      <td></td>
                      <td>{thisGame.iloc[11]['runs']}</td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td><strong>Total</strong></td>
                      <td></td>
                      <td>{thisGame['runs'].sum()}</td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  </table>
                  <table>
                  <tr>
                      <th scope="col">Bowler</th>
                      <th scope="col">Overs</th>
                      <th scope="col">Maidens</th>
                      <th scope="col">Runs</th>
                      <th scope="col">Wickets</th>
                      <th scope="col">Economy</th>
                      <th scope="col">Strike Rate</th>
                      <th scope="col">Extras</th>
                  </tr>
                  <tr>
                      <td>{thisGameBowl.iloc[0]['bowler']}</td>
                      <td>{thisGameBowl.iloc[0]['overs']}</td>
                      <td>{thisGameBowl.iloc[0]['maidens']}</td>
                      <td>{thisGameBowl.iloc[0]['runs']}</td>
                      <td>{thisGameBowl.iloc[0]['wickets']}</td>
                      <td>{thisGameBowl.iloc[0]['rpo']}</td>
                      <td>{thisGameBowl.iloc[0]['runs']}</td>
                      <td>{thisGameBowl.iloc[0]['extras']}</td>
                  </tr>
                  </table>
              </main>
          </body>
        </html>'''


        html_file= open(f"./games/s{season}/{td.teamCodes[opponent]}.html","w")
        html_file.write(gameHTML)
        html_file.close()
