import matplotlib.pyplot as plt
import numpy as np

# Bragg-Bedingung
a, I = np.genfromtxt('Messwerte/Bragg/Bragg.txt', unpack=True)

plt.plot(a, I, 'x', label='Messwerte zur Bragg-Bedingung')
plt.plot(27.6, 281.0, 'ro', label='Maximum')
plt.xlabel(r'$2\theta\mathbin{^{\circ}}')
plt.ylabel('Imp/s')
plt.xlim(26, 30)
plt.legend()
plt.grid()


# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/bragg.pdf')
plt.close()

# Ausgabe
print('Abweichung Bragg: ', (28.0/27.6 -1)*100)#

# Emissionspektrum Cu-Röhre
a, I = np.genfromtxt('Messwerte/Emissionsspektrum/1.txt', unpack=True)


plt.plot(a, I, 'x', label='Messwerte für Kupfer')
plt.plot(20.2, 1437.0, 'ro', label=r'$K_{\symup{\beta}}$')
plt.plot(22.4, 4662.0, 'o', label=r'$K_{\symup{\alpha}}$')
plt.plot(10.0, 414.0, 'go', label='Bremsberg')
plt.xlim(4, 26)
plt.grid()
plt.legend()

# Speichern
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/cu.pdf')
plt.close()