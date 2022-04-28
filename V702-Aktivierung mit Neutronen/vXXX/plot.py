import matplotlib.pyplot as plt
import numpy as np

t_in, N_in = np.genfromtxt('messwerte/vanadium.txt', unpack=True)
t = 30*t_in
N = N_in - 9

plt.semilogy(t, N, 'x', label='Messwerte')
plt.xlabel(r'$t/\unit{\second}$')
plt.ylabel(r'$N$')
plt.xlim(0, 950)
plt.grid()
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
plt.close()