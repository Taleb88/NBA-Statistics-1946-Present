import pandas as pd
import numpy as ny
import time

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

start_time = time.time()
print('read_csv and to_excel = success', ' - ', (time.time() - start_time))

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

print('conversion of season columns in all dataframes = success - ', (time.time() - start_time))

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

# changing name of season column to season_ending_year
def season_ending_year(df):
    try:
        return df.rename(columns={'season': 'season_ending_year'})
    except:
        print('cannot change name of column')

advanced_df = season_ending_year(advanced_df)
all_star_selections_df = season_ending_year(all_star_selections_df)
end_of_season_teams_voting_df = season_ending_year(end_of_season_teams_voting_df)
end_of_season_teams_df = season_ending_year(end_of_season_teams_df)
opponent_stats_per_100_poss_df = season_ending_year(opponent_stats_per_100_poss_df)
opponent_stats_per_game_df = season_ending_year(opponent_stats_per_game_df)
opponent_totals_df = season_ending_year(opponent_totals_df)
per_36_minutes_df = season_ending_year(per_36_minutes_df)
per_100_poss_df = season_ending_year(per_100_poss_df)
player_award_shares_df = season_ending_year(player_award_shares_df)
player_per_game_df = season_ending_year(player_per_game_df)
player_play_by_play_df = season_ending_year(player_play_by_play_df)
player_season_info_df = season_ending_year(player_season_info_df)
player_shooting_df = season_ending_year(player_shooting_df)
player_totals_df = season_ending_year(player_totals_df)
team_abbrev_df = season_ending_year(team_abbrev_df)
team_stats_per_100_poss_df = season_ending_year(team_stats_per_100_poss_df)
team_stats_per_game_df = season_ending_year(team_stats_per_game_df)
team_summaries_df = season_ending_year(team_summaries_df)
team_totals_df = season_ending_year(team_totals_df)



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
advanced_df['season'] = advanced_df['season_ending_year']
all_star_selections_df['season'] = all_star_selections_df['season_ending_year']
end_of_season_teams_voting_df['season'] = end_of_season_teams_voting_df['season_ending_year']
end_of_season_teams_df['season'] = end_of_season_teams_df['season_ending_year']
opponent_stats_per_100_poss_df['season'] = opponent_stats_per_100_poss_df['season_ending_year']
opponent_stats_per_game_df['season'] = opponent_stats_per_game_df['season_ending_year']
opponent_totals_df['season'] = opponent_totals_df['season_ending_year']
per_36_minutes_df['season'] = per_36_minutes_df['season_ending_year']
per_100_poss_df['season'] = per_100_poss_df['season_ending_year']
player_award_shares_df['season'] = player_award_shares_df['season_ending_year']
player_per_game_df['season'] = player_per_game_df['season_ending_year']
player_play_by_play_df['season'] = player_play_by_play_df['season_ending_year']
player_season_info_df['season'] = player_season_info_df['season_ending_year']
player_shooting_df['season'] = player_shooting_df['season_ending_year']
player_totals_df['season'] = player_totals_df['season_ending_year']
team_abbrev_df['season'] = team_abbrev_df['season_ending_year']
team_stats_per_100_poss_df['season'] = team_stats_per_100_poss_df['season_ending_year']
team_stats_per_game_df['season'] = team_stats_per_game_df['season_ending_year']
team_summaries_df['season'] = team_summaries_df['season_ending_year']
team_totals_df['season'] = team_totals_df['season_ending_year']


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


# first_seas column in player_career_info_df
def first_season_values(df):
    try:
        return df.replace(to_replace={'first_seas': {'1947': '1946-47', 
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
            f'cannot update values')

player_career_info_df = first_season_values(player_career_info_df)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)

# last seas column in player_career_info_df
def last_season_values(df):
    try:
        return df.replace(to_replace={'last_seas': {'1947': '1946-47', 
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
            f'cannot update values')

player_career_info_df = last_season_values(player_career_info_df)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)

print('first_season and last_season value modifications = success - ', (time.time() - start_time))

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
            f'cannot update values')

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

# changing names of first_seas and second_seas columns in player_career_info_df respectively
def season_column_names(df):
    try:
        return df.rename(columns={'first_seas': 'first_season',
                                  'last_seas': 'last_season'})
    except:
        print('cannot change name of column')

player_career_info_df = season_column_names(player_career_info_df)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)


print('changing of column names to first_season and last_season = success - ', (time.time() - start_time))


# ==================== #
# data cleanup - IN PROGRESS
# ==================== #
# player name updates

