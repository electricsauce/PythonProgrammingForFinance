#Get S&P 500 - the largest 500 companies by market capatilization

import bs4 as bs    #beautiful soup 4
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

save_sp500_tickers()

