from pandas import read_excel
import statsmodels.api as sm  
import itertools

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

mod = sm.tsa.statespace.SARIMAX(k54d_df, order=(0,1,1), 
                                seasonal_order=(0,1,1,12))
p = range(0, 2)
q = range(0, 3)
d = range(1, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
opt_aic = mod.fit(disp=False).aic
opt_values = ((0,1,1) + (0,1,1,12))
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(k54d_df,
                                            order=param,
                                            seasonal_order=param_seasonal)                                        
            if(opt_aic > mod.fit(disp=False).aic):
                opt_aic = mod.fit(disp=False).aic
                opt_values = (param + param_seasonal)
                print("AIC: ",opt_aic,"Values: ",opt_values)
        except:
            continue
print("Best optimal AIC: ", opt_aic, ", Optimal Parameter: ", opt_values)       
