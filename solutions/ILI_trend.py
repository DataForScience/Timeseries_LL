ILI = pd.read_csv('data/CDC.csv')

stats = ILI[['Year', 'Percent of Deaths Due to Pneumonia and Influenza']].groupby('Year').mean()

ax = stats.plot(y='Percent of Deaths Due to Pneumonia and Influenza', legend=False)
ax.set_xlabel('Date')
ax.set_ylabel(r'$\langle\% Mortality\rangle$')