# Patrick Ewing -> Patrick ewing jr.
advanced_df.loc[advanced_df['player_id'] == 3967, 'player'] = 'Patrick Ewing Jr.'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 3967, 'player'] = 'Patrick Ewing Jr.'
#per_100_poss_df.loc[per_100_poss_df['player_id'].astype(int) == 3967, 'player'] = 'Patrick Ewing Jr.'
#player_career_info_df.loc[player_career_info_df['player_id'].astype(int) == 3967, 'player'] = 'Patrick Ewing Jr.'
player_per_game_df.loc[player_per_game_df['player_id'] == 3967, 'player'] = 'Patrick Ewing Jr.'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 3967, 'player'] = 'Patrick Ewing Jr.'
player_season_info_df.loc[player_season_info_df['player_id'] == 3967, 'player'] = 'Patrick Ewing Jr.'
player_shooting_df.loc[player_shooting_df['player_id'].astype(int) == 3967, 'player'] = 'Patrick Ewing Jr.'
player_totals_df.loc[player_totals_df['player_id'] == 3967, 'player'] = 'Patrick Ewing Jr.'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Metta World Peace -> Metta Sandiford-Artest
advanced_df.loc[advanced_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'
#player_career_info_df.loc[player_career_info_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'
player_per_game_df.loc[player_per_game_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'
player_season_info_df.loc[player_season_info_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'
player_shooting_df.loc[player_shooting_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'
player_totals_df.loc[player_totals_df['player_id'] == 3205, 'player'] = 'Metta Sandiford-Artest'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Enes Freedom -> Enes Kanter Freedom (id = 4006)
advanced_df.loc[advanced_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'
#player_career_info_df.loc[player_career_info_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'
player_per_game_df.loc[player_per_game_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'
player_season_info_df.loc[player_season_info_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'
player_shooting_df.loc[player_shooting_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'
player_totals_df.loc[player_totals_df['player_id'] == 4006, 'player'] = 'Enes Kanter Freedom'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Will Barton -> Will Barton III (id = 4140)
advanced_df.loc[advanced_df['player_id'] == 4140, 'player'] = 'Will Barton III'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 4140, 'player'] = 'Will Barton III'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 4140, 'player'] = 'Will Barton III'
#player_career_info_df.loc[player_career_info_df['player_id'] == 4140, 'player'] = 'Will Barton III'
player_per_game_df.loc[player_per_game_df['player_id'] == 4140, 'player'] = 'Will Barton III'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 4140, 'player'] = 'Will Barton III'
player_season_info_df.loc[player_season_info_df['player_id'] == 4140, 'player'] = 'Will Barton III'
player_shooting_df.loc[player_shooting_df['player_id'] == 4140, 'player'] = 'Will Barton III'
player_totals_df.loc[player_totals_df['player_id'] == 4140, 'player'] = 'Will Barton III'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Herm Klotz -> Red Klotz (id = 181)
advanced_df.loc[advanced_df['player_id'] == 181, 'player'] = 'Red Klotz'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 181, 'player'] = 'Red Klotz'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 181, 'player'] = 'Red Klotz'
#player_career_info_df.loc[player_career_info_df['player_id'] == 181, 'player'] = 'Red Klotz'
player_per_game_df.loc[player_per_game_df['player_id'] == 181, 'player'] = 'Red Klotz'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 181, 'player'] = 'Red Klotz'
player_season_info_df.loc[player_season_info_df['player_id'] == 181, 'player'] = 'Red Klotz'
#player_shooting_df.loc[player_shooting_df['player_id'] == 181, 'player'] = 'Red Klotz'
player_totals_df.loc[player_totals_df['player_id'] == 181, 'player'] = 'Red Klotz'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
#player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Alperen Sengun (player_id = 4904)
advanced_df.loc[advanced_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'
#player_career_info_df.loc[player_career_info_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'
player_per_game_df.loc[player_per_game_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'
player_season_info_df.loc[player_season_info_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'
player_shooting_df.loc[player_shooting_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'
player_totals_df.loc[player_totals_df['player_id'] == 4904, 'player'] = 'Alperen Sengun'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Sarunas Jaskievicius (player_id = 3640)
advanced_df.loc[advanced_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'
#player_career_info_df.loc[player_career_info_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'
player_per_game_df.loc[player_per_game_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'
player_season_info_df.loc[player_season_info_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'
player_shooting_df.loc[player_shooting_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'
player_totals_df.loc[player_totals_df['player_id'] == 3640, 'player'] = 'Sarunas Jaskievicius'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Sarunas Marciulionis (player_id = 2540)
advanced_df.loc[advanced_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'
#player_career_info_df.loc[player_career_info_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'
player_per_game_df.loc[player_per_game_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'
player_season_info_df.loc[player_season_info_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'
player_shooting_df.loc[player_shooting_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'
player_totals_df.loc[player_totals_df['player_id'] == 2540, 'player'] = 'Sarunas Marciulionis'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Alex Abrines (player_id = 4375)
advanced_df.loc[advanced_df['player_id'] == 4375, 'player'] = 'Alex Abrines'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 4375, 'player'] = 'Alex Abrines'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 4375, 'player'] = 'Alex Abrines'
#player_career_info_df.loc[player_career_info_df['player_id'] == 4375, 'player'] = 'Alex Abrines'
player_per_game_df.loc[player_per_game_df['player_id'] == 4375, 'player'] = 'Alex Abrines'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 4375, 'player'] = 'Alex Abrines'
player_season_info_df.loc[player_season_info_df['player_id'] == 4375, 'player'] = 'Alex Abrines'
player_shooting_df.loc[player_shooting_df['player_id'] == 4375, 'player'] = 'Alex Abrines'
player_totals_df.loc[player_totals_df['player_id'] == 4375, 'player'] = 'Alex Abrines'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Angel Delgado (player_id = 4587)
advanced_df.loc[advanced_df['player_id'] == 4587, 'player'] = 'Angel Delgado'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 4587, 'player'] = 'Angel Delgado'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 4587, 'player'] = 'Angel Delgado'
#player_career_info_df.loc[player_career_info_df['player_id'] == 4587, 'player'] = 'Angel Delgado'
player_per_game_df.loc[player_per_game_df['player_id'] == 4587, 'player'] = 'Angel Delgado'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 4587, 'player'] = 'Angel Delgado'
player_season_info_df.loc[player_season_info_df['player_id'] == 4587, 'player'] = 'Angel Delgado'
player_shooting_df.loc[player_shooting_df['player_id'] == 4587, 'player'] = 'Angel Delgado'
player_totals_df.loc[player_totals_df['player_id'] == 4587, 'player'] = 'Angel Delgado'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Zan Tabak (player_id = 2891)
advanced_df.loc[advanced_df['player_id'] == 2891, 'player'] = 'Zan Tabak'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 2891, 'player'] = 'Zan Tabak'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 2891, 'player'] = 'Zan Tabak'
#player_career_info_df.loc[player_career_info_df['player_id'] == 2891, 'player'] = 'Zan Tabak'
player_per_game_df.loc[player_per_game_df['player_id'] == 2891, 'player'] = 'Zan Tabak'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 2891, 'player'] = 'Zan Tabak'
player_season_info_df.loc[player_season_info_df['player_id'] == 2891, 'player'] = 'Zan Tabak'
player_shooting_df.loc[player_shooting_df['player_id'] == 2891, 'player'] = 'Zan Tabak'
player_totals_df.loc[player_totals_df['player_id'] == 2891, 'player'] = 'Zan Tabak'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Zarko Cabarkapa (player_id = 3493)
advanced_df.loc[advanced_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'
#player_career_info_df.loc[player_career_info_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'
player_per_game_df.loc[player_per_game_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'
player_season_info_df.loc[player_season_info_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'
player_shooting_df.loc[player_shooting_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'
player_totals_df.loc[player_totals_df['player_id'] == 3493, 'player'] = 'Zarko Cabarkapa'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Zarko Paspalj (player_id = 2559)
advanced_df.loc[advanced_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'
#player_career_info_df.loc[player_career_info_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'
player_per_game_df.loc[player_per_game_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'
player_season_info_df.loc[player_season_info_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'
player_shooting_df.loc[player_shooting_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'
player_totals_df.loc[player_totals_df['player_id'] == 2559, 'player'] = 'Zarko Paspalj'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Zeljko Rebraca (player_id = 3364)
advanced_df.loc[advanced_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'
#player_career_info_df.loc[player_career_info_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'
player_per_game_df.loc[player_per_game_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'
player_season_info_df.loc[player_season_info_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'
player_shooting_df.loc[player_shooting_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'
player_totals_df.loc[player_totals_df['player_id'] == 3364, 'player'] = 'Zeljko Rebraca'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Omer Asik (player_id = 3965)
advanced_df.loc[advanced_df['player_id'] == 3965, 'player'] = 'Omer Asik'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 3965, 'player'] = 'Omer Asik'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 3965, 'player'] = 'Omer Asik'
#player_career_info_df.loc[player_career_info_df['player_id'] == 3965, 'player'] = 'Omer Asik'
player_per_game_df.loc[player_per_game_df['player_id'] == 3965, 'player'] = 'Omer Asik'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 3965, 'player'] = 'Omer Asik'
player_season_info_df.loc[player_season_info_df['player_id'] == 3965, 'player'] = 'Omer Asik'
player_shooting_df.loc[player_shooting_df['player_id'] == 3965, 'player'] = 'Omer Asik'
player_totals_df.loc[player_totals_df['player_id'] == 3965, 'player'] = 'Omer Asik'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Dario Saric (player_id = 4390)
advanced_df.loc[advanced_df['player_id'] == 4390, 'player'] = 'Dario Saric'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 4390, 'player'] = 'Dario Saric'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 4390, 'player'] = 'Dario Saric'
#player_career_info_df.loc[player_career_info_df['player_id'] == 4390, 'player'] = 'Dario Saric'
player_per_game_df.loc[player_per_game_df['player_id'] == 4390, 'player'] = 'Dario Saric'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 4390, 'player'] = 'Dario Saric'
player_season_info_df.loc[player_season_info_df['player_id'] == 4390, 'player'] = 'Dario Saric'
player_shooting_df.loc[player_shooting_df['player_id'] == 4390, 'player'] = 'Dario Saric'
player_totals_df.loc[player_totals_df['player_id'] == 4390, 'player'] = 'Dario Saric'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Dario Saric (letter accents)
advanced_df.loc[advanced_df['player'] == 'Dario Šarić', 'player'] = 'Dario Saric'
per_36_minutes_df.loc[per_36_minutes_df['player'] == 'Dario Šarić', 'player'] = 'Dario Saric'
#per_100_poss_df.loc[per_100_poss_df['player'] == 'Dario Šarić', 'player'] = 'Dario Saric'
#player_career_info_df.loc[player_career_info_df['player'] == 'Dario Šarić', 'player'] = 'Dario Saric'
player_per_game_df.loc[player_per_game_df['player'] == 'Dario Šarić', 'player']= 'Dario Saric'
#player_play_by_play_df.loc[player_play_by_play_df['player'] == 'Dario Šarić', 'player'] = 'Dario Saric'
player_season_info_df.loc[player_season_info_df['player'] == 'Dario Šarić', 'player'] = 'Dario Saric'
player_shooting_df.loc[player_shooting_df['player'] == 'Dario Šarić', 'player'] = 'Dario Saric'
player_totals_df.loc[player_totals_df['player'] == 'Dario Šarić', 'player'] = 'Dario Saric'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Donte Greene (player_id = 3813)
advanced_df.loc[advanced_df['player_id'] == 3813, 'player'] = 'Donte Greene'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 3813, 'player'] = 'Donte Greene'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 3813, 'player'] = 'Donte Greene'
#player_career_info_df.loc[player_career_info_df['player_id'] == 3813, 'player'] = 'Donte Greene'
player_per_game_df.loc[player_per_game_df['player_id'] == 3813, 'player'] = 'Donte Greene'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 3813, 'player'] = 'Donte Greene'
player_season_info_df.loc[player_season_info_df['player_id'] == 3813, 'player'] = 'Donte Greene'
player_shooting_df.loc[player_shooting_df['player_id'] == 3813, 'player'] = 'Donte Greene'
player_totals_df.loc[player_totals_df['player_id'] == 3813, 'player'] = 'Donte Greene'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Fernando Martin (player_id = 2303)
advanced_df.loc[advanced_df['player_id'] == 2303, 'player'] = 'Fernando Martin'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 2303, 'player'] = 'Fernando Martin'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 2303, 'player'] = 'Fernando Martin'
#player_career_info_df.loc[player_career_info_df['player_id'] == 2303, 'player'] = 'Fernando Martin'
player_per_game_df.loc[player_per_game_df['player_id'] == 2303, 'player'] = 'Fernando Martin'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 2303, 'player'] = 'Fernando Martin'
player_season_info_df.loc[player_season_info_df['player_id'] == 2303, 'player'] = 'Fernando Martin'
player_shooting_df.loc[player_shooting_df['player_id'] == 2303, 'player'] = 'Fernando Martin'
player_totals_df.loc[player_totals_df['player_id'] == 2303, 'player'] = 'Fernando Martin'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Lester Quinones (player_id = 5078)
advanced_df.loc[advanced_df['player_id'] == 5078, 'player'] = 'Lester Quinones'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 5078, 'player'] = 'Lester Quinones'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 5078, 'player'] = 'Lester Quinones'
#player_career_info_df.loc[player_career_info_df['player_id'] == 5078, 'player'] = 'Lester Quinones'
player_per_game_df.loc[player_per_game_df['player_id'] == 5078, 'player'] = 'Lester Quinones'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 5078, 'player'] = 'Lester Quinones'
player_season_info_df.loc[player_season_info_df['player_id'] == 5078, 'player'] = 'Lester Quinones'
player_shooting_df.loc[player_shooting_df['player_id'] == 5078, 'player'] = 'Lester Quinones'
player_totals_df.loc[player_totals_df['player_id'] == 5078, 'player'] = 'Lester Quinones'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Tomas Satoransky (player_id = 4454)
advanced_df.loc[advanced_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
#player_career_info_df.loc[player_career_info_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
player_per_game_df.loc[player_per_game_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
player_season_info_df.loc[player_season_info_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
player_shooting_df.loc[player_shooting_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
player_totals_df.loc[player_totals_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Tomas Satoransky (player_id = 4454)
advanced_df.loc[advanced_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
#player_career_info_df.loc[player_career_info_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
player_per_game_df.loc[player_per_game_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
player_season_info_df.loc[player_season_info_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
player_shooting_df.loc[player_shooting_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'
player_totals_df.loc[player_totals_df['player_id'] == 4454, 'player'] = 'Tomas Satoransky'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
#player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# Toni Kukoc (player_id = 2829)
advanced_df.loc[advanced_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'
per_36_minutes_df.loc[per_36_minutes_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'
#per_100_poss_df.loc[per_100_poss_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'
#player_career_info_df.loc[player_career_info_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'
player_per_game_df.loc[player_per_game_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'
#player_play_by_play_df.loc[player_play_by_play_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'
player_season_info_df.loc[player_season_info_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'
player_shooting_df.loc[player_shooting_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'
player_totals_df.loc[player_totals_df['player_id'] == 2829, 'player'] = 'Toni Kukoc'

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
#player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)


print('player value modifications = success - ', (time.time() - start_time))


# CREATING DOUBLE-DOUBLE AND TRIPLE-DOUBLE COLUMNS (VALUES = YES/NO) in player_per_game_df
player_per_game_df['double_double_avg'] = [''] * len(player_per_game_df)

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
# checking to see what positions trb_per_game, ast_per_game, stl_per_game, blk_per_game, and pts_per_game are located at
# result -> [28 29 30 31 34]  (ADD 1 TO EACH ELEMENT INDEX) -> [29 30 31 32 35]
#print(player_per_game_df.columns.get_indexer(['trb_per_game', 'ast_per_game', 'stl_per_game', 'blk_per_game', 'pts_per_game']))
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


print('creation of double-double and triple-double columns = success - ', (time.time() - start_time))


# populating certain cells/values the stl_per_game and blk_per_game columns with the following ->
#   N/A - Stat tracked as of the 1973-74 NBA Season
#   N/A - Stat tracked as of the 1973-74 ABA Season
player_per_game_df.loc[(player_per_game_df['season_ending_year'].astype(int) < 1974) & \
    ((player_per_game_df['lg'] == 'NBA') | (player_per_game_df['lg'] == 'BAA')), 'stl_per_game'] = \
    'N/A - Stat tracked as of the 1973-74 NBA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df.loc[(player_per_game_df['season_ending_year'].astype(int) < 1974) & \
    ((player_per_game_df['lg'] == 'NBA') | (player_per_game_df['lg'] == 'BAA')), 'blk_per_game'] = \
    'N/A - Stat tracked as of the 1973-74 NBA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df.loc[(player_per_game_df['season_ending_year'].astype(int) < 1974) & (player_per_game_df['lg'] == 'ABA'), 
                       'blk_per_game'] = 'N/A - Stat tracked as of the 1973-74 ABA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

player_per_game_df.loc[(player_per_game_df['season_ending_year'].astype(int) < 1974) & (player_per_game_df['lg'] == 'ABA'), 
                       'stl_per_game'] = 'N/A - Stat tracked as of the 1973-74 ABA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)

print('updating stl_per_game and blk_per_game columns accordingly = success - ', (time.time() - start_time))


# populating certain cells/values the trb_per_game column with the following ->
#   N/A - Stat tracked as of the 1950-51 NBA Season (NBA AND BAA merged on August 3,1949)
player_per_game_df.loc[(player_per_game_df['season_ending_year'].astype(int) < 1951) & \
    ((player_per_game_df['lg'] == 'NBA') | (player_per_game_df['lg'] == 'BAA')), 'trb_per_game'] = \
    'N/A - Stat tracked as of the 1950-51 NBA Season'

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)


print('updating trb_per_game columns accordingly = success - ', (time.time() - start_time))


# =================================== #
#                       COMPLETE
# 1. create a column called calendar year -> datatype = int
#       ['calendar_year'] = ['season_ending_year'].astype(int) - COMPLETE
# 2. fillna(0) method used to fill empty cells with '0' values in birth_year and age columns - COMPLETE
# 3. convert [birth_year] values to int datatype (player_per_game_df, player_season_info_df, player_totals_df) - COMPLETE
# 4. ['birth_year'] = calendar year - age and then subtract 1 from ['birth_year'] column for accuracy purposes - COMPLETE
# 5. modify ['birth_year'] values that are initially '0' (player_per_game_df, player_season_info_df, player_totals_df) - COMPLETE
# 6. ['age'] = ['calendar_year'] - ['birth_year'] (player_per_game_df, player_season_info_df, player_totals_df) - COMPLETE
# =================================== #

# 1
player_per_game_df['calendar_year'] = player_per_game_df['season_ending_year'].astype(int)
player_play_by_play_df['calendar_year'] = player_play_by_play_df['season_ending_year'].astype(int)
player_season_info_df['calendar_year'] = player_season_info_df['season_ending_year'].astype(int)
player_shooting_df['calendar_year'] = player_shooting_df['season_ending_year'].astype(int)
player_totals_df['calendar_year'] = player_totals_df['season_ending_year'].astype(int)

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# 2
player_per_game_df['birth_year'] = player_per_game_df['birth_year'].fillna(0)
player_play_by_play_df['birth_year'] = player_play_by_play_df['birth_year'].fillna(0)
player_season_info_df['birth_year'] = player_season_info_df['birth_year'].fillna(0)
player_shooting_df['birth_year'] = player_shooting_df['birth_year'].fillna(0)
player_totals_df['birth_year'] = player_totals_df['birth_year'].fillna(0)

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

player_per_game_df['age'] = player_per_game_df['age'].fillna(0)
player_play_by_play_df['age'] = player_play_by_play_df['age'].fillna(0)
player_season_info_df['age'] = player_season_info_df['age'].fillna(0)
player_shooting_df['age'] = player_shooting_df['age'].fillna(0)
player_totals_df['age'] = player_totals_df['age'].fillna(0)
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# 3
player_per_game_df['birth_year'] = player_per_game_df['birth_year'].astype(int)
player_play_by_play_df['birth_year'] = player_play_by_play_df['birth_year'].astype(int)  
player_season_info_df['birth_year'] = player_season_info_df['birth_year'].astype(int) 
player_shooting_df['birth_year'] = player_shooting_df['birth_year'].astype(int) 
player_totals_df['birth_year'] = player_totals_df['birth_year'].astype(int) 
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# 4
player_per_game_df['birth_year'] = player_per_game_df.apply(lambda row: row['calendar_year'] - row['age'], axis=1)
player_play_by_play_df['birth_year'] = player_play_by_play_df.apply(lambda row: row['calendar_year'] - row['age'], axis=1)
player_season_info_df['birth_year'] = player_season_info_df.apply(lambda row: row['calendar_year'] - row['age'], axis=1)
player_shooting_df['birth_year'] = player_shooting_df.apply(lambda row: row['calendar_year'] - row['age'], axis=1)
player_totals_df['birth_year'] = player_totals_df.apply(lambda row: row['calendar_year'] - row['age'], axis=1)
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# subtracting 1 from birth_year value for accuracy 
player_per_game_df['birth_year'] = player_per_game_df['birth_year'] - 1
player_play_by_play_df['birth_year'] = player_play_by_play_df['birth_year'] - 1 
player_season_info_df['birth_year'] = player_season_info_df['birth_year'] - 1
player_shooting_df['birth_year'] = player_shooting_df['birth_year'] - 1
player_totals_df['birth_year'] = player_totals_df['birth_year'] - 1 
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# 5
# Pete Smith
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1470,'birth_year'] = 1947
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1470,'birth_year'] = 1947
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1470,'birth_year'] = 1947
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Clarence Brookins
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1253,'birth_year'] = 1946
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1253,'birth_year'] = 1946
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1253,'birth_year'] = 1946
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Jim Wilson
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1291,'birth_year'] = 1948
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1291,'birth_year'] = 1948
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1291,'birth_year'] = 1948
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Walter Byrd
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1231,'birth_year'] = 1942
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1231,'birth_year'] = 1942
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1231,'birth_year'] = 1942
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Wilbur Kirkland
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1233,'birth_year'] = 1947
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1233,'birth_year'] = 1947
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1233,'birth_year'] = 1947
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Charles Parks
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1081,'birth_year'] = 1946
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1081,'birth_year'] = 1946
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1081,'birth_year'] = 1946
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Bill Allen
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 904,'birth_year'] = 1945
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 904,'birth_year'] = 1945
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 904,'birth_year'] = 1945
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Bobby Wilson
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 922,'birth_year'] = 1944
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 922,'birth_year'] = 1944
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 922,'birth_year'] = 1944
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Darrell Hardy
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 939,'birth_year'] = 1944
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 939,'birth_year'] = 1944
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 939,'birth_year'] = 1944
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Dexter Westbrook
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 945,'birth_year'] = 1943
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 945,'birth_year'] = 1943
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 945,'birth_year'] = 1943
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Dick Lee (birthdate nor year found online, birth_year value is an educational estimate based on college stats)
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 946,'birth_year'] = 1943
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 946,'birth_year'] = 1943
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 946,'birth_year'] = 1943
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Errol Palmer
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 952,'birth_year'] = 1945
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 952,'birth_year'] = 1945
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 952,'birth_year'] = 1945
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Gary Turner
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 956,'birth_year'] = 1942
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 956,'birth_year'] = 1942
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 956,'birth_year'] = 1942
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# R.B. Lynam
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1023,'birth_year'] = 1944
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1023,'birth_year'] = 1944
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1023,'birth_year'] = 1944
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Randy Stoll
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1025,'birth_year'] = 1945
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1025,'birth_year'] = 1945
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1025,'birth_year'] = 1945
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Richie Moore
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1031,'birth_year'] = 1945
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1031,'birth_year'] = 1945
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1031,'birth_year'] = 1945
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Willis Thomas
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 1067,'birth_year'] = 1937
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 1067,'birth_year'] = 1937
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 1067,'birth_year'] = 1937
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Howie McCarty
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 89,'birth_year'] = 1919
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 89,'birth_year'] = 1919
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 89,'birth_year'] = 1919
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Buddy O’Grady
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 30,'birth_year'] = 1920
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 30,'birth_year'] = 1920
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 30,'birth_year'] = 1920
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Cecil Hankins
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 32,'birth_year'] = 1922
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 32,'birth_year'] = 1922
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 32,'birth_year'] = 1922
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Deb Smith
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 41,'birth_year'] = 1920
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 41,'birth_year'] = 1920
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 41,'birth_year'] = 1920
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Donnie Forman
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 233,'birth_year'] = 1926
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 233,'birth_year'] = 1926
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 233,'birth_year'] = 1926
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Ernie Calverley
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 56,'birth_year'] = 1924
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 56,'birth_year'] = 1924
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 56,'birth_year'] = 1924
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Fritz Nagy
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 241,'birth_year'] = 1924
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 241,'birth_year'] = 1924
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 241,'birth_year'] = 1924
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# George Munroe
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 67,'birth_year'] = 1922
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 67,'birth_year'] = 1922
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 67,'birth_year'] = 1922
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Hank Biasatti
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 78,'birth_year'] = 1922
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 78,'birth_year'] = 1922
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 78,'birth_year'] = 1922
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Harold Johnson
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 82,'birth_year'] = 1920
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 82,'birth_year'] = 1920
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 82,'birth_year'] = 1920
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Red Klotz
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 181,'birth_year'] = 1920
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 181,'birth_year'] = 1920
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 181,'birth_year'] = 1920
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Howie McCarty
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 89,'birth_year'] = 1919
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 89,'birth_year'] = 1919
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 89,'birth_year'] = 1919
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Howie McCarty
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 89,'birth_year'] = 1919
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 89,'birth_year'] = 1919
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 89,'birth_year'] = 1919
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Jack Eskridge
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 254,'birth_year'] = 1924
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 254,'birth_year'] = 1924
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 254,'birth_year'] = 1924
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Jake Pelkington
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 259,'birth_year'] = 1916
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 259,'birth_year'] = 1916
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 259,'birth_year'] = 1916
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Joe Colone
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 264,'birth_year'] = 1924
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 264,'birth_year'] = 1924
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 264,'birth_year'] = 1924
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Mike Bloom
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 190,'birth_year'] = 1915
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 190,'birth_year'] = 1915
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 190,'birth_year'] = 1915
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Nat Hickey
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 191,'birth_year'] = 1902
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 191,'birth_year'] = 1902
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 191,'birth_year'] = 1902
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# Red Dehnert
player_per_game_df.loc[player_per_game_df['player_id'].astype(int) == 142,'birth_year'] = 1924
player_season_info_df.loc[player_season_info_df['player_id'].astype(int) == 142,'birth_year'] = 1924
player_totals_df.loc[player_totals_df['player_id'].astype(int) == 142,'birth_year'] = 1924
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# 6
player_per_game_df['age'] = player_per_game_df.apply(lambda row: row['calendar_year'] - row['birth_year'], axis=1)
player_season_info_df['age'] = player_season_info_df.apply(lambda row: row['calendar_year'] - row['birth_year'], axis=1)
player_totals_df['age'] = player_totals_df.apply(lambda row: row['calendar_year'] - row['birth_year'], axis=1)
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# append birth_year values to player values in player_per_game_df, player_season_info, player_totals_df 
player_per_game_df['player'] = player_per_game_df['player'].astype(str) + " (b. " + player_per_game_df['birth_year'].astype(str) + ")"
player_season_info_df['player'] = player_season_info_df['player'].astype(str) + " (b. " + player_season_info_df['birth_year'].astype(str) + ")"
player_totals_df['player'] = player_totals_df['player'].astype(str) + " (b. " + player_season_info_df['birth_year'].astype(str) + ")"
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

