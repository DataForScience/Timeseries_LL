Sun = pd.read_csv('data/sun.csv', dtype={'YEAR':'int', 'SUNACTIVITY':'float'})
Sun.set_index('YEAR', inplace=True)

Sun['forward'] = Sun['SUNACTIVITY'].shift(11)
Sun['backward'] = Sun['SUNACTIVITY'].shift(-11)

ax = Sun.iloc[:50].plot(lw=2)
ax.set_ylabel('Sun spot activity')
ax.set_xlabel('Year')
ax.legend(['Original', '11 years forward', '11 years backwards'])