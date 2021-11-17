import matplotlib.pyplot as plt
import numpy as np

T, a = np.genfromtxt('Messdaten_I_d.txt', unpack=True)

plt.plot(a**2, T**2, 'x')
plt.xlabel(r'$a / \mathrm{m^2}$')
plt.ylabel(r'$T / \mathrm{s^2}$')
plt.xlim(0)
plt.ylim(0)
plt.grid()

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
