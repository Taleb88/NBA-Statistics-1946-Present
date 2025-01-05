# TESTING VARIOUS QUERIES
import pandas as pd

player_per_game_df = pd.read_excel('Player Per Game.xlsx')
player_career_info_df = pd.read_excel('Player Career Info.xlsx')
#player per game
cols = list(player_per_game_df.columns)
index = 0

print('\nPlayer Per Game:')
for col_names in cols:
    print(index, col_names)
    index += 1
    
# player career info
cols = list(player_career_info_df.columns)
index = 0

print('\nPlayer Career Info:')
for col_names in cols:
    print(index, col_names)
    index += 1


# ===================== #
# interacting with user 
# ===================== #

# look up player in player_per_game_df
player_values = list(player_per_game_df['player'].values)

player = input("enter player's name: ")

if player in player_values:
    player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 4:28], axis=1)
    #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 8:10], axis=1)
    #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 0:1], axis=1)
    #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 1:2], axis=1)
    print(f"{player_per_game_df[(player_per_game_df['player'] == player)]}")
else:
    print('Does not exist')


''' # look up player and year they played in look up player in player_per_game_df
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
    print('Does not exist')'''

