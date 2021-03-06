#Get S&P 500 - the largest 500 companies by market capatilization

import bs4 as bs    #beautiful soup 4
import datetime as dt
import os           #so we can create new directories
import pandas as pd
import pandas_datareader.data as web
import pickle       #serializes any python object
import requests

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")

    #find all sortable wikipedia tables on the referenced website
    table = soup.find('table', {'class' : 'wikitable sortable'})
    tickers = []

    #tr = table row, [1:] = tr 1 onward, td = table data
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0] .text      #get all data from 0th row - ticker names
        tickers.append(ticker)

    #save
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

#save_sp500_tickers()

def get_data_from_yaho(reload_sp500 = False, reload_data = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2016, 12, 31)

    if reload_data:
        for ticker in tickers:
        #only grabbing first 25 tickers for now
        #for ticker in tickers[:25]:
            print(ticker)
            if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
                df = web.DataReader(ticker, 'yahoo', start, end)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            else:
                print('Already have {}'.format(ticker))


#save_sp500_tickers()
get_data_from_yaho(False, True)