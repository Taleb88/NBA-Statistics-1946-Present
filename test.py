# TESTING VARIOUS QUERIES
import pandas as pd
import time

#player_per_game_df = pd.read_csv('csv/Player Per Game.csv')
#player_career_info_df = pd.read_csv('csv/Player Career Info.csv')
#player_season_info_df = pd.read_csv('csv/Player Season Info.csv')
#player_shooting_df = pd.read_csv('csv/Player Shooting.csv')
#player_totals_df = pd.read_csv('csv/Player Totals.csv')

advanced_df = pd.read_excel('advanced.xlsx')
all_star_selections_df = pd.read_excel('All-Star Selections.xlsx')
end_of_season_teams_voting_df = pd.read_excel('End of Season Teams (Voting).xlsx')
end_of_season_teams_df = pd.read_excel('End of Season Teams.xlsx')
opponent_stats_per_100_poss_df = pd.read_excel('Opponent Stats Per 100 Poss.xlsx')
opponent_stats_per_game_df = pd.read_excel('Opponent Stats Per Game.xlsx')
opponent_totals_df = pd.read_excel('Opponent Totals.xlsx')
per_36_minutes_df = pd.read_excel('Per 36 Minutes.xlsx')
per_100_poss_df = pd.read_excel('Per 100 Poss.xlsx')
player_award_shares_df = pd.read_excel('Player Award Shares.xlsx')
player_career_info_df = pd.read_excel('Player Career Info.xlsx')
player_per_game_df = pd.read_excel('Player Per Game.xlsx')
player_play_by_play_df = pd.read_excel('Player Play By Play.xlsx')
player_season_info_df = pd.read_excel('Player Season Info.xlsx')
player_shooting_df = pd.read_excel('Player Shooting.xlsx')
player_totals_df = pd.read_excel('Player Totals.xlsx')
team_abbrev_df = pd.read_excel('Team Abbrev.xlsx')
team_stats_per_100_poss_df = pd.read_excel('Team Stats Per 100 Poss.xlsx')
team_stats_per_game_df = pd.read_excel('Team Stats Per Game.xlsx')
team_summaries_df = pd.read_excel('Team Summaries.xlsx')
team_totals_df = pd.read_excel('Team Totals.xlsx')


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

print('')


# =================#
# groupby 
# =================#

# player_award_shares_df
player_award_shares_df = pd.read_csv('csv/Player Award Shares.csv')

grouped = player_award_shares_df.groupby(['player', 'award']).agg(
    first_place_votes_avg = ('first', 'mean')
)
print(grouped)

print('')

grouped = player_award_shares_df.groupby('player')['pts_won'].mean()
print(grouped)

print('')
# team_summaries_df
team_summaries_df = pd.read_csv('csv/Team Summaries.csv')
grouped = team_summaries_df.groupby('team').agg(
    player_age_average=('age', 'mean'),
    reg_season_win_average=('w', 'mean'),
    reg_season_loss_average=('l', 'mean')
)
print(grouped.head(50))

print('')

grouped = team_summaries_df.groupby('team').filter(lambda row: row['w'].mean() < 20.0)
print(grouped.head(50).sort_values(by='team', ascending=True))



'''
# TEST ONLY - 1-9-2025 = SUCCESS
player_per_game_df['birth_year'] = player_per_game_df['birth_year'].fillna(0).astype(int)
player_per_game_df.to_excel('test.xlsx', index=False)

player_per_game_df['player'] = player_per_game_df['player'].replace('.0','')
player_per_game_df.to_excel('test.xlsx', index=False)

player_per_game_df['player'] = player_per_game_df['player'].astype(str) + " (b. " + player_per_game_df['birth_year'].astype(str) + ")"
player_per_game_df.to_excel('test.xlsx', index=False)
'''


'''
# checking to see if players have an age of '0' in multiple datasets
#   1_7_2025 - update, Index should now be an empty array [] given that all cells
#                   now been populated accordingly - COMPLETE
def player(df):
    return df[df['age'] == 0]

print(player(player_per_game_df)\
      .drop(player_per_game_df.iloc[:, 4:], axis=1)
      )
print(player(player_season_info_df)\
      .drop(player_season_info_df.iloc[:, 4:], axis=1)
      )
print(player(player_totals_df)\
      .drop(player_totals_df.iloc[:, 4:], axis=1)
      )'''

