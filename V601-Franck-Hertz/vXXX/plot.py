import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unp
from scipy import stats
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as const

U_A, delta_I = np.genfromtxt('Messwerte/a.txt', unpack = True)
plt.plot(U_A,delta_I,'bx',label='Lokale Auffängerstromänderung')
plt.xlabel(r'$U_A \,/\,\si{\volt}$')
plt.ylabel(r'$\symup{\Delta}I_A\,/\,\unit{\ampere}$')
plt.legend(loc='best')
plt.grid(which="both")
plt.tight_layout(pad=0, h_pad=1.10, w_pad=1.08)
plt.savefig('build/27Grad.pdf')
plt.close()

U_A2, delta_I2 = np.genfromtxt('Messwerte/b.txt', unpack = True)
plt.plot(U_A2,delta_I2,'bx',label='Lokale Auffängerstromänderung')
plt.xlabel(r'$U_A \,/\,\unit{\volt}$')
plt.ylabel(r'$\symup{\Delta}I_A\,/\,\si{\ampere}$')
plt.legend(loc='best')
plt.grid(which="both")
plt.tight_layout(pad=0, h_pad=1.10, w_pad=1.08)
plt.savefig('build/160Grad.pdf')
plt.close()

E_1 = [5.2,4.6,4.7,5.5]
E_1_mean = np.mean(E_1)
E_1_err = np.std(E_1)
E_1_= ufloat(E_1_mean,E_1_err)
c=3*10**8
h=4.136*10**-15
print(f'Anregungsenergie Reihe 1: {E_1_} eV')
print(f'Emittierte Strahlung 1: {c*h/E_1_*10**9} nm')

E_2 = [4.7,4.7,4.9,5.0,4.7]
E_2_mean = np.mean(E_2)
E_2_err = np.std(E_2)
E_2_= ufloat(E_2_mean,E_2_err)
c=3*10**8
h=4.136*10**-15
print(f'Anregungsenergie Reihe 1: {E_2_} eV')
print(f'Emittierte Strahlung 1: {c*h/E_2_*10**9} nm')