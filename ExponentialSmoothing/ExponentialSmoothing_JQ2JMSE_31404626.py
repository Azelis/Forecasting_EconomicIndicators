from pandas import read_excel
import pandas as pd
from numpy import log, exp, sqrt
from statsmodels.tsa.api import ExponentialSmoothing


jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

jq2j_log =  log(jq2j_df)
jq2j_sqrt =  sqrt(jq2j_df)

fit_1 = ExponentialSmoothing(jq2j_df, seasonal_periods=12, trend='add', seasonal='mul').fit()
fit_2 = ExponentialSmoothing(jq2j_df, seasonal_periods=12, trend='add', seasonal='add').fit()
fit_3 = ExponentialSmoothing(jq2j_log, seasonal_periods=12, trend='add', seasonal='mul').fit()
fit_4 = ExponentialSmoothing(jq2j_log, seasonal_periods=12, trend='add', seasonal='add').fit()
fit_5 = ExponentialSmoothing(jq2j_sqrt, seasonal_periods=12, trend='add', seasonal='mul').fit()
fit_6 = ExponentialSmoothing(jq2j_sqrt, seasonal_periods=12, trend='add', seasonal='add').fit()

############## Model Chosen  +ERROR RATE
Error_1 = jq2j_df - fit_1.fittedvalues
Error_2 = jq2j_df - fit_2.fittedvalues
Error_3 = jq2j_df - exp(fit_3.fittedvalues)
Error_4 = jq2j_df - exp(fit_4.fittedvalues)
Error_5 = jq2j_df - fit_5.fittedvalues**2
Error_6 = jq2j_df - fit_6.fittedvalues**2

MSE1=sum(Error_1**2)*1.0/len(fit_1.fittedvalues)
MSE2=sum(Error_2**2)*1.0/len(fit_2.fittedvalues)
MSE3=sum(Error_3**2)*1.0/len(exp(fit_3.fittedvalues))
MSE4=sum(Error_4**2)*1.0/len(exp(fit_4.fittedvalues))
MSE5=sum(Error_5**2)*1.0/len(fit_5.fittedvalues**2)
MSE6=sum(Error_6**2)*1.0/len(fit_6.fittedvalues**2)

cars = {'Errors': ['MSE','MSE Log','MSE sqrt'],
        'HW add mul': [MSE1, MSE3, MSE5],
        'HW add add': [MSE2, MSE4, MSE6]
        }

AllErrors = pd.DataFrame(cars, columns = ['Errors', 'HW add mul',
                                          'HW add add'])
print(AllErrors)
