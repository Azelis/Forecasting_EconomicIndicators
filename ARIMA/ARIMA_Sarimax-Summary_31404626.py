from pandas import read_excel
import statsmodels.api as sm  

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

mod = sm.tsa.statespace.SARIMAX(k54d_df, order=(0,1,1), 
                                seasonal_order=(0,1,1,12))
print(mod.fit(disp=False).summary())

mod1 = sm.tsa.statespace.SARIMAX(k54d_df, order=(0,1,2), 
                                seasonal_order=(0,1,2,12))
results = mod1.fit(disp=False)

print(results.summary())