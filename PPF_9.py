#processing data for machine learning

import numpy as np
import pandas as pd
import pickle
def process_data_for_labels(ticker):
    #how many days to make or lose x%
    hm_days = 7

    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days + 1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    #fill NaN data values with 0 - done in place
    df.fillna(0, inplace=True)

    return tickers, df

#*args allows us to pass any number of variables
def buy_sell_hold(*args):
    cols = [c for c in args]

    #if our stock price changes by our requirement - do something
    requirement = 0.02

    for col in cols:
        if col > requirement:
            return 1

        if col < -requirement:
            return -1

    return 0
