from pandas import read_excel
import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

fit_1 = ExponentialSmoothing(k54d_df, seasonal_periods=12, trend='add', seasonal='mul').fit()
fit_2 = ExponentialSmoothing(k54d_df, seasonal_periods=12, trend='add', seasonal='add').fit()

Error_1 = k54d_df - fit_1.fittedvalues
Error_2 = k54d_df - fit_2.fittedvalues

MSE1=sum(Error_1**2)*1.0/len(fit_1.fittedvalues)
MSE2=sum(Error_2**2)*1.0/len(fit_2.fittedvalues)


cars = {'Errors': ['MSE'],
        'HW add mul': [MSE1],
        'HW add add': [MSE2]
        }

AllErrors = pd.DataFrame(cars, columns = ['Errors', 'HW add mul',
                                          'HW add add'])
print(AllErrors)