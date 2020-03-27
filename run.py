from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

# based on https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/

def parser(x):
	#return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
	return x

series = read_csv('data/indonesia.csv', header=0, parse_dates=[0], index_col=1, squeeze=True, date_parser=parser)

X = series.values

size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()

for t in range(len(test)):
	model = ARIMA(history, order=(5,1,1))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history = append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))

error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

