import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates   #matplotlib does not use datetime dates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#read in our saved csv file
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)


#alternative method. Use min periods to adjust 100 day ma.
#Days with less than 99 days of history will use the data available to them.
#df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods = 0).mean()

#open high low close - samples averaged over 10 days to shrink data set
df_ohlc = df['Adj Close'].resample('10D').ohlc()

df_volume = df['Volume'].resample('10D').sum()

#reset index so that date is now a column
df_ohlc.reset_index(inplace = True)

#convert dates to matplotlib freindly date structure
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


ax1 = plt.subplot2grid((6, 1),  (0, 0), rowspan = 5, colspan=1)
ax2 = plt.subplot2grid((6, 1),  (5, 0), rowspan = 1, colspan=1, sharex = ax1)

#display mdates as human readable dates
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()