player_per_game_df['player'] = player_per_game_df['player'].replace('.0','')
player_season_info_df['player'] = player_season_info_df['player'].replace('.0','')
player_totals_df['player'] = player_totals_df['player'].replace('.0','')
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# save changes to appropriate sheets
advanced_df.to_excel('advanced.xlsx', index=False)
per_36_minutes_df.to_excel('Per 36 Minutes.xlsx', index=False)
#per_100_poss_df.to_excel('Per 100 Poss.xlsx', index=False)
#player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
#player_play_by_play_df.to_excel('Player Play By Play.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
#player_shooting_df.to_excel('Player Shooting.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# sort player values in by ASC order in player_per_game_df, player_season_info, player_totals_df
player_per_game_df = player_per_game_df.sort_values(['player'], ascending=True)
player_season_info_df = player_season_info_df.sort_values(['player'], ascending=True)
player_totals_df = player_totals_df.sort_values(['player'], ascending=True)

# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)

# reset player_id to 0 for now
#   player_per_game_df, player_season_info, player_totals_df
player_per_game_df['player_id'] = 0
player_season_info_df['player_id'] = 0
player_totals_df['player_id'] = 0
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# increment player_id based on player value ONLY 
player_per_game_df['player_id'] = player_per_game_df['player'].factorize()[0] + 1
player_season_info_df['player_id'] = player_season_info_df['player'].factorize()[0] + 1
player_totals_df['player_id'] = player_totals_df['player'].factorize()[0] + 1
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)
# remove birth_year from player values
player_per_game_df['player'] = player_per_game_df['player'].astype(str).str[:-12]
player_season_info_df['player'] = player_season_info_df['player'].astype(str).str[:-12]
player_totals_df['player'] = player_totals_df['player'].astype(str).str[:-12]
# saving updates
player_per_game_df.to_excel('Player Per Game.xlsx', index=False)
player_season_info_df.to_excel('Player Season Info.xlsx', index=False)
player_totals_df.to_excel('Player Totals.xlsx', index=False)


