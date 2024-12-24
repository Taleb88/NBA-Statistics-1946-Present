import pandas as pd
# read csv
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

# creating copies of csvs into xlsx
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)


#print(player_award_shares_df)
#print(player_per_game_df)

# convert season values to str
advanced_df['season'] = advanced_df['season'].astype(str)
all_star_selections_df['season'] = all_star_selections_df['season'].astype(str)
end_of_season_teams_voting_df['season'] = end_of_season_teams_voting_df['season'].astype(str)
end_of_season_teams_df['season'] = end_of_season_teams_df['season'].astype(str)
opponent_stats_per_100_poss_df['season'] = opponent_stats_per_100_poss_df['season'].astype(str)
opponent_stats_per_game_df['season'] = opponent_stats_per_game_df['season'].astype(str)
opponent_totals_df['season'] = opponent_totals_df['season'].astype(str)
per_36_minutes_df['season'] = per_36_minutes_df['season'].astype(str)
per_100_poss_df['season'] = per_100_poss_df['season'].astype(str)
player_award_shares_df['season'] = player_award_shares_df['season'].astype(str)
player_career_info_df['first_seas'] = player_career_info_df['first_seas'].astype(str) # first_seas
player_career_info_df['last_seas'] = player_career_info_df['last_seas'].astype(str) # last_seas
player_per_game_df['season'] = player_per_game_df['season'].astype(str)
player_play_by_play_df['season'] = player_play_by_play_df['season'].astype(str)
player_season_info_df['season'] = player_season_info_df['season'].astype(str)
player_shooting_df['season'] = player_shooting_df['season'].astype(str)
player_totals_df['season'] = player_totals_df['season'].astype(str)
team_abbrev_df['season'] = team_abbrev_df['season'].astype(str)
team_stats_per_100_poss_df['season'] = team_stats_per_100_poss_df['season'].astype(str)
team_stats_per_game_df['season'] = team_stats_per_game_df['season'].astype(str)
team_summaries_df['season'] = team_summaries_df['season'].astype(str)
team_totals_df['season'] = team_totals_df['season'].astype(str)

# saving updated season value conversions to all files
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)

# changing name of season column to year
def year(df):
    try:
        return df.rename(columns={'season': 'year'})
    except:
        print('cannot change name of column')

advanced_df = year(advanced_df)
all_star_selections_df = year(all_star_selections_df)
end_of_season_teams_voting_df = year(end_of_season_teams_voting_df)
end_of_season_teams_df = year(end_of_season_teams_df)
opponent_stats_per_100_poss_df = year(opponent_stats_per_100_poss_df)
opponent_stats_per_game_df = year(opponent_stats_per_game_df)
opponent_totals_df = year(opponent_totals_df)
per_36_minutes_df = year(per_36_minutes_df)
per_100_poss_df = year(per_100_poss_df)
player_award_shares_df = year(player_award_shares_df)
#player_career_info_df = year(player_career_info_df)
player_per_game_df = year(player_per_game_df)
player_play_by_play_df = year(player_play_by_play_df)
player_season_info_df = year(player_season_info_df)
player_shooting_df = year(player_shooting_df)
player_totals_df = year(player_totals_df)
team_abbrev_df = year(team_abbrev_df)
team_stats_per_100_poss_df = year(team_stats_per_100_poss_df)
team_stats_per_game_df = year(team_stats_per_game_df)
team_summaries_df = year(team_summaries_df)
team_totals_df = year(team_totals_df)

# saving changes to all files
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)

