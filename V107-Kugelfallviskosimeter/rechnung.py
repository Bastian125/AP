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
