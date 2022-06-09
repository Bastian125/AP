import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

# Konstanten
s = 0.005

# Geschwindikeiten
# Daten einlesen
t111, t112 = np.genfromtxt('messwerte/1/11.txt', unpack=True)
t121, t122 = np.genfromtxt('messwerte/1/12.txt', unpack=True)
t131, t132 = np.genfromtxt('messwerte/1/13.txt', unpack=True)
t141, t142 = np.genfromtxt('messwerte/1/14.txt', unpack=True)
t151, t152 = np.genfromtxt('messwerte/1/15.txt', unpack=True)

t211, t212 = np.genfromtxt('messwerte/2/21.txt', unpack=True)
t221, t222 = np.genfromtxt('messwerte/2/22.txt', unpack=True)
t231, t232 = np.genfromtxt('messwerte/2/23.txt', unpack=True)
t241, t242 = np.genfromtxt('messwerte/2/24.txt', unpack=True)
t251, t252 = np.genfromtxt('messwerte/2/25.txt', unpack=True)

t311, t312 = np.genfromtxt('messwerte/3/31.txt', unpack=True)
t321, t322 = np.genfromtxt('messwerte/3/32.txt', unpack=True)
t331, t332 = np.genfromtxt('messwerte/3/33.txt', unpack=True)
t341, t342 = np.genfromtxt('messwerte/3/34.txt', unpack=True)
t351, t352 = np.genfromtxt('messwerte/3/35.txt', unpack=True)

t411, t412 = np.genfromtxt('messwerte/4/41.txt', unpack=True)
t421, t422 = np.genfromtxt('messwerte/4/42.txt', unpack=True)
t431, t432 = np.genfromtxt('messwerte/4/43.txt', unpack=True)
t441, t442 = np.genfromtxt('messwerte/4/44.txt', unpack=True)
t451, t452 = np.genfromtxt('messwerte/4/45.txt', unpack=True)

t511, t512 = np.genfromtxt('messwerte/5/51.txt', unpack=True)
t521, t522 = np.genfromtxt('messwerte/5/52.txt', unpack=True)
t531, t532 = np.genfromtxt('messwerte/5/53.txt', unpack=True)
t541, t542 = np.genfromtxt('messwerte/5/54.txt', unpack=True)
t551, t552 = np.genfromtxt('messwerte/5/55.txt', unpack=True)

def v(t):
    t = ufloat(np.mean(t), np.std(t))
    return s/t

v111 = v(t111)
v112 = v(t112)

x=1
y=2
plt.plot(1, 2, 1)
plt.plot(x, y, label='Kurve')
plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
