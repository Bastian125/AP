import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import scipy.optimize as opt

# eckiger Stab einseitig eingespannt

def D(x, E):
    r = 0.010 # radius der staebe in meter
    m = 0.6529 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = r**4 / 12 # flaechentraegheistmoment
    L = 0.4882 # hebelarm in metern
    return F / (2 * E * I) * (L * x**2 - x**3 / 3)

L = 0.4882 # aufhaengepunkt in m
x2, kaka, pupu, D2 = np.genfromtxt('Messwerte/MesswerteDX2.txt', unpack=True)
x1 = x2 * 0.001
D1 = D2 * 0.001

lx = np.abs(L - x1)

# curve fit

popt, pcov = opt.curve_fit(D, x1, D1)
E = popt[0]
print(f'Elastizitätsmodul für den eckigen Stab bei einseitiger Einspannung \t {E:.4}')
error = np.sqrt(np.diag(pcov))
e = error[0]
print(f'Abweichung: \t{error[0]:.4}')

# plot der messdaten
plt.scatter(D(x1, E), D1, c='b', marker='+', 
    label='Messwerte')
plt.title(rf'Messdaten für den eckigen Stab bei einseitiger Einspannung')

# plot der Theoriekurve
x = np.linspace(0,L)
plt.plot(D(x, E), D(x,E), 'r', 
        label=rf'Theoriekurve für $E={{{E:.4}}}$')
# plot der sigma umgebung
plt.fill_between(D(x, E), D(x,E+e), D(x,E-e), 
        facecolor='red', alpha=0.5, label=rf'$\sigma$-Umgebung')

plt.legend()
plt.xlabel(r'$\left(L \cdot x^2 - \frac{x^3}{3}\right)/ \si{m}$')
plt.ylabel(r'$D(x) / \si{m}$')

plt.tight_layout()
plt.savefig('build/plot3.pdf')
plt.close()