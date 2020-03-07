ax = series['GDP'].diff().plot()
ax.plot([series.index.min(), series.index.max()], [0, 0], '--')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Differences');