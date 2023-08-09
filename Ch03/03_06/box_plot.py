# %%
import pandas as pd
import numpy as np

csv_file = 'track.csv'
df = pd.read_csv(csv_file, parse_dates=['time'])

lat_km = 92
lng_km = 111

def distance(lat1, lng1, lat2, lng2):
    delta_lat = (lat1 - lat2) * lat_km
    delta_lng = (lng1 - lng2) * lng_km
    return np.hypot(delta_lat, delta_lng)

dist = distance(
    df['lat'], df['lng'],
    df['lat'].shift(), df['lng'].shift(),
)
times = df['time'].diff()
times_hour = times / pd.Timedelta(1, 'hour')
speed = dist / times_hour

# %%
speed.describe() # This gives a summary of the dataset

# %%
speed.plot.box() # This outputs a boxplot of the dataset

# %%
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 6)
plt.style.use('seaborn-whitegrid')
speed.plot.box() # Here are some parameters that we can fiddle with

# %%
speed.name = '' # Further fiddling
ax = speed.plot.box(title="Miki's Run")
ax.set_ylabel(
    r'Running speed $\frac{km}{h}$')
# %%
