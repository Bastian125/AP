import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

# Dichte der Kugeln
r_gr, m_gr, r_kl, m_kl = np.genfromtxt('MasseundDichte.txt', unpack=True)

r_G = ufloat(np.round(np.mean(r_gr), 5), np.round(np.std(r_gr), 5))
m_G = ufloat(np.round(np.mean(m_gr), 5), np.round(np.std(m_gr), 5))
d_G = (m_G)/((4/3)*np.pi*r_G**3)

r_K = ufloat(np.round(np.mean(r_kl), 5), np.round(np.std(r_kl), 5))
m_K = ufloat(np.round(np.mean(m_kl), 5), np.round(np.std(m_kl), 5))
d_K = (m_K)/((4/3)*np.pi*r_K**3)

print("Große Kugel:")
print("r: ", np.round(np.mean(r_gr), 5), " +- ", np.round(np.std(r_gr), 5))
print("m: ", np.round(np.mean(m_gr), 5), " +- ", np.round(np.std(m_gr), 5))
print("d: ", d_G)

print("Kleine Kugel:")
print("r: ", np.round(np.mean(r_kl), 5), " +- ", np.round(np.std(r_kl), 5))
print("m: ", np.round(np.mean(m_kl), 5), " +- ", np.round(np.std(m_kl), 5))
print("d: ", d_K)

# Fallzeiten
# Große Kugel
T_gr = np.genfromtxt('FallzeitGr.txt', unpack=True)
print("Große Kugel: ")
print("t: ", np.round(np.mean(T_gr), 2), " +- ", np.round(np.std(T_gr), 2))

# Kleine Kugel
T_kl = np.genfromtxt('FallzeitKl.txt', unpack=True)
print("Kleine Kugel: ")
print("t: ", np.round(np.mean(T_kl), 2), " +- ", np.round(np.std(T_kl), 2))

# Viskosität bei Raumtemperatur
rho_k = ufloat(2380, 10)
t = ufloat(12.04, 0.18)
v_rt = (7.64e-8)*(rho_k - 998.2)*t
print("Viskosität bei Raumtemperatur: ", v_rt)

# Apparatenkonstante der großen Kugel
rho_g = ufloat(2232, 34)
eta_rt = ufloat(1.27e-3, 0.02e-3)
t_g = ufloat(39.7, 0.39)
K = (eta_rt)/((rho_g-998.2)*t_g)
print("Apparatenkonstante Große Kugel: ", K)

# Viskosität Temperaturabhängig
T, t, rhoT, etaT= np.genfromtxt('temperatur.txt', unpack=True)
rhoK = ufloat(2232, 34)
eta_T = K*(rhoK-rhoT)*t*10**3
print("Viskosität in Temperaturabhängigkeit: ")
print(eta_T)

# A bestimmen
a = ufloat(-13.132, 0.230)
A = np.e**(a)
print("A: ", A)

# Reynoldszahl
rhofl = 998.2
eta = ufloat(1.27e-3, 0.02e-3)
x = 0.05
r = ufloat(7.64e-3, 0.11e-3)
t = ufloat(12.04, 0.18) 
Re = (rhofl*x*2*r)/(eta*t)
print("Re: ", Re)