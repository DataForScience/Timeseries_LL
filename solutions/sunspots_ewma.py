err = []
alphas = np.linspace(0.01, 1, 100)
for alpha in alphas:
    err.append(RMSE(Sun['SUNACTIVITY'].iloc[N:], forecast(Sun['SUNACTIVITY'], alpha, N)))
    

fig, ax = plt.subplots(1)
ax.plot(alphas, err)
ax.set_ylabel('RMSE')
ax.set_xlabel(r'$\alpha$')

opt_alpha = alphas[np.argmin(err)]
ax.vlines(opt_alpha, *ax.get_ylim(), linestyle='-.', colors='r', alpha=0.4)
print(opt_alpha)