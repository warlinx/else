import pandas_datareader as pdr
import datetime

<<<<<<< HEAD
tick = 'AAPL'
start_date = datetime.datetime(2018, 10, 1)
end_date = datetime.datetime(2021, 4, 23)

aapl = pdr.get_data_yahoo(tick, start=start_date, end=end_date)

print(aapl['Close'].tail())

=======
aapl = pdr.get_data_yahoo('AAPL',
                          start=datetime.datetime(2018, 10, 1),
                          end=datetime.datetime(2021, 4, 23))

# import quandl
# aapl1 = quandl.get("WIKI/AAPL", start_date="2018-10-01", end_date="2021-04-23")


print(aapl.head())
# print(aapl1.head())
>>>>>>> origin/master

