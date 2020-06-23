from pandas import read_excel
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)


eafv_df_ses = pd.DataFrame(eafv_df)
eafv_df_ses.reset_index(inplace=True)
eafv_df_ses['year'] = [d.year for d in eafv_df_ses.Date]
eafv_df_ses['month'] = [d.strftime('%b') for d in eafv_df_ses.Date]
years = eafv_df_ses['year'].unique()

sns.cubehelix_palette(len(years))

mycolors=sns.cubehelix_palette(len(years))
for i, y in enumerate(years):
    if i > 0:   
        plt.xlabel('Date')
        plt.title('eafv Seasonal Data')
        plt.plot('month', 'Yt', data=eafv_df_ses.loc[eafv_df_ses.year==y, :], color=mycolors[i], label=y)
        plt.text(eafv_df_ses.loc[eafv_df_ses.year==y, :].shape[0]-.9, 
                 eafv_df_ses.loc[eafv_df_ses.year==y, 'Yt'][-1:].values[0], 
                 y, fontsize=12, color=mycolors[i])
plt.show()