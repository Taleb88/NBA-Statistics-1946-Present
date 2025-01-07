# TESTING VARIOUS QUERIES
import pandas as pd

player_per_game_df = pd.read_excel('Player Per Game.xlsx')
player_career_info_df = pd.read_excel('Player Career Info.xlsx')
player_season_info_df = pd.read_excel('Player Season Info.xlsx')
player_shooting_df = pd.read_excel('Player Shooting.xlsx')
player_totals_df = pd.read_excel('Player Totals.xlsx')

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


# Pete Smith
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1470,'birth_year'] = 1947
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1470,'birth_year'] = 1947
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1470,'birth_year'] = 1947
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)


'''
# =================#
# groupby 
# =================#

# player_award_shares_df
player_award_shares_df = pd.read_excel('Player Award Shares.xlsx')

grouped = player_award_shares_df.groupby(['player', 'award']).agg(
    first_place_votes_avg = ('first', 'mean')
)
print(grouped)

grouped.to_excel('test.xlsx')

print('')

grouped = player_award_shares_df.groupby('player')['pts_won'].mean()
print(grouped)

print('')
# team_summaries_df
team_summaries_df = pd.read_excel('Team Summaries.xlsx')
grouped = team_summaries_df.groupby('team').agg(
    player_age_average=('age', 'mean'),
    reg_season_win_average=('w', 'mean'),
    reg_season_loss_average=('l', 'mean')
)
print(grouped.head(50))

print('')

grouped = team_summaries_df.groupby('team').filter(lambda row: row['w'].mean() < 20.0)
print(grouped.head(50).sort_values(by='team', ascending=True))


players = list(player_per_game_df.values)
index = 0

# checking to see if players have an age of '0' in multiple datasets
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
      )


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


# ===================== #
# interacting with user 
# ===================== #

# look up player in player_per_game_df
print('\nlook up player (first name and last name required) in player_per_game_df')

player_values = list(player_per_game_df['player'].values)

while True:

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


# look up player and year they played in look up player in player_per_game_df
print(f"\nlook up player (first name and last name required) " 
      f"and year they played in player_per_game_df")

player_values = list(player_per_game_df['player'].values)
year_values = list(player_per_game_df['year'].values)

while True:

    player.lower = input("enter player's name: ")
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
'''