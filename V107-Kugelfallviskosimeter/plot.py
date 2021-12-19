import matplotlib.pyplot as plt
import numpy as np

#Daten laden
T, eta = np.genfromtxt('eta.txt', unpack=True)
x = 1/T
y = np.log(eta)

# Lineare Regression
params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

x_plot = np.linspace(0.00309, 0.00342, 100000)
plt.plot(x, y, 'x', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=1,
)
plt.grid()
plt.xlabel(r'$\frac{1}{T}\,/\,\unit{\per\kelvin}$')
plt.ylabel(r'$ln\left(\frac{\eta}{\unit{\pascal}\cdot \unit{\second}}\right)$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
