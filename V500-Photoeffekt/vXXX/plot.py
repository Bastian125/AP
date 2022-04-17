import numpy as np
import matplotlib.pyplot as plt

# Rote Spektrallinie
# Daten laden
U, I = np.genfromtxt('a1.txt' , unpack=True)

# Lineare Regression
params, covariance_matrix = np.polyfit(U, I, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')

# Plot
x_plot = np.linspace(0, 0.4)
plt.plot(U, I, 'x', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
# Label
plt.xlabel(r'$\frac{U_B}{V}$')
plt.ylabel(r'$\frac{I}{A}$')
plt.grid()
plt.legend()
plt.savefig('build/plot1.pdf')