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

# Energien
Ea = E(22.2)
Eb = E(20.2)
Efwhma = E(20.45)-E(19.9)
Efwhmb = E(22.75)-E(22.2)

# Absorptionskoeffizienten
sigma1 = z - np.sqrt(Ekabs/Ryd)
sigma2 = z - 2*np.sqrt((Ekabs - Ea)/Ryd)
sigma3 = z - 3*np.sqrt((Ekabs - Eb)/Ryd)

# Abschirmkonstanten

# Brom
a, I = np.genfromtxt('Messwerte/Absorptionsspektren/Brom.txt', unpack=True)

# Plot
plt.plot(a, I, 'x', label='Messwerte des Bromabsorbers')
plt.vlines(13.4, 0, 42, colors='r', label='Position der K-Kante')
plt.ylim(0, 42)
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('N/Imp/s')
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/brom.pdf')
plt.close()

# Gallium
a, I = np.genfromtxt('Messwerte/Absorptionsspektren/Gallium.txt', unpack=True)

# Plot
plt.plot(a, I, 'x', label='Messwerte des Galliumabsorbers')
plt.vlines(17.6, 0, 76, colors='r', label='Position der K-Kante')
plt.ylim(0, 76)
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('N/Imp/s')
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/gallium.pdf')
plt.close()

# Strontium
a, I = np.genfromtxt('Messwerte/Absorptionsspektren/Strontium.txt', unpack=True)

# Plot
plt.plot(a, I, 'x', label='Messwerte des Strontiumabsorbers')
plt.vlines(11.2, 0, 205, colors='r', label='Position der K-Kante')
plt.ylim(0, 205)
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('N/Imp/s')
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/strontium.pdf')
plt.close()

# Zink
a, I = np.genfromtxt('Messwerte/Absorptionsspektren/Zink.txt', unpack=True)

# Plot
plt.plot(a, I, 'x', label='Messwerte des Zinkabsorbers')
plt.vlines(18.6, 0, 120, colors='r', label='Position der K-Kante')
plt.ylim(0, 120)
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('N/Imp/s')
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zink.pdf')
plt.close()

# Zinkonium
a, I = np.genfromtxt('Messwerte/Absorptionsspektren/Zinkonium.txt', unpack=True)

# Plot
plt.plot(a, I, 'x', label='Messwerte des Zinkoniumabsorbers')
plt.vlines(10.1, 0, 290, colors='r', label='Position der K-Kante')
plt.ylim(0, 290)
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('N/Imp/s')
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zinkonium.pdf')
plt.close()

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