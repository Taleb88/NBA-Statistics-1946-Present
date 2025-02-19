# TESTING VARIOUS QUERIES
import pandas as pd
import numpy as np
import time

start_time = time.time()


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
#player_totals_df = pd.read_excel('Player Totals.xlsx')
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


'''
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

print('')

# new york knicks - 50-win seasons
team_summaries_df.loc[(team_summaries_df['team'] == 'New York Knicks') & 
                          (team_summaries_df['w'] > 50)]
print(team_summaries_df)
print('')
'''


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
    
value = player_award_shares_and_player_per_game_merged_df.iloc[0]

player_instance = Player(name=value['player_x'], 
                         season_ending_year=value['season_ending_year_x'], 
                         award=value['award'],
                         pts_per_game=value['pts_per_game'])

print(player_instance.info())


#############################
#     TESTING AREA ONLY     #
#############################

'''
# IN PROGRESS AS OF 2/10/2025 - COMPLETE AS OF 2/10/2025
stats_reference_guide_df = pd.DataFrame({
                                         'pts_per_game': ['Tracked since league debuted'],
                                         'trb_per_game': ['Tracked since the 1950-51 NBA Season'],
                                         'ast_per_game': ['Tracked since league debuted'],
                                         'blk_per_game': ['Tracked since the 1973-74 NBA Season'],
                                         'stl_per_game': ['Tracked since the 1973-74 NBA Season']
                                         })

stats_reference_guide_df.to_excel('stats_reference_guide.xlsx', index=False)
'''

'''
# IN PROGRESS AS OF 2/10/2025 - COMPLETE AS OF 2/10/2025
def award_winners_highlighted(x):
    try:
        if x == True:
            return 'background-color: green'     
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

player_award_shares_and_player_per_game_merged_styled_df = (
    player_award_shares_and_player_per_game_merged_df.
    style.
    map(award_winners_highlighted, subset=['winner'])
)

player_award_shares_and_player_per_game_merged_styled_df.to_excel('player_award_shares_and_player_per_game_merged.xlsx', index=False)
'''

'''
# IN PROGRESS AS OF 2/10/2025 - COMPLETE AS OF 2/10/2025
def player_per_game_highlighted(x):
    try:
        if x == 'N/A - Stat tracked as of the 1973-74 NBA Season' or \
            x == 'N/A - Stat tracked as of the 1973-74 ABA Season' or \
                x == 'N/A - Stat tracked as of the 1950-51 NBA Season':
            return 'background-color: orange'
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')
        
player_per_game_df = player_per_game_df.style.map(player_per_game_highlighted)

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
'''

