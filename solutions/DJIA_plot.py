DJIA = pd.read_csv('data/DJIA.csv', parse_dates=['DATE'], na_values='.')
# Since the dataset uses '.' to signal NA valeus, pandas represented that column as a 
# string instead of a float

DJIA.set_index('DATE', inplace=True)
ax = DJIA.plot(legend=False)
ax.set_ylabel('DJIA')
ax.set_xlabel('Date')