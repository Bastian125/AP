import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import pandas as pd

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
plt.clf()
###################

# daten input, anpassung auf SI-Größen
f, A, U, a, b = np.genfromtxt('Mbc.txt', unpack=True)

# Spannung der Quelle
U0 = 1.6

# alles in ein dataframe fuer die ausgabe
data = {'f': f, 'UC': A, 'Urel': A/U0}
df_new = pd.DataFrame(data)
print('Messdaten zum Amplitudenverhaeltnis')
print(df_new)

# anpassung auf spannungsverhaeltnis
A = A / U0

# curve fit
def AC(f, T):
    U0 = 1.6
    w = 2 * np.pi * f
    return 2.44 / (np.sqrt(1 + w**2 * T**2))

p0 = [0.0008]
om = 2 * np.pi * f
popt, pcov = curve_fit(AC, f, A, p0=p0)
#U0 = popt[0]
U0 = 1.6
T = popt[0]
err = np.sqrt(np.diag(pcov))[0]

# output
#print(f'U0 = {U0:.4}')
print(f'RC = {10**6*T:.1f} ± {10**6*err:.2} micro-seconds')

 #plot
f_plt = np.linspace(3*10**2,10**5,10**4)
plt.scatter(f,A, marker='+', label='Messwerte')
plt.plot(f_plt, AC(f_plt, T), color='r', label=rf'Ausgleichsfunktion',
        linewidth=0.4)

plt.title(r'Spannungsverhältnis $A(\omega) / U_0$ im RC-Kreis')
plt.ylabel(r'$A(\omega) / U_0$')
plt.xlabel(r'$f / \unit{\hertz}$')
plt.xscale('log')
plt.legend()

plt.savefig('build/plot2.pdf')
#plt.show()
