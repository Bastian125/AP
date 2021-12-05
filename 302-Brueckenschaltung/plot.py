import matplotlib.pyplot as plt
import numpy as np

f, U_Br, U_s, U_br = np.genfromtxt('Me).txt', unpack=True)
x = f/241
y = U_br/U_s

plt.plot(x, y, 'x', label='Messwerte')
plt.plot(x, (1)/(9) * ((x**2 -1)**2)/(((1-x**2)**2)+9*x**2), label='Theoriekurve')
plt.xlabel(r'$\Omega = \frac{f}{f_0}$')
plt.xscale('log')
plt.xlim(10**(-1), 10**(2.15))
plt.ylabel(r'$\frac{U_{Br}}{U_s}$')
plt.grid()
plt.legend(loc='best')


# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')