print('massive data cleanup in player_per_game_df, player_season_info_df, and player_totals_df = success - ', (time.time() - start_time))


#                                       IN PROGRESS
# recreate player_career_info_df (player_directory_1_df) and make sure to include following columns
#   player_id, player, birth_year, hof, num_seasons, first_season, last_season
#   this pertains to the player_per_game, player_season_info, and player_totals dataframes ONLY

# removing initial Player Career Info.xlsx prior to recreating it
import os

file_path = 'Player Career Info.xlsx'

if os.path.isfile(file_path):
    os.remove(file_path)
    print('removal of initial Player Career Info.xlsx file = success')
else:
    print('Player Career Info.xlsx does not exist')

start_time = time.time()

print('removal of Player Career Info.xlsx accordingly = success - ', (time.time() - start_time))

# creating new version of player_career_info_df dataframe
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
# first_season_values updated in string format to display full values per column


print('recreation of player_career_info_df = success - ', (time.time() - start_time))

# ===================================== #
# hof
# hof values to be updated accordingly
# ===================================== #

# web scraping via basketball-reference.com
url = \
    pd.read_html('https://www.basketball-reference.com/awards/hof.html')

data = url

hofers_list_df = url[0]
# save changes
hofers_list_df.to_excel('hofers.xlsx')

