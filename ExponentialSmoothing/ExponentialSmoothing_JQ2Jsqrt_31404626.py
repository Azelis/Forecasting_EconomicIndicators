from pandas import read_excel
from numpy import sqrt
import matplotlib.pyplot as plt

jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

jq2j_sqrt =  sqrt(jq2j_df)

plt.figure(1)
plt.subplot(211)
plt.title('jq2j Square Root and Distribution')
plt.plot(jq2j_sqrt)
plt.subplot(212)
plt.hist(jq2j_sqrt)
plt.show()
