import matplotlib.pyplot as plt
import numpy as np

t, T7, T2, T1, T3, T4, T5, T6, T8 = np.genfromtxt('messdaten/statischeMethode.txt', encoding="UTF-16"  , unpack=True)
x = 5*t
y1 = T1 
y2 = T4

plt.plot(x, y1, label='Kurve')
plt.plot(x, y2, label='Kurve')
plt.xlabel(r'$t\,\mathbin{/}\,\si{\second}$')
plt.ylabel(r'$\theta\,\mathbin{/}\,\si{\celsius}$')
plt.legend(loc='best')



# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