'''
# IN PROGRESS AS OF 1/29/2025 AND 1/30/2025 - COMPLETE AS OF 1/31/2025
# ========================================================================================#
# 1. MANIPULATE TEAM DATA AND ADD TEAM_ID TO 4 TEAM DATASETS AND FACTORIZE PER TEAM; CHANGE ORDER OF COLUMNS PER SET - COMPLETE
#   a. filter out team = 'League Average' (df[df['team'] != 'League Average']) from the datasets via a user defined function - COMPLETE
#   b. create a new column in 4 team datasets (team_summaries_df, team_totals_df, team_abbrev_df, team_stats_per_game_df) 
#           called 'team_id' - COMPLETE
#   b. for the 'team_id' column, 'multiply' zero -> '0' by the length of the dataframe (len(data frame name goes here)) - COMPLETE
#   c. change order of columns to have the team_id as the first column of each team dataframe - COMPLETE
#   d. sort the team values by ascending (alphabetical) order in each team dataframe - COMPLETE
#   e. implement a factorize method to increment the id values based on the team values (ex: team_id=1, team='atlanta hawks') - COMPLETE
# 2. UPDATE TEAMS IN 2024-25 playoffs values from FALSE to "PENDING" - COMPLETE
# 3. CREATE SEPARATE DATAFRAMES FOR PLAYOFF TEAMS ONLY - COMPLETE
# ========================================================================================#

# 1a
def filter_out_league_average(df):
    try:
        return df[df['team'] != 'League Average']
    except Exception as e:
        return(f'cannot filter out "League Average" values {type(e)}')
# implement filtering to respective dataframes
team_abbrev_df = filter_out_league_average(team_abbrev_df)
team_stats_per_game_df = filter_out_league_average(team_stats_per_game_df)
team_summaries_df = filter_out_league_average(team_summaries_df)
team_totals_df = filter_out_league_average(team_totals_df)
# save changes
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)
# 1b
team_abbrev_df['team_id'] = 0 * len(team_abbrev_df)
team_stats_per_game_df['team_id'] = 0 * len(team_stats_per_game_df)
team_summaries_df['team_id'] = 0 * len(team_summaries_df)
team_totals_df['team_id'] = 0 * len(team_totals_df)
# save changes
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)
# remove unnamed columns via loc and ~
team_abbrev_df = team_abbrev_df.loc[:, ~team_abbrev_df.columns.str.contains('^Unnamed')]
team_stats_per_game_df = team_stats_per_game_df.loc[:, ~team_stats_per_game_df.columns.str.contains('^Unnamed')]
team_summaries_df = team_summaries_df.loc[:, ~team_summaries_df.columns.str.contains('^Unnamed')]
team_totals_df = team_totals_df.loc[:, ~team_totals_df.columns.str.contains('^Unnamed')]
# save changes
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)
# 1c
team_abbrev_df_col = list(team_abbrev_df.columns)
team_stats_per_game_df_col = list(team_stats_per_game_df.columns)
team_summaries_df_col = list(team_summaries_df.columns)
team_totals_df_col = list(team_totals_df.columns)

print('')
index = 0
for col_name in team_abbrev_df_col:
    print(index,col_name)
    index += 1
print('')

index = 0
for col_name in team_stats_per_game_df_col:
    print(index,col_name)
    index += 1
print('')

index = 0
for col_name in team_summaries_df_col:
    print(index,col_name)
    index += 1
print('')

index = 0
for col_name in team_totals_df_col:
    print(index,col_name)
    index += 1
# reordering columns in dataframes via iloc
team_abbrev_df = team_abbrev_df.iloc[:,[6,2,1,3,4,5,0]]
team_stats_per_game_df = team_stats_per_game_df.iloc[:,[29,2,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,0]]
team_summaries_df = team_summaries_df.iloc[:,[32,2,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,0]]
team_totals_df = team_totals_df.iloc[:,[29,2,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,0]]
# save changes
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)
# 1d
team_abbrev_df = team_abbrev_df.sort_values(['team'], ascending=True)
team_stats_per_game_df = team_stats_per_game_df.sort_values(['team'], ascending=True)
team_summaries_df = team_summaries_df.sort_values(['team'], ascending=True)
team_totals_df = team_totals_df.sort_values(['team'], ascending=True)
# save changes
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)
# 1e
team_abbrev_df['team_id'] = team_abbrev_df['team'].factorize()[0] + 1
team_stats_per_game_df['team_id'] = team_stats_per_game_df['team'].factorize()[0] + 1
team_summaries_df['team_id'] = team_summaries_df['team'].factorize()[0] + 1
team_totals_df['team_id'] = team_totals_df['team'].factorize()[0] + 1
# save changes
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)

print('\nmanipulate team data and add team_id to 4 team datasets and factorize per team; change order of columns per set = success', ' - ', (time.time() - start_time))
# 2
team_abbrev_df.loc[team_abbrev_df['season_ending_year'] > 2024, 'playoffs'] = 'Pending'
team_stats_per_game_df.loc[team_stats_per_game_df['season_ending_year'] > 2024, 'playoffs'] = 'Pending'
team_summaries_df.loc[team_summaries_df['season_ending_year'] > 2024, 'playoffs'] = 'Pending'
team_totals_df.loc[team_totals_df['season_ending_year'] > 2024, 'playoffs'] = 'Pending'
# save changes
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)

print('\nupdate teams in 2024-25 playoffs values from false to "pending" - in progress', ' - ', (time.time() - start_time))
# 3
def playoff_teams(df):
    try:
        return df[df['playoffs'] == True]
    except Exception as e:
        return(f'cannot filter out "League Average" values {type(e)}')
# implement filtering to respective dataframes
team_abbrev_playoff_teams_only_df = filter_out_league_average(team_abbrev_df)
team_stats_per_game_playoff_teams_only_df = filter_out_league_average(team_stats_per_game_df)
team_summaries_playoff_teams_only_df = filter_out_league_average(team_summaries_df)
team_totals_playoff_teams_only_df = filter_out_league_average(team_totals_df)    
# save changes
team_abbrev_playoff_teams_only_df.to_excel('team_abbrev_playoff_teams_only.xlsx', index=False)
team_stats_per_game_playoff_teams_only_df.to_excel('team_stats_per_game_playoff_teams_only.xlsx', index=False)
team_summaries_playoff_teams_only_df.to_excel('team_summaries_playoff_teams_only.xlsx', index=False)
team_totals_playoff_teams_only_df.to_excel('team_totals_playoff_teams_only.xlsx', index=False)

print('\ncreate separate dataframes for playoff teams only - in progress', ' - ', (time.time() - start_time))
'''

