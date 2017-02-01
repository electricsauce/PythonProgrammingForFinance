import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#read in our saved csv file
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

#df['100ma'] = df['Adj Close'].rolling(window = 100).mean()

#modify dataframe in place to deal NaN results(days 0 - 99 cannot have a 100 day obing average)
#data will now start 100 days after the begin date
#df.dropna(inplace = True)

#alternative method. Use min periods to adjust 100 day ma.
#Days with less than 99 days of history will use the data available to them.
df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods = 0).mean()


#print(df.head())

ax1 = plt.subplot2grid((6, 1),  (0, 0), rowspan = 5, colspan=1)
ax2 = plt.subplot2grid((6, 1),  (5, 0), rowspan = 1, colspan=1, sharex = ax1)

ax1.plot(df.index, df['Adj Close'], label = 'Adj Close')
ax1.plot(df.index, df['100ma'], label = '100ma')
ax2.bar(df.index, df['Volume'], label = 'Volume')

#legend is in the wrong place for both graphs???
plt.legend(loc = 'best')

plt.show()