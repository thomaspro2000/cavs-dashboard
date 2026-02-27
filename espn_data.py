import requests
import json

url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?limit=1&dates=2026"

def gather_stats():
   try:
    data = requests.get(url=url)
    return data.json()
   except:
    print("API call is not available")
      