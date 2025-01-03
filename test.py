# TESTING VARIOUS QUERIES
import pandas as pd

# read csv
player_per_game_df = pd.read_excel('Player Per Game.xlsx')

cols = list(player_per_game_df.columns)
index = 0

for col_names in cols:
    print(index, col_names)
    index += 1

# ===================== #
# interacting with user 
# ===================== #
player_values = list(player_per_game_df['player'].values)
year_values = list(player_per_game_df['year'].values)

player = input("enter player's name: ")
year = int(input("enter year: "))

if (player in player_values) and (year in year_values):
    player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 4:28], axis=1)
    # player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 8:10], axis=1)
    # player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 0:1], axis=1)
    # player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 1:2], axis=1)
    print(f"{player_per_game_df[(player_per_game_df['player'] == player) & \
                                (player_per_game_df['year'] == year)]}")
else:
    print('Does not exist')