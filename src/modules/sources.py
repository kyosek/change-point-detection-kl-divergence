import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# for display
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# Load the data
df = pd.read_excel('resources/data/bitcoin_day.xlsx')

# Transform
df.columns = ['date','open','high','low','close','volume','marketCap']
df = df.sort_values(['date'])
df['date'] = pd.to_datetime(df['date'])
