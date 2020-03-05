Sun = pd.read_csv('data/sun.csv')
Sun.set_index('YEAR', inplace=True)

N=250

sun_forecast02 = forecast(Sun['SUNACTIVITY'], 0.2, N)
sun_forecast04 = forecast(Sun['SUNACTIVITY'], 0.4, N)
sun_forecast06 = forecast(Sun['SUNACTIVITY'], 0.6, N)

ax = Sun.iloc[N:].plot(y=['SUNACTIVITY'], lw=2)

ax.plot(Sun.index[N:], sun_forecast02, lw=2)
ax.plot(Sun.index[N:], sun_forecast04, lw=2)
ax.plot(Sun.index[N:], sun_forecast06, lw=2)


ax.legend(['Real', r'$forecast~\alpha=0.2$', r'$forecast~\alpha=0.4$', r'$forecast~\alpha=0.6$'])