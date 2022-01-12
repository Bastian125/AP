import matplotlib.pyplot as plt
import numpy as np

# T1 und T4 Plotten
t, T7, T2, T1, T3, T4, T5, T6, T8 = np.genfromtxt('messdaten/statischeMethode.txt', encoding="UTF-16"  , unpack=True)
x = 5*t
y1 = T1 
y2 = T4

plt.figure()
plt.plot(x, y1, '.', label=r'$T_{1}$')
plt.plot(x, y2, '.', label=r'$T_{4}$')
plt.grid()
plt.xlim(0, 730)
plt.ylim(15, 50)
plt.xlabel(r'$t\,\mathbin{/}\,\si{\second}$')
plt.ylabel(r'$\theta\,\mathbin{/}\,\si{\celsius}$')
plt.legend(loc='best')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/T1_T4.pdf')

# T5 und T8 plotten
y1 = T5
y2 = T8

plt.figure()
plt.plot(x, y1, '.', label=r'$T_{5}$')
plt.plot(x, y2, '.', label=r'$T_{8}$')
plt.grid()
plt.xlim(0, 730)
plt.ylim(15, 50)
plt.xlabel(r'$t\,\mathbin{/}\,\si{\second}$')
plt.ylabel(r'$\theta\,\mathbin{/}\,\si{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/T5_T8.pdf')

# T7 - T8, T2- T1
y1 = T7- T8
y2 = T2- T1

plt.figure()
plt.plot(x, y1, '.', label=r'$T_{\symup{St}}$')
plt.plot(x, y2, '.', label=r'$T_{\symup{St}}$')
plt.grid()
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Tempdiff.pdf')
