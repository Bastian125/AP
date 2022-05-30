import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

# Rechnung
d = 201.4e-12
h = 6.626e-34
c = 2.998e8
e = 1.602e-19
Ekabs = 8.98e3
Ryd = 13.6
z = 29

def l(theta):
    return 2*d*np.sin(theta*np.pi/180)

def E(theta):
    return (h*c)/(l(theta)*e)

Ea = E(22.2)
Eb = E(20.2)
Efwhma = E(20.45)-E(19.9)
Efwhmb = E(22.75)-E(22.2)
sigma1 = z - np.sqrt(Ekabs/Ryd)
sigma2 = z - 2*np.sqrt((Ekabs - Ea)/Ryd)
sigma3 = z - 3*np.sqrt((Ekabs - Eb)/Ryd)

# Ausgabe
print('Abweichung Bragg: ', (28.0/27.6 -1)*100)
print('Ea: ', Ea)
print('Eb: ', Eb)
print('Efwhma: ', Efwhma)
print('Efwhmb: ', Efwhmb)
print('Aa: ', Ea/Efwhma)
print('Ab: ', Eb/Efwhmb)
print('sigma1: ', sigma1)
print('sigma2: ', sigma2)
print('sigma3: ', sigma3)


# Bragg-Bedingung
a, I = np.genfromtxt('Messwerte/Bragg/Bragg.txt', unpack=True)

plt.plot(a, I, 'x', label='Messwerte zur Bragg-Bedingung')
plt.plot(27.6, 281.0, 'ro', label='Maximum')
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('N/Imp/s')
plt.xlim(26, 30)
plt.legend()
plt.grid()


# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/bragg.pdf')
plt.close()

# Emissionspektrum Cu-Röhre
a, I = np.genfromtxt('Messwerte/Emissionsspektrum/1.txt', unpack=True)


plt.plot(a, I, 'x', label='Messwerte für Kupfer')
plt.plot(20.2, 1437.0, 'ro', label=r'$K_{\symup{\beta}}$')
plt.plot(22.4, 4662.0, 'o', label=r'$K_{\symup{\alpha}}$')
plt.plot(10.0, 414.0, 'go', label='Bremsberg')
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('N/Imp/s')
plt.xlim(4, 26)
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/cu.pdf')
plt.close()