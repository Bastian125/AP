import numpy as np
import matplotlib.pyplot as plt

# Rote Spektrallinie
# Daten laden
U, I_a = np.genfromtxt('a1.txt' , unpack=True)
I = np.sqrt(I_a)

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
plt.ylabel(r'$\frac{I}{\sqrt{A}}$')
plt.grid()
plt.legend()
plt.savefig('build/plot1.pdf')
plt.close()

# Gelbe Spektrallinie
# Daten laden
U, I_a = np.genfromtxt('a2.txt' , unpack=True)
I = np.sqrt(I_a)

# Lineare Regression
params, covariance_matrix = np.polyfit(U, I, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')

# Plot
x_plot = np.linspace(0, 0.45)
plt.plot(U, I, 'x', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
# Label
plt.xlabel(r'$\frac{U_B}{V}$')
plt.ylabel(r'$\frac{I}{\sqrt{A}}$')
plt.grid()
plt.legend()
plt.savefig('build/plot2.pdf')
plt.close()

# Gruene Spektrallinie
# Daten laden
U, I_a = np.genfromtxt('a3.txt' , unpack=True)
I = np.sqrt(I_a)

# Lineare Regression
params, covariance_matrix = np.polyfit(U, I, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')

# Plot
x_plot = np.linspace(0, 0.5)
plt.plot(U, I, 'x', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
# Label
plt.xlabel(r'$\frac{U_B}{V}$')
plt.ylabel(r'$\frac{I}{\sqrt{A}}$')
plt.grid()
plt.legend()
plt.savefig('build/plot3.pdf')
plt.close()

# Violette Spektrallinie 1
# Daten laden
U, I_a = np.genfromtxt('a4.txt' , unpack=True)
I = np.sqrt(I_a)

# Lineare Regression
params, covariance_matrix = np.polyfit(U, I, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')

# Plot
x_plot = np.linspace(0, 0.9)
plt.plot(U, I, 'x', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
# Label
plt.xlabel(r'$\frac{U_B}{V}$')
plt.ylabel(r'$\frac{I}{\sqrt{A}}$')
plt.grid()
plt.legend()
plt.savefig('build/plot4.pdf')
plt.close()