import matplotlib.pyplot as plt
import numpy as np

T_r, a_r = np.genfromtxt('Messdaten_I_d.txt', unpack=True)
# Quadrieren
T = (T_r/3)**2
a = (a_r)**2

# Lineare Regression
params, covariance_matrix = np.polyfit(a, T, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
x_plot = np.linspace(0, 0.1)
plt.plot(a, T, 'x', label = r'Messwerte')
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=2,
)
plt.xlabel(r'$\frac{a^2}{\mathrm{m^2}}$')
plt.ylabel(r'$\frac{T^2}{\mathrm{s^2}}$')
plt.grid()
plt.legend()

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
