import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp

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
    return (s/t)*10**(2)

v111 = v(t111)
v112 = v(t112)
v121 = v(t121)
v122 = v(t122)
v131 = v(t131)
v132 = v(t132)
v141 = v(t141)
v142 = v(t142)
v151 = v(t151)
v152 = v(t152)

v211 = v(t211)
v212 = v(t212)
v221 = v(t221)
v222 = v(t222)
v231 = v(t231)
v232 = v(t232)
v241 = v(t241)
v242 = v(t242)
v251 = v(t251)
v252 = v(t252)

v311 = v(t311)
v312 = v(t312)
v321 = v(t321)
v322 = v(t322)
v331 = v(t331)
v332 = v(t332)
v341 = v(t341)
v342 = v(t342)
v351 = v(t351)
v352 = v(t352)

v411 = v(t411)
v412 = v(t412)
v421 = v(t421)
v422 = v(t422)
v431 = v(t431)
v432 = v(t432)
v441 = v(t441)
v442 = v(t442)
v451 = v(t451)
v452 = v(t452)

v511 = v(t511)
v512 = v(t512)
v521 = v(t521)
v522 = v(t522)
v531 = v(t531)
v532 = v(t532)
v541 = v(t541)
v542 = v(t542)
v551 = v(t551)
v552 = v(t552)

print('v111: ', v111, ', v112: ', v112)
print('v121: ', v121, ', v122: ', v122)
print('v131: ', v131, ', v132: ', v132)
print('v141: ', v141, ', v142: ', v142)
print('v151: ', v151, ', v152: ', v152)

print('v211: ', v211, ', v212: ', v212)
print('v221: ', v221, ', v222: ', v222)
print('v231: ', v231, ', v232: ', v232)
print('v241: ', v241, ', v242: ', v242)
print('v251: ', v251, ', v252: ', v252)

print('v311: ', v311, ', v312: ', v312)
print('v321: ', v321, ', v322: ', v322)
print('v331: ', v331, ', v332: ', v332)
print('v341: ', v341, ', v342: ', v342)
print('v351: ', v351, ', v352: ', v352)

print('v411: ', v411, ', v412: ', v412)
print('v421: ', v421, ', v422: ', v422)
print('v431: ', v431, ', v432: ', v432)
print('v441: ', v441, ', v442: ', v442)
print('v451: ', v451, ', v452: ', v452)

print('v511: ', v511, ', v512: ', v512)
print('v521: ', v521, ', v522: ', v522)
print('v531: ', v531, ', v532: ', v532)
print('v541: ', v541, ', v542: ', v542)
print('v551: ', v551, ', v552: ', v552)

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
