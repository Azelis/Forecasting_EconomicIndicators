from pandas import read_excel
import matplotlib.pyplot as plt
from numpy import log

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
 

k54d_log =  log(k54d_df)

plt.figure(1)
plt.subplot(211)
plt.title('K54D Logarithm and Distribution')
plt.plot(k54d_log)
plt.subplot(212)
plt.hist(k54d_log)
plt.show()
