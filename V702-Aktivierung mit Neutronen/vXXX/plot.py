import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat

# Vanadium
t_in, N_in = np.genfromtxt('messwerte/vanadium.txt', unpack=True)
t = 30*t_in
N = N_in - 9
n = np.around(np.sqrt(N), 0)
np.savetxt('messwerte/vanadium_messfehler', n)

# Fehlerrechnung
N_u = unp.uarray(N, n)
N_m = N_u/t
print(unp.exp(unp.uarray(0.49, 0.15)))
print(unp.log(2)/unp.uarray(6.4e-3, 0.28e-3))

# Lineare Regression
params, covariance_matrix = np.polyfit(t, np.log(unp.nominal_values(N_m)), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')

# Plotten
plt.plot(t, N/t, 'x', label='Messwerte')
plt.plot(
    t,
    np.exp(params[0] * t + params[1]),
    label='Lineare Regression',
    linewidth=3,
)
plt.errorbar(t, unp.nominal_values(N_m), unp.std_devs(N_m), fmt='bx')
plt.yscale('log')
plt.xlabel(r'$t/\unit{\second}$')
plt.ylabel(r'$\log{N}$')
plt.xlim(0, 950)
plt.grid()
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
plt.close()

# Silber
t_in, N_in = np.genfromtxt('messwerte/silber.txt', unpack=True)
t = t_in*10
N = N_in - 3
n = np.around(np.sqrt(N), 0)
np.savetxt('messwerte/silber_messfehler.txt', n)

# Fehlerrechnung
N_u = unp.uarray(N, n)
N_m = N_u/t

# Lineare Regression
params, covariance_matrix = np.polyfit(t, np.log(unp.nominal_values(N_m)), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')

# Plotten
plt.plot(t, N/t, 'x', label='Messwerte')
plt.plot(
    t,
    np.exp(params[0] * t + params[1]),
    label='Lineare Regression',
    linewidth=3,
)
plt.errorbar(t, unp.nominal_values(N_m), unp.std_devs(N_m), fmt='bx')
plt.yscale('log')
plt.xlabel(r'$t/\unit{\second}$')
plt.ylabel(r'$\log{N}$')
plt.xlim(0, 450)
plt.grid()
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.close()