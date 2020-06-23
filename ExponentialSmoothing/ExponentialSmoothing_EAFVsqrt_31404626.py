from pandas import read_excel
from numpy import sqrt
import matplotlib.pyplot as plt

eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

eafv_sqrt =  sqrt(eafv_df)

plt.figure(1)
plt.subplot(211)
plt.title('eafv Square Root and Distribution')
plt.plot(eafv_sqrt)
plt.subplot(212)
plt.hist(eafv_sqrt)
plt.show()
