import matplotlib.pyplot as plt
import numpy as np

# T1 und T4 Plotten
t, T7, T2, T1, T3, T4, T5, T6, T8 = np.genfromtxt('messdaten/statischeMethode.txt', encoding="UTF-16"  , unpack=True)
x = 5*t
y1 = T1 
y2 = T4
y3 = T5
y4 = T8

plt.figure()
plt.plot(x, y1, label=r'$T_{1}: \symup{Messing (breit)}$')
plt.plot(x, y2, label=r'$T_{4}: \symup{Messing (schmal)}$')
plt.plot(x, y3, label=r'$T_{5}: \symup{Aluminium}$')
plt.plot(x, y4, label=r'$T_{8}: \symup{Edelstahl}$')
plt.grid()
plt.xlim(0, 730)
plt.ylim(15, 50)
plt.xlabel(r'$t\,\mathbin{/}\,\si{\second}$')
plt.ylabel(r'$\theta\,\mathbin{/}\,\si{\celsius}$')
plt.legend(loc='best')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')


# T7 - T8, T2- T1
y1 = T7- T8
y2 = T2- T1

plt.figure()
plt.plot(x, y1, label=r'$\symup{\Delta}T_{\symup{Messing}}$')
plt.plot(x, y2, label=r'$\symup{\Delta}T_{\symup{Edelstahl}}$')
plt.grid()
plt.xlim(0, 730)
plt.ylim(-2, 13)
plt.xlabel(r'$t\,\mathbin{/}\,\si{\second}$')
plt.ylabel(r'$\theta\,\mathbin{/}\,\si{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Tempdiff.pdf')

# T1-T2 dynamisch
t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('messdaten/dynamischeMethode1.txt', encoding="UTF-16", unpack=True)

x = t*2
y1 = T1
y2 = T2

plt.figure()
plt.plot(x, y1, label=r'$T_{1}$')
plt.plot(x, y2, label=r'$T_{2}$')
plt.grid()
plt.xlim(0, 810)
plt.ylim(25, 80)
plt.xlabel(r'$t\,\mathbin{/}\,\si{\second}$')
plt.ylabel(r'$\theta\,\mathbin{/}\,\si{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/80sMess.pdf')

# T5-T6 dynamisch
y1 = T5
y2 = T6

plt.figure()
plt.plot(x, y1, label=r'$T_{5}$')
plt.plot(x, y2, label=r'$T_{6}$')
plt.grid()
plt.xlim(0, 810)
plt.ylim(25, 80)
plt.xlabel(r'$t\,\mathbin{/}\,\si{\second}$')
plt.ylabel(r'$\theta\,\mathbin{/}\,\si{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/80sAlu.pdf')

# T7-T8 dynamisch
t, T6, T2, T1, T3, T4, T5, T7, T8 = np.genfromtxt('messdaten/dynamischeMethode2.txt', encoding="UTF-16", unpack=True)

x = t*2
y1 = T7
y2 = T8

plt.figure()
plt.plot(x, y1, label=r'$T_{7}$')
plt.plot(x, y2, label=r'$T_{8}$')
plt.grid()
plt.xlim(0, 810)
plt.ylim(25, 75)
plt.xlabel(r'$t\,\mathbin{/}\,\si{\second}$')
plt.ylabel(r'$\theta\,\mathbin{/}\,\si{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/200sEdelstahl.pdf')