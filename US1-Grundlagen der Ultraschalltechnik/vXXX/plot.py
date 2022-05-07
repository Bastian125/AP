import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
 
#A#

h, A_in, t_in, A_aus, t_aus = np.genfromtxt('messwerte/Impuls-Echo/ImpulsEcho.txt', unpack=True)
t = t_aus - t_in
l = 2*h

def f(x, m, b):
    return m*x+b

params_Pb, cov_Pb = curve_fit(f, t, l)
m_Pb  = params_Pb[0]
b_Pb  = params_Pb[1]
Δm_Pb = np.sqrt(cov_Pb[0][0])
Δb_Pb = np.sqrt(cov_Pb[1][1])

print('c:')
print('{}+-{}'.format(m_Pb,Δm_Pb))
print('d:')
print('{}+-{}'.format(b_Pb,Δb_Pb))

x = np.linspace(0, 90, 2000)
plt.plot(x, (f(x, m_Pb, b_Pb)), 'k-', label='Ausgleichsfunktion')
plt.plot(t, l, 'rx', label='Messwerte')
plt.xlim(0, 90)
plt.ylim(0, 250)
plt.xlabel(r'$\mathrm{Laufzeit}\; t \; / \; \mu \mathrm{s}$')
plt.ylabel(r'$\mathrm{Länge}\; 2 \cdot l \; / \; \mathrm{mm}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("messwerte/ImpulsEcho.pdf")
#plt.show()
plt.close()