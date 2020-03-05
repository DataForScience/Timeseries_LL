stats = airline[['Year', 'Passengers']].groupby('Year').mean()
stats['Max'] = airline[['Year', 'Passengers']].groupby('Year').max()
stats['Min'] = airline[['Year', 'Passengers']].groupby('Year').min()
stats['Range'] = stats['Max']-stats['Min']

ax = stats.plot(y='Passengers', yerr='Range', legend=False)
ax.set_ylabel(r'$\langle Passengers\rangle$')

stats