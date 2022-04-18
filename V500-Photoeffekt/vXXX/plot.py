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

# Grenzspannung bestimmen
from uncertainties import ufloat
a1 = ufloat(-1.47, 0.12)
a2 = ufloat(-7.06, 0.15)
a3 = ufloat(-14.81, 0.26)
a4 = ufloat(-7.68, 0.14)

b1 = ufloat(0.59, 0.02)
b2 = ufloat(3.05, 0.04)
b3 = ufloat(7.26, 0.07)
b4 = ufloat(7.05, 0.07)

print("U1: ", -b1/a1)
print("U2: ", -b2/a2)
print("U3: ", -b3/a3)
print("U4: ", -b4/a4)

# Grenzspannung gegen Frequenz auftragen
f  = [4.64e14, 5.19e14, 5.49e14, 6.89e14]
UG = [0.401, 0.432, 0.490, 0.918]

# Lineare Regression
params, covariance_matrix = np.polyfit(f, UG, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')

# Plot
x_plot = np.linspace(0, 8e14)
plt.plot(f, UG, 'x', label=r'$U_{G}/V$')
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$\frac{f}{Hz}$')
plt.ylabel(r'$\frac{U_G}{V}$')
plt.grid()
plt.legend()
plt.savefig('build/plot5.pdf')
plt.close()

# Spannung ueber den ganzen Bereich
U, I = np.genfromtxt('b.txt', unpack=True)

plt.plot(U, I, 'x', label="Messdaten der gelben Spektrallinie.")
plt.grid()
plt.xlabel('U/V')
plt.ylabel('I/A')
plt.legend()
plt.savefig('build/plot6.pdf')
plt.close()