# adding season column to all dataframes, will be the last column
advanced_df['season'] = advanced_df['year']
all_star_selections_df['season'] = all_star_selections_df['year']
end_of_season_teams_voting_df['season'] = end_of_season_teams_voting_df['year']
end_of_season_teams_df['season'] = end_of_season_teams_df['year']
opponent_stats_per_100_poss_df['season'] = opponent_stats_per_100_poss_df['year']
opponent_stats_per_game_df['season'] = opponent_stats_per_game_df['year']
opponent_totals_df['season'] = opponent_totals_df['year']
per_36_minutes_df['season'] = per_36_minutes_df['year']
per_100_poss_df['season'] = per_100_poss_df['year']
player_award_shares_df['season'] = player_award_shares_df['year']
#player_career_info_df['season'] = player_career_info_df['year']
player_per_game_df['season'] = player_per_game_df['year']
player_play_by_play_df['season'] = player_play_by_play_df['year']
player_season_info_df['season'] = player_season_info_df['year']
player_shooting_df['season'] = player_shooting_df['year']
player_totals_df['season'] = player_totals_df['year']
team_abbrev_df['season'] = team_abbrev_df['year']
team_stats_per_100_poss_df['season'] = team_stats_per_100_poss_df['year']
team_stats_per_game_df['season'] = team_stats_per_game_df['year']
team_summaries_df['season'] = team_summaries_df['year']
team_totals_df['season'] = team_totals_df['year']


# saving changes to all files
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)


# define function that corrects season value 
#   ex: 1956 -> 1955-56
def season_values(df):
    try:
        return df.replace(to_replace={'season': {'1947': '1946-47', 
                                                '1948': '1947-48',
                                                '1949': '1948-49',
                                                '1950': '1949-50',
                                                '1951': '1950-51',
                                                '1952': '1951-52',
                                                '1953': '1952-53',
                                                '1954': '1953-54',
                                                '1955': '1954-55',
                                                '1956': '1955-56',
                                                '1957': '1956-57',
                                                '1958': '1957-58',
                                                '1959': '1958-59',
                                                '1960': '1959-60',
                                                '1961': '1960-61',
                                                '1962': '1960-62',
                                                '1963': '1962-63',
                                                '1964': '1963-64',
                                                '1965': '1964-65',
                                                '1966': '1965-66',
                                                '1967': '1966-67',
                                                '1968': '1967-68',
                                                '1969': '1968-69',
                                                '1970': '1969-70',
                                                '1971': '1970-71',
                                                '1972': '1971-72',
                                                '1973': '1972-73',
                                                '1974': '1973-74',
                                                '1975': '1974-75',
                                                '1976': '1975-76',
                                                '1977': '1976-77',
                                                '1978': '1977-78',
                                                '1979': '1978-79',
                                                '1980': '1979-80',
                                                '1981': '1980-81',
                                                '1982': '1981-82',
                                                '1983': '1982-83',
                                                '1984': '1983-84',
                                                '1985': '1984-85',
                                                '1986': '1985-86',
                                                '1987': '1986-87',
                                                '1988': '1987-88',
                                                '1989': '1988-89',
                                                '1990': '1989-90',
                                                '1991': '1990-91',
                                                '1992': '1991-92',
                                                '1993': '1992-93',
                                                '1994': '1993-94',
                                                '1995': '1994-95',
                                                '1996': '1995-06',
                                                '1997': '1996-97',
                                                '1998': '1997-98',
                                                '1999': '1998-99',
                                                '2000': '1999-00',
                                                '2001': '2000-01',
                                                '2002': '2001-02',
                                                '2003': '2002-03',
                                                '2004': '2003-04',
                                                '2005': '2004-05',
                                                '2006': '2005-06',
                                                '2007': '2006-07',
                                                '2008': '2007-08',
                                                '2009': '2008-09',
                                                '2010': '2009-10',
                                                '2011': '2010-11',
                                                '2012': '2011-12',
                                                '2013': '2012-13',
                                                '2014': '2013-14',
                                                '2015': '2014-15',
                                                '2016': '2015-16',
                                                '2017': '2016-17',
                                                '2018': '2017-18',
                                                '2019': '2018-19',
                                                '2020': '2019-20',
                                                '2021': '2020-21',
                                                '2022': '2021-22',
                                                '2023': '2022-23',
                                                '2024': '2023-24',
                                                '2025': '2024-25'
                                                }}) 
    except Exception as e:
        print(f'caught {type(e)}: e \n'
            f'cannot list results')

