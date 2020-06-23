from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
 

fit_1_train = ExponentialSmoothing(k54d_df[0:-12], seasonal_periods=12, trend='add', seasonal='mul').fit()

k54d_test = k54d_df[-12:]


fcast_1_train = fit_1_train.forecast(12)

   
plt.title('K54D Forecast 2019 by splitt data')  
fcast_1_train.plot(label='Trained forecast', legend=True, color="red")
k54d_test.plot(label='Actual', legend=True, color="black")
plt.show()