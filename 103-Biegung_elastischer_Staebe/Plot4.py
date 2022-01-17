import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import scipy.optimize as opt

# eckiger Stab einseitig eingespannt

def D_mit(x, E):
    r = 0.010 # radius der staebe in meter
    m = 1.5528 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = r**4 / 12 # flaechentraegheistmoment
    L = 0.5572 # hebelarm in metern
    return F / (48 * E * I) * (3 * L**2 * x - 4 * x**3)

def D_mit_left(x,E):
    r = 0.010 # radius der staebe in meter
    m = 1.5528 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = r**4 / 12 # flaechentraegheistmoment
    L = 0.5572 # hebelarm in metern
    return F / (48 * E * I) * (4 * x**3 - 12 * L * x**2 + 9 * L**2 * x - L**3)

# allgemeine Daten
r = 0.010 # radius der staebe in meter
m = 1.5528 # masse des gewichtes in Kg

F = m * 9.81 # Kraft durch die Masse m

I = r**4 / 12 # flaechentraegheistmoment

### messung 1 ###
# stab der an beiden enden aufliegt
L = 0.275 # mitte in cm

### data import ###
x2, kaka, pupu, D2 = np.genfromtxt('Messwerte/MesswerteDX3.txt', unpack=True)
x1 = x2 * 0.001
D1 = D2 * 0.001


### data cleaning ###

pos_right = x1[x1 < 0.275]
pos_left = x1[x1 > 0.275]
data_right = D1[x1 < 0.275]
data_left = D1[x1 > 0.275]

fitting_data = np.append(data_left, data_right)
pos_mirrored = (.275 - (pos_left - .275))
fitting_x = np.append(pos_mirrored, pos_right)

print(fitting_x)
print(fitting_data)

# curve-fit 
popt, pcov = opt.curve_fit(D_mit, fitting_x, fitting_data)
error = np.sqrt(np.diag(pcov))
E = popt[0]
e = error[0]

print(f'E-Modul fuer runder bei beidseitiger Auflage:\t{E:.4}')
print(f'Abweichung: \t{error[0]:.4}')

### plot der Theoriekurve ###
# linke haelfte
x = np.linspace(0,0.275)
plt.plot(D_mit(x, E), D_mit(x,E), 'r',
        label=rf'Theoriekurve für $E=({{{E:.5}}})$Pa')
plt.fill_between(D_mit(x, E), D_mit(x,E+e), D_mit(x,E-e), 
        facecolor='red', alpha=0.3, label=rf'$\sigma$-Umgebung')
# rechte haelfte
x = np.linspace(.275,0.55)

plt.plot(D_mit_left(x, E), D_mit_left(x,E), 'r')
plt.fill_between(D_mit_left(x, E), D_mit_left(x,E+e), D_mit_left(x,E-e), 
        facecolor='red', alpha=0.3)

# datenpunkte
plt.scatter(D_mit(x1, E), D1, c='b', marker='+', label='Messwerte')

# visuals
plt.xlabel(r'$\left(3L^2 x -4Lx^2\right)$ bzw $\left(4x^3 -12Lx^2 +9L^2 x - L^3\right)$ / \si{m}$')
plt.ylabel(r'$D(x) / \si{m}$')
plt.title(rf'Messdaten für den eckigen Stab bei beidseitiger Auflage')
plt.legend()

plt.savefig('build/plot9.pdf')

plt.close()