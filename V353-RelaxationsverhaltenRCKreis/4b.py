# fuer Messung 4b
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# daten input, anpassung auf SI-Größen
f, A, U, a, b = np.genfromtxt('Mbc.txt', unpack=True)

# Spannung der Quelle
U0 = 1.6

# alles in ein dataframe fuer die ausgabe
data = {'f': f, 'UC': A, 'Urel': A/1.6}
df_new = pd.DataFrame(data)
print('Messdaten zum Amplitudenverhaeltnis')
print(df_new)

# anpassung auf spannungsverhaeltnis
A = A / 1.6

# curve fit
def AC(f, T):
    #U0 = 4.2
    U0 = 1 # damit das Verhaeltnis dargestellt wird
    w = 2 * np.pi * f
    return U0 / (np.sqrt(1 + w**2 * T**2))

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
plt.scatter(f,A, marker='+', label='Messdaten')
plt.plot(f_plt, AC(f_plt, T), color='r', label=rf'Curve Fit zu $RC={{{T * 10**6:.5}}}\mu\si{{s}}$',
        linewidth=0.4)

plt.title(r'Spannungsverhältnis $A(\omega) / U_0$ im RC-Kreis')
plt.ylabel(r'$A(\omega) / U_0$')
plt.xlabel(r'$f \cdot \si{s}$')
plt.xscale('log')
plt.legend()

plt.savefig('build/plot2.pdf')
#plt.show()
print('es funkt nichts')