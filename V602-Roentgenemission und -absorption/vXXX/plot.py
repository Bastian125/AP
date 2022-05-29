import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

# Rechnung
d = 201.4e-12
h = 6.626e-34
c = 2.998e8
e = 1.602e-19

def l(theta):
    return 2*d*np.sin(0.5*theta)

def E(theta):
    return (h*c)/(l(theta)*e)


# Ausgabe
print('Abweichung Bragg: ', (28.0/27.6 -1)*100)
print('lambda_alpha: ', l(22.4))
print('lambda_beta: ', l(20.2))
print('lambda_alpha_fwhm: ', l(0.5))
print('lambda_alpha_fwhm: ', l(0.45))
print('Ea: ', E(22.2))
print('Eb: ', E(20.2))
print('Efwhma: ', E(0.5))
print('Efwhmb: ', E(0.45))


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