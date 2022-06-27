import matplotlib.pyplot as plt
import numpy as np

# Spannung korrigieren
# U_korr = U_gemessen + RI
# R := Innenwiderstand 1MOhm
# I := Strom Nanoamperemeter

# Konstanten

# Daten einlesen
U1, I1 = np.genfromtxt('messwerte/2a.txt', unpack=True)
U2, I2 = np.genfromtxt('messwerte/3a.txt', unpack=True)
U3, I3 = np.genfromtxt('messwerte/4a.txt', unpack=True)
U4, I4 = np.genfromtxt('messwerte/1a.txt', unpack=True)
U5, I5 = np.genfromtxt('messwerte/5a.txt', unpack=True)

# Funktionen
def saettigung(I1, I2, I3, I4, I5):
    print('I_Saettigung_1: ', np.amax(I1))
    print('I_Saettigung_2: ', np.amax(I2))
    print('I_Saettigung_3: ', np.amax(I3))
    print('I_Saettigung_4: ', np.amax(I4))
    print('I_Saettigung_5: ', np.amax(I5))
    return 0

# Plot 1
plt.plot(U1, I1, 'o', label=r'$I_{\symup{H}}=\SI{1,9}{\ampere}$')
plt.plot(U2, I2, 'o', label=r'$I_{\symup{H}}=\SI{2,0}{\ampere}$')
plt.xlabel(r'$U/\unit{\volt}$')
plt.ylabel(r'$I/\unit{\milli\ampere}$')
plt.grid()
plt.legend()

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
plt.close()

# Plot 2
plt.plot(U3, I3, 'o', label=r'$I_{\symup{H}}=\SI{2,1}{\ampere}$')
plt.plot(U4, I4, 'o', label=r'$I_{\symup{H}}=\SI{2,3}{\ampere}$')
plt.plot(U5, I5, 'o', label=r'$I_{\symup{H}}=\SI{2,5}{\ampere}$')
plt.xlabel(r'$U/\unit{\volt}$')
plt.ylabel(r'$I/\unit{\milli\ampere}$')
plt.grid()
plt.legend()

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.close()

# Ausgabe
#saettigung(I1, I2, I3, I4, I5)