advanced_df = season_values(advanced_df)
all_star_selections_df = season_values(all_star_selections_df)
end_of_season_teams_voting_df = season_values(end_of_season_teams_voting_df)
end_of_season_teams_df = season_values(end_of_season_teams_df)
opponent_stats_per_100_poss_df = season_values(opponent_stats_per_100_poss_df)
opponent_stats_per_game_df = season_values(opponent_stats_per_game_df)
opponent_totals_df = season_values(opponent_totals_df)
per_36_minutes_df = season_values(per_36_minutes_df)
per_100_poss_df = season_values(per_100_poss_df)
player_award_shares_df = season_values(player_award_shares_df)
#player_career_info_df = season_values(player_career_info_df)
player_per_game_df = season_values(player_per_game_df)
player_play_by_play_df = season_values(player_play_by_play_df)
player_season_info_df = season_values(player_season_info_df)
player_shooting_df = season_values(player_shooting_df)
player_totals_df = season_values(player_totals_df)
team_abbrev_df = season_values(team_abbrev_df)
team_stats_per_100_poss_df = season_values(team_stats_per_100_poss_df)
team_stats_per_game_df = season_values(team_stats_per_game_df)
team_summaries_df = season_values(team_summaries_df)
team_totals_df = season_values(team_totals_df)

