from pandas import read_excel
from numpy import log, exp
from statsmodels.tsa.api import Holt
import pandas as pd

k226_df_all = read_excel('K226data_31404626.xls', shee_tname='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

k226_df = k226_df_all['2013-01-01':]
k226_log =  log(k226_df)

fit_1 = Holt(k226_df).fit(optimized=True)
fit_2 = Holt(k226_log).fit(optimized=True)

Error_1 = k226_df - fit_1.fittedvalues
Error_2 = k226_df - exp(fit_2.fittedvalues)

MSE1=sum(Error_1**2)*1.0/len(fit_1.fittedvalues)
MSE2=sum(Error_2**2)*1.0/len(exp(fit_2.fittedvalues))

cars = {'Errors': ['MSE','MSE Log'],
        'LES': [MSE1, MSE2]
        }

AllErrors = pd.DataFrame(cars, columns = ['Errors', 'LES'])
print(AllErrors)