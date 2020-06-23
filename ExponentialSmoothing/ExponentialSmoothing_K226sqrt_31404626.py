from pandas import read_excel
from numpy import sqrt
import matplotlib.pyplot as plt

########################## Data Preparation
k226_df_all = read_excel('K226data_31404626.xls', shee_tname='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

k226_df = k226_df_all['2013-01-01':]

k226_sqrt =  sqrt(k226_df)

plt.figure(1)
plt.subplot(211)
plt.title('k226 Square Root and Distribution')
plt.plot(k226_sqrt)
plt.subplot(212)
plt.hist(k226_sqrt)
plt.show()