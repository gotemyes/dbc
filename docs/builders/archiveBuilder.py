import pandas as pd
import sys
sys.path.append('../../')

import data.teamDict as td

batData = pd.read_csv('../../data/dbc_stats - batting.csv')
bowlData = pd.read_csv('../../data/dbc_stats - bowling.csv')

### PREVIOUS SEASON LINKS
currentSeason = batData['season'].max()
previousSeasons = batData['season'].unique().tolist()
previousSeasons.sort(reverse=True)


seasonTags=[]
for season in previousSeasons:

    opponents = batData[batData['season']==season]\
        .groupby('opponent').mean().sort_values('gameID',ascending=True).index.tolist()
    oppTags = []
    for opp in opponents:
        tag = f'<li><a href="../games/s{season}/{td.teamCodes[opp]}.html" target="_self">{opp}</a></li>'
        oppTags.append(tag)

    seasonTagBody = ' '*12+('\n'+' '*12).join(oppTags)
    seasonTagTop = ' '*6+'<section>\n'+' '*8+f'<h2>Season {season}</h2>\n'+' '*10+'<ol>'
    seasonTagBottom = ' '*10+'<ol>\n'+' '*6+'</section>'

    seasonTags.append(seasonTagTop+'\n'+seasonTagBody+'\n'+seasonTagBottom)

allSeasonTags='\n'.join(seasonTags)




archiveHTML = f'''<!DOCTYPE html>
<html>
  <head>
    <title>Previous Seasons</title>
    <link href="../css/style.css" rel="stylesheet" type="text/css">
    <link rel="shortcut icon" type="image/x-icon" href="../images/cricket.ico">
  </head>
  <body>
    <header>
      <h1>Previous Seasons</h1>
      <p>Thanks for checking out the archive! Our record keeping has improved as time has gone on, so older games will have less information associated.</p>
      <h3><a href="../../index.html" target="_self">Back To Home</a></h3>
    </header>
    <main>
{allSeasonTags}
    </main>
  </body>
</html>'''


html_file= open(f"../resources/pages/archive.html","w")
html_file.write(archiveHTML)
html_file.close()
