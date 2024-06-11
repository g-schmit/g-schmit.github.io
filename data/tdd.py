import pandas as pd
from IPython.display import display

# df = pd.read_csv('stardew/fish_detail.csv')
# df.columns = [c.replace('& ', '') for c in df.columns]
# df.columns = [c.replace('(', '') for c in df.columns]
# df.columns = [c.replace(')', '') for c in df.columns]
# df.columns = [c.replace(' ', '_') for c in df.columns]
# df[['Difficulty', 'Behavior']] = df.Difficulty_Behavior.str.split(" ", expand=True)
# df.drop(['Difficulty_Behavior'], axis = 1, inplace=True)
# df['Difficulty'] = df['Difficulty'].astype(int)
# df.loc[df['Time'] == 'Anytime', 'Time'] = '0am - 12am'
# df['Time'] = df['Time'].str.replace('–', '-')
# df['Time'] = df['Time'].str.replace('\r', '')
# # df['Time'] = df['Time'].str.replace('am', '')
# # df['Time'] = df['Time'].str.replace('12am', '0')
# df[['Time1', 'Time2']] = df.Time.str.split("\n", expand = True)
# df[['Start_Time1', 'Stop_Time1']] = df.Time1.str.split(" - ", expand = True)
# df[['Start_Time2', 'Stop_Time2']] = df.Time2.str.split(" - ", expand = True)
# pd.set_option('display.max_columns', None)
# df.drop(['Time'], axis = 1, inplace=True)
# df.drop(['Time1'], axis = 1, inplace=True)
# df.drop(['Time2'], axis = 1, inplace=True)
# df.to_csv('stardew/fish_detail2.csv')

df = pd.read_csv('stardew/fish_detail2.csv')
pd.set_option('display.max_columns', None)
display(df)