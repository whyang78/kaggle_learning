import pandas_datareader as pdr
import pandas as pd
start_date = pd.to_datetime('2000-01-01')
stop_date = pd.to_datetime('2016-03-01')
spy = pdr.data.get_data_yahoo('SPY', start_date, stop_date)
spy.to_csv('./a.csv')