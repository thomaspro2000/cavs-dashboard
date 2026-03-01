import cavs
import nbateamid
import pandas as pd

# Please enter NBA Team name within the "Team Name variable"

nba_team_name = 'Los Angeles Clippers'

nba_id = nbateamid.findnbateamId(nba_team_name)

data = cavs.gather_yearly_stats(nba_id)
print(data)