hofers_list_df = pd.read_excel('hofers.xlsx', header=1) # removes first row of dataset
# save changes
hofers_list_df.to_excel('hofers.xlsx', index=False)

# rename column Name to Player
hofers_list_df = hofers_list_df.rename(columns={'Name': 'player'}) 
# save changes
hofers_list_df.to_excel('hofers.xlsx', index=False)

# remove first row
hofers_list_df = hofers_list_df.iloc[1:]
# save changes
hofers_list_df.to_excel('hofers.xlsx', index=False)

# filter out all rows that do not contain 'Player'
hofers_list_df = hofers_list_df.loc[hofers_list_df['Category'] == 'Player']

hofers_list_df.to_excel('hofers.xlsx', index=False)

# array of words to be removed
words_to_be_removed = ["WNBA", "Int'l", "/", "CBB Player", "Coach", "Exec", "Oly", "CBB Coach"]
hofers_list_df['player'] = [' '.join([item for item in x.split(' ')[:2]
                          if item not in words_to_be_removed])
                          for x in hofers_list_df['player']]
# save changes
hofers_list_df.to_excel('hofers.xlsx', index=False)

# merge both player_career_info_df and hofers
player_career_info_df = pd.merge(player_career_info_df,
                hofers_list_df,
                how='outer',
                left_index=True,
                right_index=True)
# save changes
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
# python pandas simple xlookup/vlookup version checking if player is in hof - evaluates to TRUE or FALSE
player_career_info_df['hof'] = player_career_info_df['player_x'].isin(player_career_info_df['player_y'])
# save changes
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
# change True values to "Yes"
player_career_info_df['hof'] = player_career_info_df['hof'].replace(True, 'Yes')
# save changes
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
# change False values to "No"
player_career_info_df['hof'] = player_career_info_df['hof'].replace(False, 'No')
# save changes
player_career_info_df.to_excel('Player Career Info.xlsx', index=False)


print('updating hof values accordingly in player_career_info_df = success - ', (time.time() - start_time))


# removing extra columns in player_career_info_df
player_career_info_df = \
    player_career_info_df.drop(player_career_info_df.iloc[:,7:27], axis=1)

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)
# renaming column from player_x back to player
player_career_info_df = player_career_info_df.rename(columns={'player_x': 'player'})

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)

# update hof values further
player_career_info_df.loc[(player_career_info_df['player'] == 'Bill Bradley') & 
                          (player_career_info_df['birth_year'].astype(int) == 1941), 'hof'] = 'No'

player_career_info_df.loc[(player_career_info_df['player'] == 'Bobby Jones') & 
                          (player_career_info_df['birth_year'].astype(int) == 1983), 'hof'] = 'No'

player_career_info_df.loc[(player_career_info_df['player'] == 'Roger Brown') & 
                          (player_career_info_df['birth_year'].astype(int) == 1950), 'hof'] = 'No'

player_career_info_df.to_excel('Player Career Info.xlsx', index=False)


print('update hof values further accordingly in player_career_info_df = success - ', (time.time() - start_time))


# ============= #
# merging certain dataframes 
# ============= #

# merging player award shares and player per game dataframes
player_award_shares_and_player_per_game_merged_df = pd.merge(player_award_shares_df,
                                                          player_per_game_df, 
                                                          on=['seas_id'])
#print(player_award_shares_and_player_per_game_merged_df)
player_award_shares_and_player_per_game_merged_df.\
    to_excel('player_award_shares_and_player_per_game_merged.xlsx', index=False)

# merging player shooting and player totals dataframes
player_shooting_and_player_totals_merged_df = pd.merge(player_shooting_df, 
                                                       player_totals_df,
                                                       on=['seas_id'])
#print(player_shooting_and_player_totals_merged_df)
player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)

# converting values to string format
player_award_shares_and_player_per_game_merged_df['winner'] = \
    player_award_shares_and_player_per_game_merged_df['winner'].astype(str)

# changing 'nan' values to 'True' in Bobby Jones' case - 1983 sixth man of the year
player_award_shares_and_player_per_game_merged_df['winner'] = \
    player_award_shares_and_player_per_game_merged_df['winner'].replace('nan', 'True')

# hofers and player_per_game dataframes merged
player_career_info_and_player_per_game_merged_df = pd.merge(player_career_info_df,
                          player_per_game_df,
                          on=['player_id'])

player_career_info_and_player_per_game_merged_df.to_excel('player_career_and_player_per_game_merged.xlsx', index=False)


print('merging of multiple dataframes = success - ', (time.time() - start_time))


# filter out non-hofers here
hofers_list_and_player_per_game_df = player_career_info_and_player_per_game_merged_df.loc[player_career_info_and_player_per_game_merged_df['hof'] == 'Yes']

hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game.xlsx', index=False)


print('filter out non-hofers here = success - ', (time.time() - start_time))


# 1-16-2025 - COMPLETE
#   hofers_list_and_player_per_game_df (DATAFRAME) = SUCCESS
#   player_id -> ASC seas_id -> DSC = SUCCESS
#   remove rows with df['tm'] == 'TOT' = SUCCESS
#   formula = SUCCESS
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
# groupby implemented to display games, points per game, and assists per game averages for the hall-of-famers
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
        'pts_per_game': "sum",
        'ast_per_game': "sum"
        }
    ).reset_index()
