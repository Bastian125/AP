import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

# Rechnung
d = 201.4e-12
h = 6.626e-34
heV = 4.135e-15
c = 2.998e8
e = 1.602e-19
Ekabs = 8.98e3
Ryd = 13.6
z = 29
a = 7.297e-3

def l(theta):
    return 2*d*np.sin(theta*np.pi/180)

def E(theta):
    return (h*c)/(l(theta)*e)

def s(Z, E):
    w = np.sqrt(E/Ryd -a**2 * Z**4 /4)
    return Z-w

print('Rydbergenergie: ', ufloat(0.300, 0.011)**2)
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
# Energie
E_Br = E(13.4)
E_Ga = E(17.6)
E_Sr = E(11.2)
E_Zn = E(18.6)
E_Zr = E(10.1)

print('E_Br: ',E_Br)
print('E_Ga: ',E_Ga)
print('E_Sr: ',E_Sr)
print('E_Zn: ',E_Zn)
print('E_Zr: ',E_Zr)
print('sig_Br: ', s(35, E_Br))
print('sig_Ga: ', s(31, E_Ga))
print('sig_Sr: ', s(38, E_Sr))
print('sig_Zn: ', s(30, E_Zn))
print('sig_Zr: ', s(40, E_Zr))

# Absorptionskoeffizienten


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

# Zirkonium
a, I = np.genfromtxt('Messwerte/Absorptionsspektren/Zirkonium.txt', unpack=True)

# Plot
plt.plot(a, I, 'x', label='Messwerte des Zirkoniumabsorbers')
plt.vlines(10.1, 0, 290, colors='r', label='Position der K-Kante')
plt.ylim(0, 290)
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('N/Imp/s')
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zirkonium.pdf')
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

#Rydberg
E = [13283, 10811, 15849, 9651, 17554]
e = np.sqrt(E)
Z = [35, 31, 38, 30, 40]

# Lineare Regression
params, covariance_matrix = np.polyfit(e, Z, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')



x_plot = np.linspace(8000, 18000)

plt.plot(E, Z, 'x', label='Errechnete Punkte')
x_plot = np.linspace(9000, 18000)
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlim(9000, 18000)
plt.ylim(29, 41)
plt.xlabel(r'$\sqrt(E)/\sqrt(\unit{\eV})$')
plt.ylabel(r'$Z$')
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/rydberg.pdf')
plt.close()