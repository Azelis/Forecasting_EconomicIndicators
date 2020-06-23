from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

X = k54d_df.values
diffSeries = list()
for i in range(1, len(X)):
	value = X[i] - X[i - 1]
	diffSeries.append(value)

plot_acf(diffSeries, title='ACF for First difference K54D', lags=50)
plt.show()
plot_pacf(diffSeries, title='PACF for First difference K54D', lags=50)
plt.show()

plt.title('K54D for First difference')
plt.plot(diffSeries,color="black")
plt.show()
