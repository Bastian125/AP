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
#print(unp.exp(unp.uarray(0.49, 0.15)))
#print(unp.log(2)/unp.uarray(6.4e-3, 0.28e-3))

# Lineare Regression 1
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
N_m_1 = N_u/t
N_m = N/t
t1 = t[0:7]
t2 = t[12:42]
N_korr = 13*(1-np.exp(-80.95e-4*10))*np.exp(-80.95e-4*t1)
N1 = N_m[0:7]-N_korr
N2 = N_m[12:42] 
print(unp.log(2)/unp.uarray(80.95e-4, 13.46e-4))
print(unp.log(2)/unp.uarray(89.67e-3, 18.04e-3))

# Lineare Regression 1
params1, covariance_matrix1 = np.polyfit(t1, np.log(N1), deg=1, cov=True)

errors1 = np.sqrt(np.diag(covariance_matrix1))

for name, value, error in zip('ab', params1, errors1):
    print(f'{name} = {value} ± {error}')

# Lineare Regression 2
params2, covariance_matrix2 = np.polyfit(t2, np.log(N2), deg=1, cov=True)

errors2 = np.sqrt(np.diag(covariance_matrix2))

for name, value, error in zip('ab', params2, errors2):
    print(f'{name} = {value} ± {error}')

# Plotten
plt.plot(t, N_m, 'x', label='Messwerte')
plt.plot(
    t1,
    np.exp(params1[0] * t1 + params1[1]),
    label='Lineare Regression 1',
    linewidth=3,
)
plt.plot(
    t2,
    np.exp(params2[0] * t2 + params2[1]),
    label='Lineare Regression 2',
    linewidth=3,
)
plt.errorbar(t, unp.nominal_values(N_m_1), unp.std_devs(N_m_1), fmt='bx')
plt.yscale('log')
plt.xlabel(r'$t/\unit{\second}$')
plt.ylabel(r'$\log{N}$')
plt.xlim(0, 450)
plt.ylim(0, 100)
plt.vlines(120, 0, 100, 'r', 'dashed')
plt.grid()
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.close()