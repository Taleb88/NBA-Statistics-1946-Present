import pandas as pd

advanced_df = pd.read_csv('csv/advanced.csv')
all_star_selections_df = pd.read_csv('csv/All-Star Selections.csv')
end_of_season_teams_voting_df = pd.read_csv('csv/End of Season Teams (Voting).csv')
end_of_season_teams_df = pd.read_csv('csv/End of Season Teams.csv')
opponent_stats_per_100_poss_df = pd.read_csv('csv/Opponent Stats Per 100 Poss.csv')
opponent_stats_per_game_df = pd.read_csv('csv/Opponent Stats Per Game.csv')
opponent_totals_df = pd.read_csv('csv/Opponent Totals.csv')
per_36_minutes_df = pd.read_csv('csv/Per 36 Minutes.csv')
per_100_poss_df = pd.read_csv('csv/Per 100 Poss.csv')
player_award_shares_df = pd.read_csv('csv/Player Award Shares.csv')
player_career_info_df = pd.read_csv('csv/Player Career Info.csv')
player_per_game_df = pd.read_csv('csv/Player Per Game.csv')
player_play_by_play_df = pd.read_csv('csv/Player Play By Play.csv')
player_season_info_df = pd.read_csv('csv/Player Season Info.csv')
player_shooting_df = pd.read_csv('csv/Player Shooting.csv')
player_totals_df = pd.read_csv('csv/Player Totals.csv')
team_abbrev_df = pd.read_csv('csv/Team Abbrev.csv')
team_stats_per_100_poss_df = pd.read_csv('csv/Team Stats Per 100 Poss.csv')
team_stats_per_game_df = pd.read_csv('csv/Team Stats Per Game.csv')
team_summaries_df = pd.read_csv('csv/Team Summaries.csv')
team_totals_df = pd.read_csv('csv/Team Totals.csv')

#print(player_award_shares_df)
#print(player_per_game_df)


# groupby
player_award_shares_df.groupby(['award', 'player'])
print(player_award_shares_df.head())

#merging 
player_award_shares_and_player_per_game_merged_df = pd.merge(player_award_shares_df,
                                                          player_per_game_df, 
                                                          on=['player_id'])

#print(player_award_shares_and_player_per_game_merged_df)

player_award_shares_and_player_per_game_merged_df.\
    to_excel('player_award_shares_and_player_per_game_merged.xlsx', index=False)


# defining a player class that corresponds to the 
#   player_award_shares_and_player_per_game_merged dataframe
class Player:
    def __init__(self, name, season, award, pts_per_game):
        self.name = name
        self.season = season
        self.award = award
        self.pts_per_game = pts_per_game

    def info(self):
        return f"{self.name} won the {self.season} {self.award} while averaging {self.pts_per_game} points per game."
    
value = player_award_shares_and_player_per_game_merged_df.iloc[5]

player_instance = Player(name=value['player_x'], 
                         season=value['season_x'], 
                         award=value['award'],
                         pts_per_game=value['pts_per_game'])

print(player_instance.info())


# converting values to string format
player_award_shares_and_player_per_game_merged_df['winner'] = \
    player_award_shares_and_player_per_game_merged_df['winner'].astype(str)

# changing 'nan' values to 'True' in Bobby Jones' case - 1983 sixth man of the year
player_award_shares_and_player_per_game_merged_df['winner'] = \
    player_award_shares_and_player_per_game_merged_df['winner'].replace('nan', 'True')


