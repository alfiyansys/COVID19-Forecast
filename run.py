from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot

series = read_csv('data/indonesia.csv', header=0, parse_dates=[0])

print(series)