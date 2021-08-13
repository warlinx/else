import pandas_datareader as pdr
import datetime

tick = 'AAPL'
start_date = datetime.datetime(2018, 10, 1)
end_date = datetime.datetime(2021, 4, 23)

aapl = pdr.get_data_yahoo(tick, start=start_date, end=end_date)

print(aapl['Close'].tail())

