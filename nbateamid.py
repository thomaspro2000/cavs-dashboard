from nba_api.stats.static import teams
import pandas as pd

# teamdata = teams.get_teams()
# print(teamdata)

def findnbateamId(teamname):
    try:
        nbaTeam = teams.find_teams_by_full_name(teamname)
        id = nbaTeam[0]['id']
        if id == 0:
            print("No ID found. Please double check NBA Team Name")
        else:
            print(id)
            return id
        
    except:
        print("Double check function")

    