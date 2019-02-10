import requests
import os

from nba_api.stats.endpoints import scoreboardv2

req = scoreboardv2.ScoreboardV2()
#games = req.get_normalized_json()
games = req.game_header.get_json()
print (type(games))
print (games)
# for g in games:
#     print (g)