'''# TEST ONLY 1-25-2025 - COMPLETE - WILL NOT USE DUE TO COMPLEXITY OF LOGIC/VALUE TYPES IN DATAFRAME
col = list(team_totals_df.columns)
index = 0

for col_name in col:
    print(index, col_name) # season_ending_year, x2p, x2pa, x3p, x3pa
    index += 1

print('\n',team_totals_df) # COMPLETE

# filter out rows that do not have season_ending year 
#   values != 2001 through 2024 via loc method
#   create new dataframe based off the results
team_totals_field_goals_2001_to_2024_df = \
    team_totals_df.loc[(team_totals_df['season_ending_year'] >= 2001) 
                       & (team_totals_df['season_ending_year'] <= 2024)]
# filtering out rows with team = 'League Average'
team_totals_field_goals_2001_to_2024_df = \
    team_totals_field_goals_2001_to_2024_df.loc[\
        team_totals_field_goals_2001_to_2024_df['team'] != 'League Average']

print('\n',team_totals_field_goals_2001_to_2024_df.head(30)) # COMPLETE
print('\n',team_totals_field_goals_2001_to_2024_df.tail(29)) # COMPLETE

team_totals_field_goals_2001_to_2024_df.to_excel('team_totals_field_goals_2001_to_2024.xlsx', index=False)

team_totals_three_point_field_goals_2001_to_2024_pivot_table_df = pd.pivot_table(team_totals_field_goals_2001_to_2024_df,
                                                                     index='team',
                                                                     columns='season_ending_year',
                                                                     values=['x3p'])

print('\n',team_totals_three_point_field_goals_2001_to_2024_pivot_table_df) # COMPLETE

team_totals_three_point_field_goals_2001_to_2024_pivot_table_df.\
    to_excel('team_totals_three_point_field_goals_2001_to_2024_pivot_table.xlsx')
#remove top row from pivot table
team_totals_three_point_field_goals_2001_to_2024_pivot_table_df = \
    pd.read_excel('team_totals_three_point_field_goals_2001_to_2024_pivot_table.xlsx', header=1)

print('\n',team_totals_three_point_field_goals_2001_to_2024_pivot_table_df) # COMPLETE

team_totals_three_point_field_goals_2001_to_2024_pivot_table_df.\
    to_excel('team_totals_three_point_field_goals_2001_to_2024_pivot_table.xlsx', index=False) # COMPLETE
#remove top row from pivot table
team_totals_three_point_field_goals_2001_to_2024_pivot_table_df = \
    team_totals_three_point_field_goals_2001_to_2024_pivot_table_df.iloc[1:]

team_totals_three_point_field_goals_2001_to_2024_pivot_table_df.\
    to_excel('team_totals_three_point_field_goals_2001_to_2024_pivot_table.xlsx', index=False)

print('\n',team_totals_three_point_field_goals_2001_to_2024_pivot_table_df) # COMPLETE


# creating charts (2001-2024)
import matplotlib.pyplot as plt

for i in range(2000,2024):
    x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
    y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2001]
    color='orange'
    plt.barh(x, y, color=color)
    plt.title(f'total Three-Point Field Goals Made Per Team {i + 1}')
    plt.show()'''

