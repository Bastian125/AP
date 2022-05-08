
import matplotlib.pyplot as plt
import numpy as np

import uncertainties as unp
from scipy import stats
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as const
#IMPULS-ECHO#

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

print('c1:')
print('{}+-{}'.format(m_Pb,Δm_Pb))
print('d1:')
print('{}+-{}'.format(b_Pb,Δb_Pb))

x = np.linspace(0, 90, 2000)
plt.plot(x, (f(x, m_Pb, b_Pb)), 'k-', label='Ausgleichsfunktion')
plt.plot(t, l, 'rx', label='Messwerte')
plt.xlim(0, 90)
plt.ylim(0, 250)
plt.xlabel(r'$\mathrm{Laufzeit}\; t \; / \; \mu \mathrm{s}$')
plt.ylabel(r'$\mathrm{Länge}\; 2 \cdot l \; / \; \mathrm{mm}$')
plt.grid(which="both")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("messwerte/ImpulsEcho.pdf")
#plt.show()
plt.close()

#DURCHSCHALLUNG#

h2, tin2 , taus2 = np.genfromtxt('messwerte/Durchschallung/Durchschallung.txt', unpack=True)
t2 = taus2 - tin2
def g(x, m, b):
    return m*x+b

params_2, cov_2 = curve_fit(g, t2, h2)
m_2  = params_2[0]
b_2  = params_2[1]
Δm_2 = np.sqrt(cov_2[0][0])
Δb_2 = np.sqrt(cov_2[1][1])

print('c2:')
print('{}+-{}'.format(m_2,Δm_2))
print('d2:')
print('{}+-{}'.format(b_2,Δb_2))

y = np.linspace(0, 90, 2000)
plt.plot(y, (g(y, m_2, b_2)), 'k-', label='Ausgleichsfunktion')
plt.plot(t2, h2, 'rx', label='Messwerte')
plt.xlim(0, 90)
plt.ylim(0, 250)
plt.xlabel(r'$\mathrm{Laufzeit}\; t \; / \; \mu \mathrm{s}$')
plt.ylabel(r'$\mathrm{Länge}\; l \; / \; \mathrm{mm}$')
plt.grid(which="both")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("messwerte/Durchschallung.pdf")
#plt.show()
plt.close()

#DÄMPFUNG#

A = A_in / A_aus
l_ = l * 10**(-3)


print(f'A: {A}')
plt.plot(l_[-1],np.log(A[-1]), color='dimgray', marker='x')
plt.plot(l_[-2],np.log(A[-2]), color='dimgray', marker='x')
l_ = np.delete(l_, [4])
A = np.delete(A, [4])
print(l)

m , b , r ,p ,std =stats.linregress(l_,np.log(A))
M=unp.uarray(m,std)
B=unp.uarray(b,std)

print(f'm2: {M}')
print(f'c2: {1/M}')
print(f'b2: {B}')

xx = np.linspace(0,0.25, 1000)
plt.plot(xx,m*xx+b, 'k-', label='Ausgleichsfunktion')
plt.plot(l_,np.log(A),'rx',label='Messwerte') 


plt.xlabel(r'Länge $2 \cdot l \; / \; \mathrm{m}$')
plt.ylabel(r'$\log{\, \frac{U}{U_0}}$')
plt.legend(loc='best')
plt.grid(which="both")

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('messwerte/Daempfung.pdf')
plt.close()

#Auge#
t_4, a = np.genfromtxt('messwerte/Auge/auge.txt', unpack = True)
t4 = t_4 / 2 * 10**-6
print(f't4: {t4}')
c_1 = 1483
c_2 = 2500
c_3 = 1410

def d(t,c,c_old):
    return (c*t*10**2 - c_old)  #output in cm

d1 = d(t4[0],c_1,0)
d2 = d(t4[1],c_1,d1)
d3 = d(t4[2],c_2,d1+d2)
d4 = d(t4[3],c_3,d1+d2+d3)
print(f'd1: {d1}')
print(f'd2: {d2}')
print(f'd3: {d3}')
print(f'd4: {d4}')