# nba mvp and top 10 highest scoring averages
def nba_mvp_ppg(df):
    try:
        return df[(df['award'] == 'nba mvp') & 
                  (df['winner'] == 'True') & 
                  (df['season_x'] == df['season_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

top_5_nba_mvp_ppg_df = nba_mvp_ppg(player_award_shares_and_player_per_game_merged_df)
top_10_nba_mvp_ppg_df = nba_mvp_ppg(player_award_shares_and_player_per_game_merged_df)

top_5_nba_mvp_ppg_df.to_excel('top_5_nba_mvp_ppg_df.xlsx', index=False)
top_10_nba_mvp_ppg_df.to_excel('top_10_nba_mvp_ppg_df.xlsx', index=False)

# sort values by pts_per_game
top_5_nba_mvp_ppg_df = top_5_nba_mvp_ppg_df.sort_values(['pts_per_game'], ascending=False).head(5)
top_10_nba_mvp_ppg_df = top_10_nba_mvp_ppg_df.sort_values(['pts_per_game'], ascending=False).head(10)

top_5_nba_mvp_ppg_df.to_excel('top_5_nba_mvp_ppg_df.xlsx', index=False)
top_10_nba_mvp_ppg_df.to_excel('top_10_nba_mvp_ppg_df.xlsx', index=False)
# drop unnecessary columns from top_5_nba_mvp_ppg_df
top_5_nba_mvp_ppg_df = \
    top_5_nba_mvp_ppg_df.drop(top_5_nba_mvp_ppg_df.iloc[:,6:45], axis=1)
# drop unnecessary columns from top_10_nba_mvp_ppg_df
top_10_nba_mvp_ppg_df = \
    top_10_nba_mvp_ppg_df.drop(top_10_nba_mvp_ppg_df.iloc[:,6:45], axis=1)
# drop unnecessary columns from top_5_nba_mvp_ppg_df
top_5_nba_mvp_ppg_df = \
    top_5_nba_mvp_ppg_df.drop(['first'], axis=1)
# drop unnecessary columns from top_10_nba_mvp_ppg_df
top_10_nba_mvp_ppg_df = \
    top_10_nba_mvp_ppg_df.drop(['first'], axis=1)


#print(top_10_nba_mvp_ppg_df)
# rename certain columns in top_5_nba_mvp_ppg_df
top_5_nba_mvp_ppg_df = top_5_nba_mvp_ppg_df.rename(columns={'season_x': 'season',
                                                            'player_x': 'player',
                                                            'age_x': 'age',
                                                            'tm_x':'team'})
# rename certain columns in top_10_nba_mvp_ppg_df
top_10_nba_mvp_ppg_df = top_10_nba_mvp_ppg_df.rename(columns={'season_x': 'season',
                                                            'player_x': 'player',
                                                            'age_x': 'age',
                                                            'tm_x':'team'})
#print(top_10_nba_mvp_ppg_df)
top_5_nba_mvp_ppg_df.to_excel('top_5_nba_mvp_ppg_df.xlsx', index=False)
top_10_nba_mvp_ppg_df.to_excel('top_10_nba_mvp_ppg_df.xlsx', index=False)


# creating graphs
import matplotlib.pyplot as plt
# top 5 nba mvp ppg
x = top_5_nba_mvp_ppg_df['player'].astype(str) + '\n' +\
      top_5_nba_mvp_ppg_df['season'].astype(str) + '\n' +\
      top_5_nba_mvp_ppg_df['pts_per_game'].astype(str) + ' Points Per Game' +\
      '\n'
y = top_5_nba_mvp_ppg_df['pts_per_game']
color = 'orange'
plt.bar(x, y, color=color)
plt.title('NBA MVP Winners Points Per Game Average - Top 5')
plt.xlabel('PLAYERS')
plt.ylabel('POINTS PER GAME')
plt.show()
# top 10 nba mvp ppg
x = top_10_nba_mvp_ppg_df['player'].astype(str) + '\n' +\
      top_10_nba_mvp_ppg_df['season'].astype(str) + '\n' +\
      top_10_nba_mvp_ppg_df['pts_per_game'].astype(str) + ' PPG' +\
      '\n'
y = top_10_nba_mvp_ppg_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('NBA MVP Winners Points Per Game Average - Top 10')
plt.xlabel('PLAYERS')
plt.ylabel('POINTS PER GAME')
plt.show()


# conditional formatting
def award_winners_highlighted(x):
    try:
        if x == 'True':
            return 'background-color: green'
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

player_award_shares_and_player_per_game_merged_styled_df = (
    player_award_shares_and_player_per_game_merged_df.
    style.
    applymap(award_winners_highlighted, subset=['winner'])
)

player_award_shares_and_player_per_game_merged_styled_df.to_excel('player_award_shares_and_player_per_game_merged.xlsx', index=False)