'''# TEST ONLY 1-23-2025 - COMPLETE
col = list(team_totals_df.columns)
index = 0

for col_name in col:
    print(index, col_name) # season_ending_year, x2p, x2pa, x3p, x3pa
    index += 1

print('\n',team_totals_df) # COMPLETE

# filter out rows that do not have season_ending year 
#   values != 2001 through 2024 via loc method
#   create new dataframe based off the results
team_totals_field_goals_2001_to_2024_df = \
    team_totals_df.loc[(team_totals_df['season_ending_year'] >= 2001) 
                       & (team_totals_df['season_ending_year'] <= 2024)]
# filtering out rows with team = 'League Average'
team_totals_field_goals_2001_to_2024_df = \
    team_totals_field_goals_2001_to_2024_df.loc[\
        team_totals_field_goals_2001_to_2024_df['team'] != 'League Average']

print('\n',team_totals_field_goals_2001_to_2024_df.head(30)) # COMPLETE
print('\n',team_totals_field_goals_2001_to_2024_df.tail(29)) # COMPLETE

team_totals_field_goals_2001_to_2024_df.to_excel('team_totals_field_goals_2001_to_2024.xlsx', index=False)

team_totals_three_point_field_goals_2001_to_2024_pivot_table_df = pd.pivot_table(team_totals_field_goals_2001_to_2024_df,
                                                                     index='team',
                                                                     columns='season_ending_year',
                                                                     values=['x3p'])

print('\n',team_totals_three_point_field_goals_2001_to_2024_pivot_table_df) # COMPLETE

team_totals_three_point_field_goals_2001_to_2024_pivot_table_df.\
    to_excel('team_totals_three_point_field_goals_2001_to_2024_pivot_table.xlsx')
#remove top row from pivot table
team_totals_three_point_field_goals_2001_to_2024_pivot_table_df = \
    pd.read_excel('team_totals_three_point_field_goals_2001_to_2024_pivot_table.xlsx', header=1)

print('\n',team_totals_three_point_field_goals_2001_to_2024_pivot_table_df) # COMPLETE

team_totals_three_point_field_goals_2001_to_2024_pivot_table_df.\
    to_excel('team_totals_three_point_field_goals_2001_to_2024_pivot_table.xlsx', index=False) # COMPLETE
#remove top row from pivot table
team_totals_three_point_field_goals_2001_to_2024_pivot_table_df = \
    team_totals_three_point_field_goals_2001_to_2024_pivot_table_df.iloc[1:]

team_totals_three_point_field_goals_2001_to_2024_pivot_table_df.\
    to_excel('team_totals_three_point_field_goals_2001_to_2024_pivot_table.xlsx', index=False)

print('\n',team_totals_three_point_field_goals_2001_to_2024_pivot_table_df) # COMPLETE

print('\nteam three point field goal made from 2001-2024 seasons pivot table = success - ', (time.time() - start_time))

# creating charts (2001-2024)
import matplotlib.pyplot as plt
x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2001]
color = 'orange'
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2000-01)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2001-02)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2003]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2002-03)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2004]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2003-04)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2005]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2004-05)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2006]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2005-06)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2007]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2006-07)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2008]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2007-08)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2009]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2008-09)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2010]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2009-10)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2011]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2010-11)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2012]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2011-12)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2013]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2012-13)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2014]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2013-14)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2015]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2014-15)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2016]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2015-16)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2017]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2016-17)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2018]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2017-18)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2019]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2018-19)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2020]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2019-20)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2021]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2020-21)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2022]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2021-22)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2023]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2022-23)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()

x = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df['season_ending_year'].astype(str)
y = team_totals_three_point_field_goals_2001_to_2024_pivot_table_df[2024]
plt.barh(x, y, color=color)
plt.title('Total Three-Point Field Goals Made Per Team (2023-24)')
plt.yticks(fontsize=8)
plt.xlabel('Three-Point Field Goals Made')
plt.show()
'''


