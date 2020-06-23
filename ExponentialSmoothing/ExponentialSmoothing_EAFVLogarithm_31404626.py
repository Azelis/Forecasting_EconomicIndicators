from pandas import read_excel
from numpy import log
import matplotlib.pyplot as plt

eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

eafv_log =  log(eafv_df)

plt.figure(1)
plt.subplot(211)
plt.title('eafv Logarithm and Distribution')
plt.plot(eafv_log)
plt.subplot(212)
plt.hist(eafv_log)
plt.show()
