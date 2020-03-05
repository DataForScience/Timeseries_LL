DJIA['mean30'] = DJIA['DJIA'].rolling(30).mean()
DJIA['max30'] = DJIA['DJIA'].rolling(60).max()
DJIA['min30'] = DJIA['DJIA'].rolling(60).min()

ax = DJIA[['DJIA', 'mean30', 'max30', 'min30']].plot(lw=2)
ax.fill_between(x=DJIA.index, y1=DJIA['max30'].values, y2=DJIA['min30'].values, alpha=0.5)

ax.set_ylabel('DJIA')
ax.set_xlabel('Date')
ax.legend(['daily', '30 day average', '30 day max', '30 day min'])