'''
# TEST ONLY 1-17-2025 - COMPLETED - SUCCESS
#  nba all-star pivot table
all_star_selections_pivot_table_df = pd.read_excel('All-Star Selections.xlsx')
# create pivot table of all-star selections
all_star_selections_pivot_table_df = pd.pivot_table(all_star_selections_pivot_table_df,
                                             index=['player'],
                                             values=['team'],
                                             aggfunc='count')
# save changes accordingly
all_star_selections_pivot_table_df.to_excel('all_star_selections_pivot_table.xlsx')
# sort values by team number values, asc should be false since we want the highest value on top
all_star_selections_pivot_table_df = all_star_selections_pivot_table_df.sort_values(by=['team'], ascending=False)
# save changes accordingly
all_star_selections_pivot_table_df.to_excel('all_star_selections_pivot_table.xlsx')
# all-star selections >= 10
all_star_selections_10_plus_pivot_table_df = \
    all_star_selections_pivot_table_df.loc[all_star_selections_pivot_table_df['team'] >= 10]
# save changes accordingly
all_star_selections_10_plus_pivot_table_df.to_excel('all_star_selections_10_plus_pivot_table.xlsx')
'''


'''
# TEST ONLY 1-16-2025 - COMPLETED - SUCCESS (note - WILL NOT ADD stls_per_game nor blks_per_game columns due to sporadic nba/aba official stat keepings)
#   filter out rows with ['tm'] == 'TOT'
#   hofer_list_and_player_per_game_df = pd.read_excel('hofer_list_and_player_per_game_df')
#       version 2 - rebounds (values should = 0)
#                   subtract num_seasons from the following player_ids:
#                       player_id = 57 (num_seasons-1) 1 
#                       player_id = 205 (num_seasons-3) 3
#                       player_id = 278 (num_seasons-2) 2
#                       player_id = 479 (num_seasons-2) 2
#                       player_id = 568 (num_seasons-2) 2
#                       player_id = 749 (num_seasons-3) 3
#                       player_id = 1401 (num_seasons-1) 1 
#                       player_id = 1434 (num_seasons-1) 1 
#                       player_id = 1599 (num_seasons-1) 1 
#                       player_id = 1909 (num_seasons-2) 2
#                       player_id = 2074 (num_seasons-2) 2
#                       player_id = 2617 (num_seasons-2) 2
#                       player_id = 2679 (num_seasons-1) 1 
#                       player_id = 4620 (num_seasons-1) 1 
#                       player_id = 5051 (num_seasons-1) 1 
#       
#      version 3 - steals and blocks (values should = 0)
#                   subtract num_seasons from certain player_ids   
#
# VERSION 2 - COMPLETE                
hofer_list_and_player_per_game_df_version_2 = pd.read_excel('hofers_list_and_player_per_game.xlsx')
# change 'N/A - Stat tracked as of the 1950-51 NBA Season' value to '0' (zero) 
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['season_ending_year'] < 1951, 'trb_per_game'] = 0
# save changes
hofer_list_and_player_per_game_df_version_2.to_excel('hofer_list_and_player_per_game_version_2.xlsx', index=False)
# filter out rows that have ['tm'] == TOT
hofer_list_and_player_per_game_df_version_2 = hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['tm'] != 'TOT']
# save changes
hofer_list_and_player_per_game_df_version_2.to_excel('hofer_list_and_player_per_game_version_2.xlsx', index=False)
# groupby implemented to display games and points per game averages for the hall-of-famers
hofer_list_and_player_per_game_df_version_2 = hofer_list_and_player_per_game_df_version_2.groupby(
        ['player_id',
         'player_x',
         'birth_year_x',
         'hof']
         ).agg({
        'num_seasons': "max",
        'first_season': "min", 
        'last_season': "max",
        'trb_per_game': "sum"} # trb only
    ).reset_index()
# save changes
hofer_list_and_player_per_game_df_version_2.to_excel('hofer_list_and_player_per_game_version_2.xlsx', index=False)
# update num_seasons values for players who played prior to the 1950-51 nba season
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 57, 'num_seasons'] = 3
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 205, 'num_seasons'] = 8
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 278, 'num_seasons'] = 8
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 479, 'num_seasons'] = 5
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 568, 'num_seasons'] = 7
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 749, 'num_seasons'] = 10
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 1401, 'num_seasons'] = 10
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 1434, 'num_seasons'] = 14
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 1599, 'num_seasons'] = 9
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 1909, 'num_seasons'] = 5
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 2074, 'num_seasons'] = 8
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 2617, 'num_seasons'] = 5
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 2679, 'num_seasons'] = 4
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 4620, 'num_seasons'] = 10
hofer_list_and_player_per_game_df_version_2.loc[hofer_list_and_player_per_game_df_version_2['player_id'] == 5051, 'num_seasons'] = 9
# save changes
hofer_list_and_player_per_game_df_version_2.to_excel('hofer_list_and_player_per_game_version_2.xlsx', index=False)
# calculations - 
hofer_list_and_player_per_game_df_version_2['trb_per_game'] = hofer_list_and_player_per_game_df_version_2.apply(lambda row: row['trb_per_game'] / row['num_seasons'], axis=1)
# save changes
hofer_list_and_player_per_game_df_version_2.to_excel('hofer_list_and_player_per_game_version_2.xlsx', index=False)
# round values 2 decimal spaces
hofer_list_and_player_per_game_df_version_2['trb_per_game'] = hofer_list_and_player_per_game_df_version_2['trb_per_game'].apply(lambda row: round(row, 2))
# save changes
hofer_list_and_player_per_game_df_version_2.to_excel('hofer_list_and_player_per_game_version_2.xlsx', index=False)
# copy trb_per_game column from version_2 to main hofer_list_and_player_per_game_df (averages list is the main dataframe/sheet for all hofers)
#hofers_list_and_player_per_game_df['trb_per_game'] = hofer_list_and_player_per_game_df_version_2['trb_per_game']
# save changes
#hofers_list_and_player_per_game_df.to_excel('hofer_list_and_player_per_game_averages.xlsx', index=False)
'''

