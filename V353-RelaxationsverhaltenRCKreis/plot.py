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
plt.scatter(f,A, marker='+', color='gold', label='Messwerte')
plt.plot(f_plt, AC(f_plt, T), color='navy', label=rf'Ausgleichsfunktion',
        linewidth=0.4)

plt.title(r'Spannungsverhältnis $A(\omega) / U_0$ im RC-Kreis')
plt.ylabel(r'$A(\omega) / U_0$')
plt.xlabel(r'$f / \unit{\hertz}$')
plt.xscale('log')
plt.legend()

plt.savefig('build/plot2.pdf')
#plt.show()
plt.clf()

### 4c ###

# daten input, anpassung auf SI-Größen
f, A, U, a, b = np.genfromtxt('Mbc.txt', unpack=True)

# Spannung der Quelle
U0 = 1.6

# merge arrays
phi = a/b * 2 * np.pi

# neues dataframe fuer ausgabe
d = {'f': f, 'a': a, 'b':b, 'phi':phi}
df_new = pd.DataFrame(d)
print(df_new)

# curve fit
def phi_fit(f, T):
    omega = 2 * np.pi * f
    return np.arctan(-1 * omega * T)

p0 = [0.00089]
T, pcov = curve_fit(phi_fit, f, phi, p0=p0)
err = np.sqrt(np.diag(pcov))[0]
T = T[0]

# output
print(f'RC = ({-1*T * 10**6:.4f} ± {err * 10*6:.4f}) micro-seconds')

# plot
phi_plt = np.linspace(30, 10**5, 10**4)
plt.plot(phi_plt, phi_fit(phi_plt, T), color='navy', label=rf'Ausgleichsfunktion')
plt.scatter(f,phi, marker='+', color='gold', label='Messwerte')

plt.title(r'Phasenverschiebung zwischen $U_C$ und $U_G$')
plt.xlabel(r'$f / \unit{\hertz}$')
plt.ylabel(r'$\varphi /$ rad')
plt.legend()
#plt.xlim(0,10000)
plt.xscale('log')

plt.savefig('build/plot3.pdf')
plt.clf()

# phasenverschiebung.py
# daten input, anpassung auf SI-Größen

f, A, U, a, b = np.genfromtxt('Mbc.txt', unpack=True)
# Spannung der Quelle
U0 = 1.6

phi = a/b * 2 * np.pi

f_c = f
phi_c = phi

# curve fit
def phi_fit(f, T):
    omega = 2 * np.pi * f
    return np.arctan(-1 * omega * T)

p0 = [0.00089]
Tc, pcov = curve_fit(phi_fit, f, phi, p0=p0)
err = np.sqrt(np.diag(pcov))[0]
Tc = -1 * Tc[0] # RC nach berechnung von 4c

# output
T = Tc
print('Fit-Ergebnisse für Phasenverschiebung:')
print(f'RC = ({T * 10**6:.4f} ± {err * 10*6:.4f}) micro-seconds')

# amplitudenverhaeltnis
# daten input, anpassung auf SI-Größen

# Spannung der Quelle
U0 = 1.6

# anpassung auf spannungsverhaeltnis
A = A / 1.6

# curve fit
def AC(f, T):
    U0 = 1 # damit das Verhaeltnis dargestellt wird
    w = 2 * np.pi * f
    return 2.44 / (np.sqrt(1 + w**2 * T**2))

p0 = [0.0008]
om = 2 * np.pi * f
popt, pcov = curve_fit(AC, f, A, p0=p0)
U0 = 1.6
Tb = popt[0]
err = np.sqrt(np.diag(pcov))[0]

# output
T = Tb
print('Fit-Ergebnisse für Amplitudenverhaeltnis:')
print(f'RC = {10**6*T:.1f} ± {10**6*err:.2} micro-seconds')

# plotting
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

RC = Tc
# plot von messwerten
ax.scatter(phi_c, AC(f_c, RC), marker='+', 
        linewidth=1, color='r', label='Messwerte der Phasenverschiebung')
ax.scatter(phi_fit(-1 * f[0:7], RC), A[0:7], marker='x', color='navy',
        linewidth=0.8, label='Messwerte des Amplitudenverhältnis')

f = np.linspace(10**-2, 10**4, 10**5)
# plot fuer wert laut phase
plt.polar(phi_fit(-1 * f, RC), AC(f, RC), label='Ausgleichsfunktion für die Zeitkonstante aus 4c',
        linewidth=0.5, color='gold')

ax.set_thetamin(120)
ax.set_thetamax(-10)
ax.set_rlabel_position(0)
ax.grid(True)

plt.title('Polarplot')
plt.xticks([0, np.pi/8, np.pi/4,  3*np.pi/8, np.pi/2],
        [r"$0$", r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",  r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.legend()
plt.tight_layout()
plt.savefig('build/polarplot.pdf')

#""" polarplot.py end """
