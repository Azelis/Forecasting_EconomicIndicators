from pandas import read_excel
from numpy import log
import matplotlib.pyplot as plt

k226_df_all = read_excel('K226data_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

k226_df = k226_df_all['2013-01-01':]

k226_log = log(k226_df)

plt.figure(1)
plt.subplot(211)
plt.title('K226 Logarithm and Distribution')
plt.plot(k226_log)
plt.subplot(212)
plt.hist(k226_log)
plt.show()