'''
# TEST ONLY 1-16-2025 - COMPLETE - SUCCESS
#   hofers_list_and_player_per_game_df (DATAFRAME) = SUCCESS
#   player_id -> ASC seas_id -> DSC = SUCCESS
#   remove rows with df['tm'] == 'TOT' = SUCCESS
#   formula -> ex: df['pts_per_game'].sum / df['num_seasons'] - IN PROGRESS
hofers_list_and_player_per_game_df = pd.read_excel('hofers_list_and_player_per_game.xlsx')
# sort values in dataframe by player_id and season_ending_year
hofers_list_and_player_per_game_df = \
    hofers_list_and_player_per_game_df.\
        sort_values(by=['player_id', 'season_ending_year'], 
                    ascending=[True, False])
# save changes
hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game.xlsx', index=False)
# filter out rows that have ['tm'] == TOT
hofers_list_and_player_per_game_df.loc[hofers_list_and_player_per_game_df['tm'] != 'TOT']
# save changes
hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game_averages.xlsx', index=False)
# groupby implemented to display games and points per game averages for the hall-of-famers
hofers_list_and_player_per_game_df = hofers_list_and_player_per_game_df.groupby(
        ['player_id',
         'player_x',
         'birth_year_x',
         'hof',
         'num_seasons',
         'first_season',
         'last_season']
         ).agg({
        'g': "sum",
        'pts_per_game': "sum"
        }
    ).reset_index()
# save changes
hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game_averages.xlsx', index=False)
# calcuations
hofers_list_and_player_per_game_df['g'] = hofers_list_and_player_per_game_df.apply(lambda row: row['g'] / row['num_seasons'], axis=1)
hofers_list_and_player_per_game_df['pts_per_game'] = hofers_list_and_player_per_game_df.apply(lambda row: row['pts_per_game'] / row['num_seasons'], axis=1)
# save changes   
hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game_averages.xlsx', index=False)
# round values 2 decimal spaces
hofers_list_and_player_per_game_df['g'] = hofers_list_and_player_per_game_df['g'].apply(lambda row: round(row, 2))
hofers_list_and_player_per_game_df['pts_per_game'] = hofers_list_and_player_per_game_df['pts_per_game'].apply(lambda row: round(row, 2))
# save changes
hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game_averages.xlsx', index=False)
'''


'''
# TEST ONLY 1-14-2025 - COMPLETE - SUCCESS
#   hof updates to appropriate rows in player_career_info_df
#player_career_info_df['hof'] = player_career_info_df['hof'].replace(False, 'No')
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)

player_career_info_df.loc[(player_career_info_df['player'] == 'Bill Bradley') & 
                          (player_career_info_df['birth_year'].astype(int) == 1941), 'hof'] = 'No'

player_career_info_df.loc[(player_career_info_df['player'] == 'Bobby Jones') & 
                          (player_career_info_df['birth_year'].astype(int) == 1983), 'hof'] = 'No'

player_career_info_df.loc[(player_career_info_df['player'] == 'Roger Brown') & 
                          (player_career_info_df['birth_year'].astype(int) == 1950), 'hof'] = 'No'

player_career_info_df.to_excel('test.xlsx', index=False)
'''


