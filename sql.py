# sql only
import pandas as pd
import csv
import sqlite3

player_career_info_df = pd.read_excel('Player Career Info.xlsx')
player_career_info_df.to_csv('player_career_info.csv', index=False)

'''
# EXECUTED ON 1-12-2025
try:
    # import csv 
    with open('player_career_info.csv', 'r', encoding='utf-8') as file:
        dict_reader = csv.DictReader(file)
        player_data = [(x['player_id'],
                        x['player'],
                        x['birth_year'],
                        x['hof'],
                        x['num_seasons'],
                        x['first_season'],
                        x['last_season']) 
                        for x in dict_reader]
        print(player_data)

    # connect to db
    conn = sqlite3.connect('player_career_info_2025_01_12.db')
    cur = conn.cursor()

    # set up player_table in variable
    player_table = 'CREATE TABLE player(player_id INT NOT NULL,\
                                        player VARCHAR(50) NOT NULL, \
                                        birth_year INT, \
                                        hof VARCHAR(10) NOT NULL, \
                                        num_seasons INT NOT NULL, \
                                        first_season VARCHAR(10) NOT NULL, \
                                        last_season VARCHAR(10) NOT NULL);'

    # create player_table
    cur.execute(player_table)

    # insert data into player table
    cur.executemany('INSERT INTO player (player_id, player, birth_year, hof, num_seasons, first_season, last_season) \
                VALUES (?,?,?,?,?,?,?);', player_data)
    
    # display player table
    cur.execute('SELECT * FROM player')
    result = cur.fetchall()
    print(result)

    conn.commit() # commit changes

    if conn:
        print('data ingestion success')

    cur.close() # close db

except sqlite3.Error as error:
    print(f'error: ', error)
'''

# EXECUTED ON 1-12-2025 - QUERY TEST = SUCCESS
try: 
    # connect to db
    conn = sqlite3.connect('player_career_info_2025_01_12.db')
    cur = conn.cursor()

    # display player table
    cur.execute("SELECT * FROM player WHERE num_seasons >= 21 AND last_season <= 2025")
    result = cur.fetchall()
    print(result)

except sqlite3.Error as error:
    print(f'error: ', error)
