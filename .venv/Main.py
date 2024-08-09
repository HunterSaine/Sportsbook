# Description: Main file for the application
import numpy as np
import pandas as pd
import requests
import json
from keys import apikey
def fetch_data(apikey):
    # Fetch data from the API
    # Return the data
    data = requests.get('https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=e9be841a2b734322476b32827df51230&regions=us&markets=h2h,spreads&oddsFormat=american')
    return data

# data = fetch_data(apikey).json()
# print(data)
# df = pd.json_normalize(data)
# print(df.head())
# df.to_csv('data.csv', index=False)
# df['bookmaker_titles'] = df['bookmakers'].apply(lambda x: [bookmaker['title'] for bookmaker in x])
# filtered_df = df[['home_team', 'away_team', 'sport_title', 'commence_time', 'bookmaker_titles']]
# # filtered_df.columns = ['Teams', 'Sites', 'Commence Time', 'H2H Odds', 'Spread Points', 'Spread Odds']
# print(filtered_df.head())
# filtered_df.to_csv('filtered_data.csv', index=False)