'''
# TEST ONLY 1-13-2025 - COMPLETE - SUCCESS
player_career_info_df = \
    player_career_info_df.drop(player_career_info_df.iloc[:, 7:13], axis=1)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)

print(player_career_info_df)
'''

'''
# TEST ONLY 1-13-2025 - COMPLETE - SUCCESS
# web scraping from basketball-reference.com
url = \
    pd.read_html('https://www.basketball-reference.com/awards/hof.html')

data = url

print(len(data)) # how many tables there are on the basketball-reference.com
print(data[0])

hofers_list_df = url[0]

hofers_list_df.to_excel('hofers.xlsx')

cols = list(hofers_list_df.columns)
index = 0

for x in cols:
    print(index, x)
    index += 1

hofers_list_df = pd.read_excel('hofers.xlsx', header=1) # removes first row of dataset

hofers_list_df.to_excel('hofers.xlsx', index=False)

print(hofers_list_df)
print('')
# rename column Name to Player
hofers_list_df = hofers_list_df.rename(columns={'Name': 'player'}) 

hofers_list_df.to_excel('hofers.xlsx', index=False)

print(hofers_list_df)
print('')
# remove first row
hofers_list_df = hofers_list_df.iloc[1:]

hofers_list_df.to_excel('hofers.xlsx', index=False)

print(hofers_list_df)
print('')
# filter out all rows that do not contain 'Player'
hofers_list_df = hofers_list_df.loc[hofers_list_df['Category'] == 'Player']

hofers_list_df.to_excel('hofers.xlsx', index=False)

print(hofers_list_df)
print('')
# array of words to be removed
words_to_be_removed = ["WNBA", "Int'l", "/", "CBB Player", "Coach", "Exec", "Oly", "CBB Coach"]
hofers_list_df['player'] = [' '.join([item for item in x.split(' ')[:2]
                          if item not in words_to_be_removed])
                          for x in hofers_list_df['player']]

hofers_list_df.to_excel('hofers.xlsx', index=False)

print(hofers_list_df)
'''

'''
# TEST 1-14-2025 - COMPLETE - SUCCESS
hofers_list_df = pd.read_excel('hofers.xlsx')
# merge both player_career_info_df and hofers
player_career_info_df = pd.merge(player_career_info_df,
                hofers_list_df,
                how='outer',
                left_index=True,
                right_index=True)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
# python pandas simple xlookup/vlookup version
player_career_info_df['hof'] = player_career_info_df['player_x'].isin(player_career_info_df['player_y'])

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)

print(player_career_info_df)
'''

'''
# TEST ONLY 1-12-2025 - COMPLETE - WILL NOT USE
def player_per_game_highlighted(x):
    if x == 'N/A - Stat tracked as of the 1973-74 NBA Season':
        return 'background-color: yellow'

player_per_game_df.style.apply(player_per_game_highlighted)

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
'''

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
        elif player_id == 0:
            print('please enter a number greater than zero')
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

    try:
        player = input("enter player's name: ")

        if player == 'exit':
            break

        if player in player_values:
            #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 4:28], axis=1)
            #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 8:10], axis=1)
            #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 0:1], axis=1)
            #player_per_game_df = player_per_game_df.drop(player_per_game_df.iloc[:, 1:2], axis=1)
            print(f"{player_per_game_df[(player_per_game_df['player'] == player)]}")
        elif player not in player_values:
            print('not exist')
        else:
            continue
    except ValueError:
        print('please enter a number only')
        continue

# look up player and year they played in look up player in player_per_game_df
print(f"\nlook up player (first name and last name required) " 
      f"and year they played in player_per_game_df")

player_values = list(player_per_game_df['player'].values)
year_values = list(player_per_game_df['year'].values)

while True:
    try:

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
    except ValueError:
        print('please enter a number only')
        continue        

# =========================== #

