import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# for display
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# Load the data
df = pd.read_excel('resources/data/bitcoin_day.xlsx')

# Transform
df.columns = ['date','open','high','low','close','volumn','marketCap']
df['date'] = pd.to_datetime(df['date'])
df['log_close'] = np.log(df.close)
df['log_high'] = np.log(df.high)
df['log_low'] = np.log(df.low)

# Plot the data
sns.lineplot(y='close',x='date',data=df)
plt.title('Bitcoin Daily Close Price (all time)')
plt.show()

sns.lineplot(y='close',x='date',data=df[df['date']>= '2019-01-01'])
plt.title('Bitcoin Daily Close Price (2019 ~)')
plt.show()