'''
# - COMPLETED AS OF 1_7_2025 - CAN BE ADDED TO main.py - *MUST BE LEFT COMMENTED OUT*
# creating new dataframe with unique player ids
unique_columns_df = pd.DataFrame()
player_id = player_per_game_df.iloc[:,2]
unique_columns_df['player_id'] = player_id.copy()
player = player_per_game_df.iloc[:,3]
unique_columns_df['player'] = player.copy()
player = player_per_game_df.iloc[:,4]
unique_columns_df['birth_year'] = player.copy()

unique_columns_df.to_excel('test.xlsx', index=False)

unique_columns_df = unique_columns_df.drop_duplicates()

unique_columns_df.to_excel('test.xlsx', index=False)
'''

# defining a player class that corresponds to the 
#   player_award_shares_and_player_per_game_merged dataframe
player_award_shares_and_player_per_game_merged_df = \
    pd.read_excel('player_award_shares_and_player_per_game_merged.xlsx')

class Player:
    def __init__(self, name, season_ending_year, award, pts_per_game):
        self.name = name
        self.season_ending_year = season_ending_year
        self.award = award
        self.pts_per_game = pts_per_game

    def info(self):
        try:
            return f"{self.name} won the {self.season_ending_year} {self.award} while averaging {self.pts_per_game} points per game."
        except Exception as e:
            print(f'caught {type(e)}: e \n'
                f'cannot list results')
    
value = player_award_shares_and_player_per_game_merged_df.iloc[5]

player_instance = Player(name=value['player_x'], 
                         season_ending_year=value['season_ending_year_x'], 
                         award=value['award'],
                         pts_per_game=value['pts_per_game'])

print(player_instance.info())




#############################
#     TESTING AREA ONLY     #
#############################
'''
# TEST ONLY 1-11-2025 - COMPLETE
player_career_info_df = pd.DataFrame()
player_id = player_per_game_df.iloc[:, 2]
player_career_info_df['player_id'] = player_id.copy()
player = player_per_game_df.iloc[:, 3]
player_career_info_df['player'] = player.copy()
birth_year = player_per_game_df.iloc[:, 4]
player_career_info_df['birth_year'] = birth_year.copy()
player_career_info_df['hof'] = ['No'] * len(player_per_game_df) # list comprehension to follow for Yes, No values
num_seasons = player_per_game_df.iloc[:, 7]
player_career_info_df['num_seasons'] = num_seasons.copy() # column to be converted to int
first_season = player_per_game_df.iloc[:, 38]
player_career_info_df['first_season'] = first_season.copy() # get min value later
last_season = player_per_game_df.iloc[:, 38]
player_career_info_df['last_season'] = last_season.copy() # get max value later
# save file
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
# min value for first_season
player_career_info_df = \
    player_career_info_df.groupby(['player_id', 'player', 'birth_year', 'hof']).agg({
        'num_seasons': "max",
        'first_season': "min", 
        'last_season': "max"
        }
    ).reset_index()
# save file
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
'''

'''
# TEST ONLY 1-11-2025 - COMPLETE
import os

file_path = 'Player Career Info.xlsx'

if os.path.isfile(file_path):
    os.remove(file_path)
    print('removal of initial player_career_info.xlsx file = success')
else:
    print('player_career_info_df.xlsx does not exist')

start_time = time.time()

print('removal of player_career_info_df.xlsx accordingly = success - ', (time.time() - start_time))
'''

'''
#TEST ONLY 1-10-2025; 1-11-2025 - COMPLETE
#   WILL NOT MOVE FORWARD WITH THIS DUE TO ELSE STATEMENT REQUIRED
player_per_game_df['stl_per_game'] = ['N/A - Stat tracked as of the 1973-74 NBA Season'
                                      if x[1] < 1974 and (x[8] == 'NBA' or x[8] == 'BAA')
                                      else ''
                                      for x in player_per_game_df.itertuples()]

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df['stl_per_game'] = ['N/A - Stat tracked as of the 1973-74 ABA Season'
                                      if x[1] < 1974 and x[8] == 'ABA'
                                      else ''
                                      for x in player_per_game_df.itertuples()]

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

start_time = time.time()

print('updating stl_per_game and blk_per_game columns accordingly = success - ', (time.time() - start_time))
'''

'''
# 1-10-2025 - SUCCESS
advanced_df = pd.read_excel('advanced.xlsx')

advanced_df.loc[advanced_df['player_id'] == 1, 'player'] = 'Patrick Ewing Jr.'

advanced_df.to_excel('test.xlsx', index=False)
'''

'''
# 1-10-2025 - SUCCESS
x = pd.read_excel('Player Per Game.xlsx')

x = x['player'].replace('.0', '')

x.to_excel('test.xlsx')
'''

'''
x = x.sort_values(by=['player'], ascending=True)

x.to_excel('test.xlsx')

x['player'] = x['player'].replace('.0','',inplace=True)

x.to_excel('test.xlsx')

x['player_id'] = x['player'].factorize()[0] + 1

x.to_excel('test.xlsx')
'''



