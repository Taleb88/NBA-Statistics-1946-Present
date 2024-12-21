import pandas as pd

all_star_selections = pd.read_csv('csv/All-Star Selections.csv')

print(all_star_selections)

def michael_jordan(df):
    return df[df['player'] == 'Michael Jordan']

all_star_selections = michael_jordan(all_star_selections)

print(all_star_selections)