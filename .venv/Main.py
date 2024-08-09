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
    return data.json()


# Step 1: Load JSON data from the file
with open('data.txt', 'r') as file:
    data = json.load(file)

# Step 2: Normalize JSON data to flatten the structure
df = pd.json_normalize(data, 'bookmakers', ['sport_key', 'sport_title', 'commence_time', 'home_team', 'away_team'])

# Step 3: Extract relevant columns
df = df[['sport_key', 'sport_title', 'commence_time', 'home_team', 'away_team', 'title', 'markets']]

# Step 4: Expand the 'markets' column to include detailed information
markets_df = pd.json_normalize(df['markets'].explode())
df = df.drop(columns=['markets']).join(markets_df)
outcomes_df = pd.json_normalize(df['outcomes'].explode())
df = df.drop(columns=['outcomes']).join(outcomes_df)
# Display the DataFrame
print(df.head())
df.to_csv('newdata.csv', index=False)

# data = json.dumps(fetch_data(apikey),indent=2)
# print(data)
#
# df = pd.read_csv('data.csv')
# json_data = df.to_json(orient='records')
# df = pd.json_normalize(json.loads(json_data))
# print(df.head())
# df['bookmakers'] = df['bookmakers'].apply(json.loads)
# df['bookmaker_titles'] = df['bookmakers'].apply(lambda x: [bookmaker['title'] for bookmaker in x])
# filtered_df = df[['home_team', 'away_team', 'bookmakers[key]']]
# print(filtered_df.head())
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