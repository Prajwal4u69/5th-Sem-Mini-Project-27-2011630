import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Make function for calls to Yahoo Finance
def get_adj_close(ticker, start, end):
    '''
    A function that takes ticker symbols, starting period, ending period
    as arguments and returns with a Pandas DataFrame of the Adjusted Close Prices
    for the tickers from Yahoo Finance
    '''
    start = start
    end = end
    info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
    return pd.DataFrame(info)


apple =  get_adj_close('aapl', '01/01/2018', '23/11/2018')  
fb = get_adj_close('fb', '01/01/2018', '23/11/2018')
tesla = get_adj_close('tsla', '01/01/2018', '23/11/2018')
amazon = get_adj_close('amzn', '01/01/2018', '23/11/2018')
intel = get_adj_close('intc', '01/01/2018', '23/11/2018')
adobe = get_adj_close('adbe', '01/01/2018', '23/11/2018')
TCS = get_adj_close('tcs', '01/01/2018', '23/11/2018')
coca = get_adj_close('ko', '01/01/2018', '23/11/2018')
#Capgemini = get_adj_close('cap', '1/11/2018', '23/11/2018')
accenture = get_adj_close('acn', '01/01/2018', '23/11/2018')

# WIPRO TCS  KO (coacola)  CAP ACN
# Calculate 30 Day Moving Average, Std Deviation, Upper Band and Lower Band
for item in (apple,fb, tesla, amazon,intel,adobe,TCS,coca,accenture):
    item['30 Day MA'] = item['Adj Close'].rolling(window=20).mean()
    item['30 Day STD'] = item['Adj Close'].rolling(window=20).std()
    item['Upper Band'] = item['30 Day MA'] + (item['30 Day STD'] * 2)
    item['Lower Band'] = item['30 Day MA'] - (item['30 Day STD'] * 2)

# set style, empty figure and axes
plt.style.use('fivethirtyeight')



apple[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('APPLE')
plt.ylabel('Price (USD)')
plt.show();

fb[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Facebook')
plt.ylabel('Price (USD)')
plt.show();


tesla[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Tesla')
plt.ylabel('Price (USD)')
plt.show();


amazon[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Amazon')
plt.ylabel('Price (USD)')
plt.show();

intel[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Intel Corporation')
plt.ylabel('Price (USD)')
plt.show();

adobe[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Adobe Inc')
plt.ylabel('Price (USD)')
plt.show();


TCS[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Technical Service Consultancy')
plt.ylabel('Price (USD)')
plt.show();


coca[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('The Coca Cola Company')
plt.ylabel('Price (USD)')
plt.show();


'''

Capgemini[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Capgemini SE')
plt.ylabel('Price (USD)')
plt.show();
'''



accenture[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Accenture')
plt.ylabel('Price (USD)')
plt.show();





## Getting End of the  Day Stock


import quandl
quandl.ApiConfig.api_key = 'ecPnAnXSSAzyj3SxqVTg'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT','FB','TSLA','AMZN','INTC','ADBE','TCS','KO','CAP','ACN'], 
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                        date = { 'gte': '2018-01-22', 'lte': '2018-11-1' }, 
                        paginate=True)
print(data)
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Make function for calls to Yahoo Finance
def get_adj_close(ticker, start, end):
    '''
    A function that takes ticker symbols, starting period, ending period
    as arguments and returns with a Pandas DataFrame of the Adjusted Close Prices
    for the tickers from Yahoo Finance
    '''
    start = start
    end = end
    info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
    return pd.DataFrame(info)


apple =  get_adj_close('aapl', '01/01/2018', '23/11/2018')  
fb = get_adj_close('fb', '01/01/2018', '23/11/2018')
tesla = get_adj_close('tsla', '01/01/2018', '23/11/2018')
amazon = get_adj_close('amzn', '01/01/2018', '23/11/2018')
intel = get_adj_close('intc', '01/01/2018', '23/11/2018')
adobe = get_adj_close('adbe', '01/01/2018', '23/11/2018')
TCS = get_adj_close('tcs', '01/01/2018', '23/11/2018')
coca = get_adj_close('ko', '01/01/2018', '23/11/2018')
#Capgemini = get_adj_close('cap', '1/11/2018', '23/11/2018')
accenture = get_adj_close('acn', '01/01/2018', '23/11/2018')

# WIPRO TCS  KO (coacola)  CAP ACN
# Calculate 30 Day Moving Average, Std Deviation, Upper Band and Lower Band
for item in (apple,fb, tesla, amazon,intel,adobe,TCS,coca,accenture):
    item['30 Day MA'] = item['Adj Close'].rolling(window=20).mean()
    item['30 Day STD'] = item['Adj Close'].rolling(window=20).std()
    item['Upper Band'] = item['30 Day MA'] + (item['30 Day STD'] * 2)
    item['Lower Band'] = item['30 Day MA'] - (item['30 Day STD'] * 2)

# set style, empty figure and axes
plt.style.use('fivethirtyeight')



apple[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('APPLE')
plt.ylabel('Price (USD)')
plt.show();

fb[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Facebook')
plt.ylabel('Price (USD)')
plt.show();


tesla[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Tesla')
plt.ylabel('Price (USD)')
plt.show();


amazon[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Amazon')
plt.ylabel('Price (USD)')
plt.show();

intel[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Intel Corporation')
plt.ylabel('Price (USD)')
plt.show();

adobe[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Adobe Inc')
plt.ylabel('Price (USD)')
plt.show();


TCS[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Technical Service Consultancy')
plt.ylabel('Price (USD)')
plt.show();


coca[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('The Coca Cola Company')
plt.ylabel('Price (USD)')
plt.show();


'''

Capgemini[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Capgemini SE')
plt.ylabel('Price (USD)')
plt.show();
'''



accenture[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('Accenture')
plt.ylabel('Price (USD)')
plt.show();





## Getting End of the  Day Stock


import quandl
quandl.ApiConfig.api_key = 'ecPnAnXSSAzyj3SxqVTg'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT','FB','TSLA','AMZN','INTC','ADBE','TCS','KO','CAP','ACN'], 
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                        date = { 'gte': '2018-01-22', 'lte': '2018-11-1' }, 
                        paginate=True)
print(data)