'''
# COMPLETED AS OF 1-9-2025
player_season_info_df['player'] = player_season_info_df['player'].astype(str) + " (b. " + player_season_info_df['birth_year'].astype(str) + ")"
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df['player'] = player_per_game_df['player'].replace('.0','')
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
'''

'''
#COMPLETED AS OF 1_7_2025 AND 1_8_2025
test_temp_df = pd.read_excel('TEST_TEMP_TO_BE_REMOVED.xlsx')

test_temp_df['X'] = test_temp_df.apply(lambda x: x['X'] - 1 
                                       if x['X'] == 100 
                                       or x['X'] == 200 
                                       or x['X'] == 300
                                       or x['X'] == 400 
                                       else x['X'] + 0, 
                                       axis=1)

test_temp_df.to_excel('TEST_TEMP_TO_BE_REMOVED.xlsx', index=False)
'''

'''
# - COMPLETE AS OF 1_8_2025
# creating new dataframe with unique player ids
unique_columns_df = pd.DataFrame()
player_id = player_per_game_df.iloc[:,2]
unique_columns_df['player_id'] = player_id.copy()
player = player_per_game_df.iloc[:,3]
unique_columns_df['player'] = player.copy()
player = player_per_game_df.iloc[:,4]
unique_columns_df['birth_year'] = player.copy()

unique_columns_df.to_excel('test_1_8_2025.xlsx', index=False)

unique_columns_df = unique_columns_df.drop_duplicates()

unique_columns_df.to_excel('test.xlsx', index=False)
'''

'''
# TESTING IN PROGRESS - COMPLETE ON 1-8-2025
# read player_per_game and do the following modifications
player_per_game_df = pd.merge(player_per_game_df, player_career_info_df,
                              how='outer', on='player')

player_per_game_df.to_excel('new_tile_temp.xlsx')

player_per_game_df.sort_values(by='player')

player_per_game_df.to_excel('new_tile_temp.xlsx')

# copy player_id values from player_id_y to player_id_x
player_per_game_df['player_id_x'] = player_per_game_df['player_id_y']


player_per_game_df.to_excel('new_tile_temp.xlsx')
'''


# ===================== #
# interacting with user 
# ===================== #

# look up player in player_career_info_df
print('\nlook up player (first name and last name required) in player_career_info_df')

player_values = list(player_career_info_df['player'].values)

while True:

    player = input("enter player's name: ")

    if player == 'exit':
        break

    if player in player_values:
        print(f"{player_career_info_df[(player_career_info_df['player'] == player)]}")
    elif player not in player_values:
        print('not exist')
    else:
        continue


# look up player in player_per_game_df via player_id
print('\nlook up player via player_id in player_per_game_df')

player_values = list(player_per_game_df['player_id'].values)

while True:

    try:
        player_id = int(input("enter player_id: "))

        if player_id == -1:
            break

        if player_id in player_values:
            #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 5:28], axis=1)
            #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 8:10], axis=1)
            #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 0:1], axis=1)
            #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 1:2], axis=1)
            print(f"{player_per_game_df[(player_per_game_df['player_id'] == player_id)]}")
        elif player_id not in player_values:
            print('not exist')
        elif not player_id.isnumeric():
            print('please enter a numerical value only')
    except ValueError:
        print('please enter a number only')
        continue


# look up player in player_per_game_df
print('\nlook up player (first name and last name required) in player_per_game_df')

player_values = list(player_per_game_df['player'].values)

while True:

    player = input("enter player's name: ")

    if player == 'exit':
        break

    if player in player_values:
        player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 4:28], axis=1)
        player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 8:10], axis=1)
        player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 0:1], axis=1)
        player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 1:2], axis=1)
        print(f"{player_per_game_df[(player_per_game_df['player'] == player)]}")
    elif player not in player_values:
        print('not exist')
    else:
        continue


# look up player and year they played in look up player in player_per_game_df
print(f"\nlook up player (first name and last name required) " 
      f"and year they played in player_per_game_df")

player_values = list(player_per_game_df['player'].values)
year_values = list(player_per_game_df['year'].values)

while True:

    player = input("enter player's name: ")
    year = int(input("enter year: "))

    if player == 'exit':
        break

    if (player in player_values) and (year in year_values):
        # player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 4:28], axis=1)
        # player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 8:10], axis=1)
        # player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 0:1], axis=1)
        # player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 1:2], axis=1)
        print(f"{player_per_game_df[(player_per_game_df['player'] == player) & \
                                    (player_per_game_df['year'] == year)]}")
    elif (player not in player_values) or (year in year_values):
        print('not exist')
    else:
        continue

# =========================== #