# saving changes to all files
advanced_df.to_excel('advanced.xlsx', index=False)
all_star_selections_df.to_excel('All-Star Selections.xlsx', index=False)
end_of_season_teams_voting_df.to_excel('End of Season Teams (Voting).xlsx', index=False)
end_of_season_teams_df.to_excel('End of Season Teams.xlsx', index=False)
opponent_stats_per_100_poss_df.to_excel('Opponent Stats Per 100 Poss.xlsx', index=False)
opponent_stats_per_game_df.to_excel('Opponent Stats Per Game.xlsx', index=False)
opponent_totals_df.to_excel('Opponent Totals.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
player_award_shares_df.to_excel('Player Award Shares.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
team_abbrev_df.to_excel('Team Abbrev.xlsx', index=False)
team_stats_per_100_poss_df.to_excel('Team Stats Per 100 Poss.xlsx', index=False)
team_stats_per_game_df.to_excel('Team Stats Per Game.xlsx', index=False)
team_summaries_df.to_excel('Team Summaries.xlsx', index=False)
team_totals_df.to_excel('Team Totals.xlsx', index=False)


# CREATING DOUBLE-DOUBLE AND TRIPLE-DOUBLE COLUMNS (VALUES = YES/NO) in player_per_game_df
player_per_game_df['double_double_avg'] = [''] * len(player_per_game_df)

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
# checking to see what positions trb_per_game, ast_per_game, stl_per_game, blk_per_game, and pts_per_game are located at
# result -> [28 29 30 31 34]  (ADD 1 TO EACH ELEMENT INDEX) -> [29 30 31 32 35]
print(player_per_game_df.columns.get_indexer(['trb_per_game', 'ast_per_game', 'stl_per_game', 'blk_per_game', 'pts_per_game']))
# determine if a player have averged a double-double in a season via list comprehension, placing 'Yes' or 'No' values in double_double_avg column
player_per_game_df['double_double_avg'] = ['Yes' 
                                           if x[29] >= 10.0 and x[30] >= 10.0 or 
                                           x[29] >= 10.0 and x[31] >= 10.0 or
                                           x[29] >= 10.0 and x[32] >= 10.0 or
                                           x[29] >= 10.0 and x[35] >= 10.0 or
                                           x[30] >= 10.0 and x[29] >= 10.0 or
                                           x[30] >= 10.0 and x[31] >= 10.0 or
                                           x[30] >= 10.0 and x[32] >= 10.0 or
                                           x[30] >= 10.0 and x[35] >= 10.0 or
                                           x[31] >= 10.0 and x[29] >= 10.0 or
                                           x[31] >= 10.0 and x[30] >= 10.0 or
                                           x[31] >= 10.0 and x[32] >= 10.0 or
                                           x[31] >= 10.0 and x[35] >= 10.0 or
                                           x[32] >= 10.0 and x[29] >= 10.0 or
                                           x[32] >= 10.0 and x[30] >= 10.0 or
                                           x[32] >= 10.0 and x[31] >= 10.0 or
                                           x[32] >= 10.0 and x[35] >= 10.0 or
                                           x[35] >= 10.0 and x[29] >= 10.0 or
                                           x[35] >= 10.0 and x[30] >= 10.0 or
                                           x[35] >= 10.0 and x[31] >= 10.0 or
                                           x[35] >= 10.0 and x[32] >= 10.0                                                                                                                                                                                                                                                                
                                           else "No" 
                                           for x in player_per_game_df.itertuples()] 

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df['triple_double_avg'] = [''] * len(player_per_game_df)
# determine if a player have averged a triple-double in a season via list comprehension, placing 'Yes' or 'No' values in triple_double_avg column
player_per_game_df['triple_double_avg'] = ['Yes' 
                                           if x[29] >= 10.0 and x[30] >= 10.0 and x[31] >= 10.0 or 
                                           x[29] >= 10.0 and x[30] >= 10.0 and x[32] >= 10.0 or 
                                           x[29] >= 10.0 and x[30] >= 10.0 and x[35] >= 10.0 or
                                           x[29] >= 10.0 and x[31] >= 10.0 and x[32] >= 10.0 or
                                           x[29] >= 10.0 and x[31] >= 10.0 and x[35] >= 10.0 or
                                           x[29] >= 10.0 and x[32] >= 10.0 and x[35] >= 10.0 or
                                           x[30] >= 10.0 and x[31] >= 10.0 and x[32] >= 10.0 or
                                           x[30] >= 10.0 and x[31] >= 10.0 and x[35] >= 10.0 or
                                           x[30] >= 10.0 and x[32] >= 10.0 and x[35] >= 10.0 or 
                                           x[31] >= 10.0 and x[32] >= 10.0 and x[35] >= 10.0
                                           else "No" 
                                           for x in player_per_game_df.itertuples()] 

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

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
    def __init__(self, name, year, award, pts_per_game):
        self.name = name
        self.year = year
        self.award = award
        self.pts_per_game = pts_per_game

    def info(self):
        try:
            return f"{self.name} won the {self.year} {self.award} while averaging {self.pts_per_game} points per game."
        except Exception as e:
            print(f'caught {type(e)}: e \n'
                f'cannot list results')
    
value = player_award_shares_and_player_per_game_merged_df.iloc[5]

player_instance = Player(name=value['player_x'], 
                         year=value['year_x'], 
                         award=value['award'],
                         pts_per_game=value['pts_per_game'])

print(player_instance.info())

# converting values to string format
player_award_shares_and_player_per_game_merged_df['winner'] = \
    player_award_shares_and_player_per_game_merged_df['winner'].astype(str)

# changing 'nan' values to 'True' in Bobby Jones' case - 1983 sixth man of the year
player_award_shares_and_player_per_game_merged_df['winner'] = \
    player_award_shares_and_player_per_game_merged_df['winner'].replace('nan', 'True')


# ================== #
# filtering #
# ================== #

# finding unique values under 'award' column
# result -> ['clutch_poy' 'dpoy' 'mip' 'nba mvp' 'nba roy' 'smoy' 'aba mvp' 'aba roy']
print(player_award_shares_and_player_per_game_merged_df['award'].unique())
# award winners
# clutch poy
def clutch_poy_winners(df):
    try:
        return df[(df['award'] == 'clutch_poy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y']) ]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

clutch_poy_winners_df = clutch_poy_winners(player_award_shares_and_player_per_game_merged_df)

clutch_poy_winners_df.to_excel('clutch_poy_winners.xlsx', index=False)
# dpoy
def dpoy_winners(df):
    try:
        return df[(df['award'] == 'dpoy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

dpoy_winners_df = dpoy_winners(player_award_shares_and_player_per_game_merged_df)

dpoy_winners_df.to_excel('dpoy_winners.xlsx', index=False)
# mip (most improved player)
def mip_winners(df):
    try:
        return df[(df['award'] == 'mip') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

mip_winners_df = mip_winners(player_award_shares_and_player_per_game_merged_df)

mip_winners_df.to_excel('mip_winners.xlsx', index=False)
# nba mvp
def nba_mvp_winners(df):
    try:
        return df[(df['award'] == 'nba mvp') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

nba_mvp_winners_df = nba_mvp_winners(player_award_shares_and_player_per_game_merged_df)

nba_mvp_winners_df.to_excel('nba_mvp_winners.xlsx', index=False)
# nba roy (rookie of the year)
def nba_roy_winners(df):
    try:
        return df[(df['award'] == 'nba roy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

nba_roy_winners_df = nba_roy_winners(player_award_shares_and_player_per_game_merged_df)

nba_roy_winners_df.to_excel('nba_roy_winners.xlsx', index=False)
# smoy (6th man of the year)
def smoy_winners(df):
    try:
        return df[(df['award'] == 'smoy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

smoy_winners_df = smoy_winners(player_award_shares_and_player_per_game_merged_df)

smoy_winners_df.to_excel('smoy_winners.xlsx', index=False)
# aba mvp
def aba_mvp_winners(df):
    try:
        return df[(df['award'] == 'aba mvp') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

aba_mvp_winners_df = aba_mvp_winners(player_award_shares_and_player_per_game_merged_df)

aba_mvp_winners_df.to_excel('aba_mvp_winners.xlsx', index=False)
# aba roy (rookie of the year)
def aba_roy_winners(df):
    try:
        return df[(df['award'] == 'aba roy') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')

aba_roy_winners_df = aba_roy_winners(player_award_shares_and_player_per_game_merged_df)

aba_roy_winners_df.to_excel('aba_roy_winners.xlsx', index=False)



# nba mvp and top 10 highest scoring averages
def nba_mvp_ppg(df):
    try:
        return df[(df['award'] == 'nba mvp') & 
                  (df['winner'] == 'True') & 
                  (df['year_x'] == df['year_y'])]
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
top_5_nba_mvp_ppg_df = top_5_nba_mvp_ppg_df.rename(columns={'year_x': 'year',
                                                            'player_x': 'player',
                                                            'age_x': 'age',
                                                            'tm_x':'team'})
# rename certain columns in top_10_nba_mvp_ppg_df
top_10_nba_mvp_ppg_df = top_10_nba_mvp_ppg_df.rename(columns={'year_x': 'year',
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
      top_5_nba_mvp_ppg_df['year'].astype(str) + ' Season \n' +\
      top_5_nba_mvp_ppg_df['pts_per_game'].astype(str) + ' Points Per Game' +\
      '\n'
y = top_5_nba_mvp_ppg_df['pts_per_game']
color = 'blue'
plt.bar(x, y, color=color)
plt.title('NBA MVP Winners Points Per Game Average - Top 5')
plt.xlabel('PLAYERS')
plt.ylabel('POINTS PER GAME')
plt.show()
# top 10 nba mvp ppg
x = top_10_nba_mvp_ppg_df['player'].astype(str) + '\n' +\
      top_10_nba_mvp_ppg_df['year'].astype(str) + ' Season \n' +\
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