# save changes
hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game_averages.xlsx', index=False)
# calcuations
hofers_list_and_player_per_game_df['g'] = hofers_list_and_player_per_game_df.apply(lambda row: row['g']
                                                                                    / row['num_seasons'], axis=1)
hofers_list_and_player_per_game_df['pts_per_game'] = hofers_list_and_player_per_game_df.apply(lambda row: row['pts_per_game'] / row['num_seasons'], axis=1)
hofers_list_and_player_per_game_df['ast_per_game'] = hofers_list_and_player_per_game_df.apply(lambda row: row['ast_per_game'] / row['num_seasons'], axis=1)

# save changes   
hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game_averages.xlsx', index=False)
# round values 2 decimal spaces
hofers_list_and_player_per_game_df['g'] = hofers_list_and_player_per_game_df['g'].apply(lambda row: round(row, 2))
hofers_list_and_player_per_game_df['pts_per_game'] = hofers_list_and_player_per_game_df['pts_per_game'].apply(lambda row: round(row, 2))
hofers_list_and_player_per_game_df['ast_per_game'] = hofers_list_and_player_per_game_df['ast_per_game'].apply(lambda row: round(row, 2))
# save changes
hofers_list_and_player_per_game_df.to_excel('hofers_list_and_player_per_game_averages.xlsx', index=False)


print('updates made to hofers_list_and_player_per_game_df = success - ', (time.time() - start_time))


# TEST ONLY 1-16-2025 - IN PROGRESS
#   filter out rows with ['tm'] == 'TOT'
#   hofer_list_and_player_per_game_df = pd.read_excel('hofer_list_and_player_per_game_df')
#       version 2 - rebounds (values should = 0)
#                   subtract num_seasons from the following player_ids
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
#                   
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
# calculations 
hofer_list_and_player_per_game_df_version_2['trb_per_game'] = hofer_list_and_player_per_game_df_version_2.apply(lambda row: row['trb_per_game'] / row['num_seasons'], axis=1)
# save changes
hofer_list_and_player_per_game_df_version_2.to_excel('hofer_list_and_player_per_game_version_2.xlsx', index=False)
# round values 2 decimal spaces
hofer_list_and_player_per_game_df_version_2['trb_per_game'] = hofer_list_and_player_per_game_df_version_2['trb_per_game'].apply(lambda row: round(row, 2))
# save changes
hofer_list_and_player_per_game_df_version_2.to_excel('hofer_list_and_player_per_game_version_2.xlsx', index=False)
# copy trb_per_game column from version_2 to main hofer_list_and_player_per_game_df (averages list is the main dataframe/sheet for all hofers)
trb_per_game = hofer_list_and_player_per_game_df_version_2.iloc[:,7]
hofers_list_and_player_per_game_df['trb_per_game'] = trb_per_game.copy()
# save changes to main hofer_list_and_player_per_game_df
hofers_list_and_player_per_game_df.to_excel('hofer_list_and_player_per_game_averages.xlsx', index=False)


print('adding trb_per_game column to hofers_list_and_player_per_game_df = success - ', (time.time() - start_time))


# ================== #
# adding fgs and fts made combined/fgs and fts attempted combined/tsp - true shooting percentage 
#   columns
# ================== #

# attempts made in all 3 categories
player_shooting_and_player_totals_merged_df['x2p + x3p + ft'] = \
    player_shooting_and_player_totals_merged_df.apply(lambda row: row['x2p'] + row['x3p'] + row['ft'],axis=1)

player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# converting all values to floats
player_shooting_and_player_totals_merged_df['x2p + x3p + ft'] = \
    player_shooting_and_player_totals_merged_df['x2p + x3p + ft'].astype(float)

player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# total attempts in all 3 categories
player_shooting_and_player_totals_merged_df['x2pa + x3pa + fta'] = \
    player_shooting_and_player_totals_merged_df.apply(lambda row: row['x2pa'] + row['x3pa'] + row['fta'], axis=1)

player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# converting all values to floats
player_shooting_and_player_totals_merged_df['x2pa + x3pa + fta'] = \
    player_shooting_and_player_totals_merged_df['x2pa + x3pa + fta'].astype(float)

player_shooting_and_player_totals_merged_df.\
    to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# fill missing values under x3p_percent column with 0
player_award_shares_and_player_per_game_merged_df['x3p_percent'] = \
    player_award_shares_and_player_per_game_merged_df['x3p_percent'].fillna(0)

player_shooting_and_player_totals_merged_df.to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# created true_shooting_percentage column containing a quotient of makes/attempts
player_shooting_and_player_totals_merged_df['true_shooting_percentage'] = \
    player_shooting_and_player_totals_merged_df['x2p + x3p + ft'].astype(float)/\
        player_shooting_and_player_totals_merged_df['x2pa + x3pa + fta'].astype(float)

player_shooting_and_player_totals_merged_df.to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)
# only 3 digits past the decimal should remain in the values under true_shooting_percentage column
player_shooting_and_player_totals_merged_df['true_shooting_percentage'] = \
    player_shooting_and_player_totals_merged_df['true_shooting_percentage'].apply(lambda row: round(row, 3))

player_shooting_and_player_totals_merged_df.to_excel('player_shooting_and_player_totals_merged.xlsx', index=False)


print('creation of true shooting percentage columns = success - ', (time.time() - start_time))


# ================== #
# filtering #
# ================== #

# finding unique values under 'award' column
# result -> ['clutch_poy' 'dpoy' 'mip' 'nba mvp' 'nba roy' 'smoy' 'aba mvp' 'aba roy']
#print(player_award_shares_and_player_per_game_merged_df['award'].unique())
# award winners
# clutch poy
def clutch_poy_winners(df):
    try:
        return df[(df['award'] == 'clutch_poy') & 
                  (df['winner'] == 'True') & 
                  (df['season_ending_year_x'] == df['season_ending_year_y']) ]
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
                  (df['season_ending_year_x'] == df['season_ending_year_y'])]
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
                  (df['season_ending_year_x'] == df['season_ending_year_y'])]
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
                  (df['season_ending_year_x'] == df['season_ending_year_y'])]
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
                  (df['season_ending_year_x'] == df['season_ending_year_y'])]
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
                  (df['season_ending_year_x'] == df['season_ending_year_y'])]
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
                  (df['season_ending_year_x'] == df['season_ending_year_y'])]
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
                  (df['season_ending_year_x'] == df['season_ending_year_y'])]
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')


aba_roy_winners_df = aba_roy_winners(player_award_shares_and_player_per_game_merged_df)

aba_roy_winners_df.to_excel('aba_roy_winners.xlsx', index=False)


# =========== #
# pivot tables 
# =========== #

