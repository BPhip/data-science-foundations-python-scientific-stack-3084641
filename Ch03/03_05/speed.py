# %%
import pandas as pd

csv_file = 'track.csv'
df = pd.read_csv(csv_file, parse_dates=['time'])
df

# %%
import numpy as np

lat_km = 92
lng_km = 111


def distance(lat1, lng1, lat2, lng2):
    delta_lat = (lat1 - lat2) * lat_km
    delta_lng = (lng1 - lng2) * lng_km
    return np.hypot(delta_lat, delta_lng)
# %%
lat1, lng1 = df.loc[200]['lat'], df.iloc[200]['lng']
lat2, lng2 = df.loc[201]['lat'], df.iloc[201]['lng']
distance(lat1, lng1, lat2, lng2)
# %%
s = pd.Series(np.arange(5))
s # We are going to create a series of items 

# %%
s.shift() # Shift moves all items down by one, with 0 becoming NaN

# %%
s.shift(-1) # A shift of -1 increases everything by 1, with the top value going into NaN


# %%
dist = distance(
    df['lat'], df['lng'], 
    df['lat'].shift(), df['lng'].shift(),
)
dist[:5] # This is giving the distance between a point and the previous point and saving it to a dataframe

# %%
dist.sum() # This gives us a total of 4.7km (ish) - which sounds reasonable

# %%
times = df['time'].diff()
times[:5] # This gives a set of differences between each point and the last one

# %%
times.sum() # A total time of 32 mins - this is reasonable

# %%

times_hour = times / pd.Timedelta(1, 'hour')
times_hour[:5]

# %%
speed = dist / times_hour
speed[:5] # This is showing speed in km/h (with an error showing up of the 35 km/h)
# %%
