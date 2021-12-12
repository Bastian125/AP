import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy

# daten input
U, l, t = np.genfromtxt('MaWerte.txt', unpack=True)


params, _fehler = np.polyfit(t,np.log(U/U[0]), deg=1, cov=True)

fehler = np.sqrt(np.diag(_fehler))
print("\nParams=",params)
print("fehler=", fehler)


uparams=unp.uarray(params,fehler)

x=np.linspace(t[-1],t[0],1000)
plt.figure()
plt.plot(t,np.log(U/U[0]),'.', color='gold',  label='Messwerte')
plt.plot(x, params[0]*x + params[1], color='navy',  label='Ausgleichsgerade')
plt.xlabel(r'$T \:/\: \unit{\second}$')
plt.ylabel(r'$ln\left(\frac{U_C}{U_0}\right) $')
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
###################