# clutch poy
clutch_poy_pivot_table_df = \
    pd.pivot_table(clutch_poy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

clutch_poy_pivot_table_df.to_excel('clutch_poy_pivot_table.xlsx')

clutch_poy_pivot_table_df = \
    pd.read_excel('clutch_poy_pivot_table.xlsx')

clutch_poy_pivot_table_df.to_excel('clutch_poy_pivot_table.xlsx', index=False)

print(clutch_poy_pivot_table_df)
# dpoy
dpoy_pivot_table_df = \
    pd.pivot_table(dpoy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

dpoy_pivot_table_df.to_excel('dpoy_pivot_table.xlsx')

#print(dpoy_pivot_table_df.sort_values(by=['award'], ascending=False))

dpoy_pivot_table_df = \
    pd.read_excel('dpoy_pivot_table.xlsx')

dpoy_pivot_table_df.to_excel('dpoy_pivot_table.xlsx', index=False)
# updating Dikembe Mutombo's dpoy award count from 6 to 4
dpoy_pivot_table_df['award'] = \
    dpoy_pivot_table_df['award'].where(
        ~dpoy_pivot_table_df['player_x'].\
            isin(['Dikembe Mutombo']), \
                4
    )

print(dpoy_pivot_table_df.sort_values(by=['award'], ascending=False))

dpoy_pivot_table_df.to_excel('dpoy_pivot_table.xlsx', index=False)
# mip
mip_pivot_table_df = \
    pd.pivot_table(mip_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

mip_pivot_table_df.to_excel('mip_pivot_table.xlsx')

mip_pivot_table_df = \
    pd.read_excel('mip_pivot_table.xlsx')

mip_pivot_table_df.to_excel('mip_pivot_table.xlsx', index=False)
# nba mvp
nba_mvp_pivot_table_df = \
    pd.pivot_table(nba_mvp_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

nba_mvp_pivot_table_df.to_excel('nba_mvp_pivot_table.xlsx')

nba_mvp_pivot_table_df = \
    pd.read_excel('nba_mvp_pivot_table.xlsx')

nba_mvp_pivot_table_df.to_excel('nba_mvp_pivot_table.xlsx', index=False)
# nba roy
nba_roy_pivot_table_df = \
    pd.pivot_table(nba_roy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

nba_roy_pivot_table_df.to_excel('nba_roy_pivot_table.xlsx')

nba_roy_pivot_table_df = \
    pd.read_excel('nba_roy_pivot_table.xlsx')

nba_roy_pivot_table_df.to_excel('nba_roy_pivot_table.xlsx', index=False)
# smoy
smoy_pivot_table_df = \
    pd.pivot_table(smoy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

smoy_pivot_table_df.to_excel('smoy_pivot_table.xlsx')

smoy_pivot_table_df = \
    pd.read_excel('smoy_pivot_table.xlsx')

smoy_pivot_table_df.to_excel('smoy_pivot_table.xlsx', index=False)
# aba mvp
aba_mvp_pivot_table_df = \
    pd.pivot_table(aba_mvp_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

aba_mvp_pivot_table_df.to_excel('aba_mvp_pivot_table.xlsx')

aba_mvp_pivot_table_df = \
    pd.read_excel('aba_mvp_pivot_table.xlsx')

aba_mvp_pivot_table_df.to_excel('aba_mvp_pivot_table.xlsx', index=False)
# aba roy
aba_roy_pivot_table_df = \
    pd.pivot_table(aba_roy_winners_df, index=['player_x'],
                   values=['award'], aggfunc='count')

aba_roy_pivot_table_df.to_excel('aba_roy_pivot_table.xlsx')

aba_roy_pivot_table_df = \
    pd.read_excel('aba_roy_pivot_table.xlsx')

aba_roy_pivot_table_df.to_excel('aba_roy_pivot_table.xlsx', index=False)

# updating Swen Nater's aba_roy award count from 3 to 1 since he was traded midseason
aba_roy_pivot_table_df['award'] = \
    aba_roy_pivot_table_df['award'].where(
        ~aba_roy_pivot_table_df['player_x'].\
            isin(['Swen Nater']), \
                1
    )

print(aba_roy_pivot_table_df.sort_values(by=['award'], ascending=False))

aba_roy_pivot_table_df.to_excel('aba_roy_pivot_table.xlsx', index=False)

# nba mvp and top 10 highest scoring averages
def nba_mvp_ppg(df):
    try:
        return df[(df['award'] == 'nba mvp') & 
                  (df['winner'] == 'True') & 
                  (df['season_ending_year_x'] == df['season_ending_year_y'])]
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
top_5_nba_mvp_ppg_df = top_5_nba_mvp_ppg_df.rename(columns={'season_ending_year_x': 'season_ending_year',
                                                            'player_x': 'player',
                                                            'age_x': 'age',
                                                            'tm_x':'team'})

top_5_nba_mvp_ppg_df.to_excel('top_5_nba_mvp_ppg_df.xlsx', index=False)

# rename certain columns in top_10_nba_mvp_ppg_df
top_10_nba_mvp_ppg_df = top_10_nba_mvp_ppg_df.rename(columns={'season_ending_year_x': 'season_ending_year',
                                                            'player_x': 'player',
                                                            'age_x': 'age',
                                                            'tm_x':'team'})

#print(top_10_nba_mvp_ppg_df)
top_10_nba_mvp_ppg_df.to_excel('top_10_nba_mvp_ppg_df.xlsx', index=False)


# rename a column in clutch_poy_pivot_table_df
clutch_poy_pivot_table_df = clutch_poy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

clutch_poy_pivot_table_df.to_excel('clutch_poy_pivot_table.xlsx', index=False)

# rename a column in dpoy_pivot_table_df
dpoy_pivot_table_df = dpoy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

dpoy_pivot_table_df.to_excel('dpoy_pivot_table.xlsx', index=False)

# rename a column in mip_pivot_table_df
mip_pivot_table_df = mip_pivot_table_df.\
    rename(columns={'player_x': 'player'})

mip_pivot_table_df.to_excel('mip_pivot_table.xlsx', index=False)

# rename a column in nba_mvp_pivot_table_df
nba_mvp_pivot_table_df = nba_mvp_pivot_table_df.\
    rename(columns={'player_x': 'player'})

nba_mvp_pivot_table_df.to_excel('nba_mvp_pivot_table.xlsx', index=False)

# rename a column in nba_roy_pivot_table_df
nba_roy_pivot_table_df = nba_roy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

nba_roy_pivot_table_df.to_excel('nba_roy_pivot_table.xlsx', index=False)

# rename a column in smoy_pivot_table_df
smoy_pivot_table_df = smoy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

smoy_pivot_table_df.to_excel('smoy_pivot_table.xlsx', index=False)

# rename a column in aba_mvp_pivot_table_df
aba_mvp_pivot_table_df = aba_mvp_pivot_table_df.\
    rename(columns={'player_x': 'player'})

aba_mvp_pivot_table_df.to_excel('aba_mvp_pivot_table.xlsx', index=False)

# rename a column in aba_roy_pivot_table_df
aba_roy_pivot_table_df = aba_roy_pivot_table_df.\
    rename(columns={'player_x': 'player'})

aba_roy_pivot_table_df.to_excel('aba_roy_pivot_table.xlsx', index=False)


print('creation and modification of pivot tables = success - ', (time.time() - start_time))


# ================= #
# creating more dfs 
# ================= #

# bill russell dataframe - per game averages
def bill_russell(df):
    try:
        return df[df['player'] == 'Bill Russell']
    except:
        print('cannot filter dataframe')

bill_russell_per_game_avgs_df = bill_russell(player_per_game_df)

bill_russell_per_game_avgs_df.to_excel('bill_russell_per_game_averages.xlsx', index=False)

# wilt chamberlain dataframe - per game averages
def wilt_chamberlain(df):
    try:
        return df[df['player'] == 'Wilt Chamberlain']
    except:
        print('cannot filter dataframe')

wilt_chamberlain_per_game_avgs_df = wilt_chamberlain(player_per_game_df)

wilt_chamberlain_per_game_avgs_df.to_excel(
    'wilt_chamberlain_per_game_averages.xlsx', index=False)

# merging bill russell and wilt chamberlain per game avgs dataframes 
#   (when they played in the same years only)
bill_russell_and_wilt_chamberlain_per_game_avgs_merged_df = pd.merge(bill_russell_per_game_avgs_df, 
                                                       wilt_chamberlain_per_game_avgs_df,
                                                       on=['season_ending_year'])

bill_russell_and_wilt_chamberlain_per_game_avgs_merged_df.to_excel(
    'bill_russell_and_wilt_chamberlain_per_game_avgs_merged.xlsx',
    index=False)

# michael jordan dataframe - per game averages
def michael_jordan(df):
    try:
        return df[df['player'] == 'Michael Jordan']
    except:
        print('cannot filter dataframe')

michael_jordan_per_game_avgs_df = michael_jordan(player_per_game_df)

michael_jordan_per_game_avgs_df.to_excel('michael_jordan_per_game_averages.xlsx', index=False)

# lebron james dataframe - per game averages
def lebron_james(df):
    try:
        return df[df['player'] == 'LeBron James']
    except:
        print('cannot filter dataframe')

lebron_james_per_game_avgs_df = lebron_james(player_per_game_df)

lebron_james_per_game_avgs_df.to_excel('lebron_james_per_game_averages.xlsx', index=False)
# michael jordan and lebron james - per game averages
def michael_jordan_and_lebron_james(df):
    try:
        return df[(df['player'] == 'LeBron James') | (df['player'] == 'Michael Jordan')]
    except:
        print('cannot filter dataframe')

michael_jordan_and_lebron_james_per_game_avgs_df = michael_jordan_and_lebron_james(player_per_game_df)

michael_jordan_and_lebron_james_per_game_avgs_df.to_excel('michael_jordan_and_lebron_james_per_game_averages.xlsx', index=False)
# michael jordan and lebron james - pivot table
michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df = pd.pivot_table(
    michael_jordan_and_lebron_james_per_game_avgs_df,index=['player'],
    values=['pts_per_game',
    'trb_per_game',
    'ast_per_game',
    'stl_per_game',
    'blk_per_game'], 
    aggfunc='mean')

print(michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df)

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df.\
    to_excel('michael_jordan_and_lebron_james_per_game_avgs_pivot_table.xlsx')

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df = \
    pd.read_excel('michael_jordan_and_lebron_james_per_game_avgs_pivot_table.xlsx')

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df.\
    to_excel('michael_jordan_and_lebron_james_per_game_avgs_pivot_table.xlsx', index=False)

cols = ['pts_per_game','trb_per_game','ast_per_game','stl_per_game','blk_per_game']

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df[cols] = \
    michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df[cols].round(2)

michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df.\
    to_excel('michael_jordan_and_lebron_james_per_game_avgs_pivot_table.xlsx', index=False)


print('creation of multiple dataframes for individual players = success - ', (time.time() - start_time))


# ================== #
# creating graphs via matplotlib
# ================== #
import matplotlib.pyplot as plt
# top 5 nba mvp ppg
x = top_5_nba_mvp_ppg_df['player'].astype(str) + '\n' +\
      top_5_nba_mvp_ppg_df['season_ending_year'].astype(str) + ' Season \n' +\
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
      top_10_nba_mvp_ppg_df['season_ending_year'].astype(str) + ' Season \n' +\
      top_10_nba_mvp_ppg_df['pts_per_game'].astype(str) + ' PPG' +\
      '\n'
y = top_10_nba_mvp_ppg_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('NBA MVP Winners Points Per Game Average - Top 10')
plt.xlabel('PLAYERS')
plt.ylabel('POINTS PER GAME')
plt.show()
# clutch poy
x = clutch_poy_pivot_table_df['player'].astype(str) + '\n'
y = clutch_poy_pivot_table_df['award']
plt.bar(x, y, color=color)
plt.title('# of Clutch POY Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# dpoy 
x = dpoy_pivot_table_df['player'].astype(str)
y = dpoy_pivot_table_df['award']
plt.barh(x, y, color=color)
plt.title('# of DPOY Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# mip 
x = mip_pivot_table_df['player'].astype(str)
y = mip_pivot_table_df['award']
plt.barh(x, y, color=color)
plt.title('# of MIP Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# nba mvp
x = nba_mvp_pivot_table_df['player'].astype(str)
y = nba_mvp_pivot_table_df['award']
plt.barh(x, y, color=color)
plt.title('# of NBA MVP Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# *NO ROY (NBA) CHART DUE TO QUANTITY ISSUE* #
# aba mvp
x = aba_mvp_pivot_table_df['player'].astype(str)
y = aba_mvp_pivot_table_df['award']
plt.bar(x, y, color=color)
plt.title('# of ABA MVP Awards Per Player')
plt.xlabel('PLAYERS')
plt.ylabel('# of Times Won')
plt.show()
# *NOT NECESSARY TO CREATE ABA_ROY CHART* #
# bill russell chart - rebounds per game
x = bill_russell_per_game_avgs_df['player'].astype(str) + '\n' + \
    bill_russell_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    bill_russell_per_game_avgs_df['trb_per_game'].astype(str) + ' RPG'
y = bill_russell_per_game_avgs_df['trb_per_game']
plt.bar(x, y, color=color)
plt.title('Bill Russell RPG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('RPG')
plt.show()
# bill russell chart - ast per game
x = bill_russell_per_game_avgs_df['player'].astype(str) + '\n' + \
    bill_russell_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    bill_russell_per_game_avgs_df['ast_per_game'].astype(str) + ' APG'
y = bill_russell_per_game_avgs_df['ast_per_game']
plt.bar(x, y, color=color)
plt.title('Bill Russell APG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('APG')
plt.show()
# bill russell chart - pts per game
x = bill_russell_per_game_avgs_df['player'].astype(str) + '\n' + \
    bill_russell_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    bill_russell_per_game_avgs_df['pts_per_game'].astype(str) + ' PPG'
y = bill_russell_per_game_avgs_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('Bill Russell PPG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('PPG')
plt.show()
# wilt chamberlain chart - rebounds per game
x = wilt_chamberlain_per_game_avgs_df['player'].astype(str) + '\n' + \
    wilt_chamberlain_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    wilt_chamberlain_per_game_avgs_df['trb_per_game'].astype(str) + ' RPG'
y = wilt_chamberlain_per_game_avgs_df['trb_per_game']
plt.bar(x, y, color=color)
plt.title('Wilt Chamberlain RPG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('RPG')
plt.show()
# wilt chamberlain chart - ast per game
x = wilt_chamberlain_per_game_avgs_df['player'].astype(str) + '\n' + \
    wilt_chamberlain_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    wilt_chamberlain_per_game_avgs_df['ast_per_game'].astype(str) + ' AST'
y = wilt_chamberlain_per_game_avgs_df['ast_per_game']
plt.bar(x, y, color=color)
plt.title('Wilt Chamberlain APG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('APG')
plt.show()
# wilt chamberlain chart - points per game
x = wilt_chamberlain_per_game_avgs_df['player'].astype(str) + '\n' + \
    wilt_chamberlain_per_game_avgs_df['season'].astype(str) + ' Season\n' + \
    wilt_chamberlain_per_game_avgs_df['pts_per_game'].astype(str) + ' PPG'
y = wilt_chamberlain_per_game_avgs_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('Wilt Chamberlain PPG By Year')
plt.xlabel('PLAYERS')
plt.ylabel('PPG')
plt.show()

# michael jordan and lebron james
x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['pts_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - PPG Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career PPG Averages')
plt.show()

x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['trb_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - RPG Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career RPG Averages')
plt.show()

x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['ast_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - AST Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career AST Averages')
plt.show()

x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['stl_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - SPG Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career SPG Averages')
plt.show()

x = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['player'].astype(str)
y = michael_jordan_and_lebron_james_per_game_avgs_pivot_table_df['blk_per_game']
plt.bar(x, y, color=color)
plt.title('Michael Jordan and Lebron James - BPG Career Avg')
plt.xlabel('PLAYERS')
plt.ylabel('Career BPG Averages')
plt.show()


print('development of charts = success - ', (time.time() - start_time))


# =============== #
# conditional formatting 
# =============== #

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
    applymap(award_winners_highlighted)
)

player_award_shares_and_player_per_game_merged_styled_df.to_excel('player_award_shares_and_player_per_game_merged.xlsx', index=False)

# highlight max values in certain columns in the merged dataframe
bill_russell_and_wilt_chamberlain_per_game_avgs_merged_styled_df = \
    bill_russell_and_wilt_chamberlain_per_game_avgs_merged_df.style.\
        highlight_max(subset=[
            'trb_per_game_x', 
            'ast_per_game_x', 
            'pts_per_game_x',
            'trb_per_game_y', 
            'ast_per_game_y', 
            'pts_per_game_y'], 
            color='yellow', 
            axis=0)

bill_russell_and_wilt_chamberlain_per_game_avgs_merged_styled_df.\
    to_excel('bill_russell_and_wilt_chamberlain_per_game_avgs_merged.xlsx', index=False)

def player_per_game_highlighted(x):
    try:
        if x == 'N/A - Stat tracked as of the 1973-74 NBA Season' or x == 'N/A - Stat tracked as of the 1973-74 ABA Season' or x == 'N/A - Stat tracked as of the 1950-51 NBA Season':
            return 'background-color: red'
    except Exception as e:
        print(f'caught {type(e)}: e \n'
              f'cannot list results')
        
player_per_game_df = player_per_game_df.style.applymap(player_per_game_highlighted)

player_per_game_df.to_excel('Player Per Game.xlsx', index=False)


print('conditional formatting = success - ', (time.time() - start_time))

# ======================================================================== #