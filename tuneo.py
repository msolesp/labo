plt.errorbar(x, y, yerror, None, '.')

plt.rc('xtick',labelsize=12)
plt.rc('ytick',labelsize=12)
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=10)

plt.xlabel(r'Frecuencia señal generador  [Hz]', fontsize=12)
plt.ylabel(r'$V_R   [V]$', fontsize=14)

plt.show()
