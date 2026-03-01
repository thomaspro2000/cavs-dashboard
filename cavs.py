from nba_api.stats.endpoints import leaguegamefinder

def gather_yearly_stats(teamid):
    try:
        df = leaguegamefinder.LeagueGameFinder(team_id_nullable=teamid).get_data_frames()[0]
        if df.empty:
            return None
        else:
            recentSeason = df[df['GAME_DATE'].between('2026-01-01', '2026-12-31')]
            filteredrecentSeason = recentSeason[["TEAM_NAME", "GAME_DATE", "MATCHUP", "PTS", "WL", "FG_PCT"]]
            return filteredrecentSeason
    except:
        print("API Call was unsuccessful, please check GameID")
