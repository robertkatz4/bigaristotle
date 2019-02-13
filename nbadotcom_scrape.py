import requests
import os
import json
import boto3

from nba_api.stats.endpoints import scoreboardv2

session = boto3.session.Session(profile_name=os.environ["AWS_PROFILE"])

dynamodb = session.resource('dynamodb',
                            region_name='us-east-1',
                            endpoint_url="https://dynamodb.us-east-1.amazonaws.com:443")
table = dynamodb.Table('Scoreboard')

count = 0
while count < 366:
    req = scoreboardv2.ScoreboardV2(game_date='1996-12-01', league_id='00', day_offset=count)
    #games = req.get_normalized_json()
    print(count)

    games = req.game_header.get_json()
    games_json = json.loads(games)
    for g in (games_json['data']):
        game_date_est = g[0]
        game_sequence = g[1]
        game_id = g[2]
        game_status_id = g[3]
        game_status_text = g[4]
        game_code = g[5]
        home_team_id = g[6]
        visitor_team_id = g[7]
        season = g[8]
        live_period = g[9]
        live_pc_time = g[10]
        natl_tv_broad = g[11]
        arena_name = g[16]
        # info = movie['info']

        print("adding game:", game_id, game_code)

        table.put_item(
           Item={
               'game_id': game_id,
               'game_date_est': game_date_est,
               'game_code': game_code,
               'home_team_id': home_team_id,
               'visitor_team_id': visitor_team_id,
               'season': season,
               'arena_name': arena_name,
           }
        )

    count += 1
