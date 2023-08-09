# %%
import pandas as pd

csv_file = 'track.csv'
df = pd.read_csv(csv_file, parse_dates=['time'])

# %%
df['lat']

# %%
df.lat # Don't do this! As column names with spaces won't work

# %%
df[['lat', 'lng']]

# %%
df['lat'][0]

# %%
df.loc[0] # .loc lets you see a whole row (in this case the 0'th row)

# %%
df.loc[2:7] # This slices to show you rows 2,3,4,5,6,7

# %%
df[['lat', 'lng']][2:7] # This slice is half-open (it includes the first index, but not the last) 

# %%
df.index

# %%
import numpy as np

df1 = pd.DataFrame(
    np.arange(10).reshape(5, 2),
    columns=['x', 'y'],
    index=['a', 'b', 'c', 'd', 'e'],
)
df1

# %%
df1.loc[0] # This fails as there is no row labeled 0

# %%
df1.loc['a'] # But this does work, as there is an 'a' index

# %%
df1.loc['a':'d']

# %%
df1.iloc[0] # .iloc works regarldess of row labels - it just works on location

# %%
df.index

# %%
df.index = df['time'] # The index is set to the time stamps
df.index

# %%
df.loc[0] # This fails as there is no 0 rows

# %%
df.loc['2015-08-20 03:48:34']

# %%

df.loc['2015-08-20 03:48'] # This selects all times that had 3 hours 48 mins
# %%
