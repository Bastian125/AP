import numpy as np
import matplotlib.pyplot as plt

# D durch mitteln bestimmen
F, phi, r = np.genfromtxt('Messdaten_D.txt', unpack=True)

def D(F, phi, r):
    return (F*r)/(phi)

D = D(F, phi, r)
D_r = np.round(D, 6)
print('D: ', np.round(D_r, 6),'\n Mittelwert: ', np.round(np.mean(D_r), 6),'\n Abweichung: ', np.round(np.std(D_r), 6))

# Schwingungsdauern
# T_Zyl durch mitteln bestimmen
Z_Zyl = np.genfromtxt('Messdaten_Zylinder.txt', unpack=True)
T_Zyl = np.round(Z_Zyl/5, 2)
print('\n T_Zyl: ', T_Zyl, '\n Mittelwert: ', np.round(np.mean(T_Zyl), 2), '\n Abweichung: ', np.round(np.std(T_Zyl), 2))

# T_Kugel durch mitteln bestimmen
Z_Kugel = np.genfromtxt('Messdaten_Kugel.txt', unpack=True)
T_Kugel = np.round(Z_Kugel/3, 2)
print('\n T_Kugel: ', T_Kugel, '\n Mittelwert: ', np.round(np.mean(T_Kugel), 2), '\n Abweichung: ', np.round(np.std(T_Kugel), 2))

# T_Koerper1
Z_K1 = np.genfromtxt('Messdaten_Koerper1.txt', unpack=True)
T_K1 = np.round(Z_K1/3, 2)
print('\n T_K1: ', T_K1, '\n Mittelwert: ', np.round(np.mean(T_K1), 2), '\n Abweichung: ', np.round(np.std(T_K1), 2))

# T_Koerper2
Z_K2 = np.genfromtxt('Messdaten_Koerper2.txt', unpack=True)
T_K2 = np.round(Z_K2/3, 2)
print('\n T_K2: ', T_K2, '\n Mittelwert: ', np.round(np.mean(T_K2), 2), '\n Abweichung: ', np.round(np.std(T_K2), 2))

# Maße des Koerpers
# Maße Kopf
r_K = np.genfromtxt('r_kopf.txt', unpack=True)
r_k = np.round(r_K, 4)
print('\n r_k: ', r_k, '\n Mittelwert: ', np.round(np.mean(r_k), 4), '\n Abweichung: ', np.round(np.std(r_k), 4))

# Maße Oberkoerper
r_O = np.genfromtxt('r_ober.txt', unpack=True)
r_o = np.round(r_O, 4)
print('\n r_o: ', r_o, '\n Mittelwert: ', np.round(np.mean(r_o), 4), '\n Abweichung: ', np.round(np.std(r_o), 4))

# Maße Arme
r_A = np.genfromtxt('r_arme.txt', unpack=True)
r_a = np.round(r_A, 4)
print('\n r_a: ', r_a, '\n Mittelwert: ', np.round(np.mean(r_a), 4), '\n Abweichung: ', np.round(np.std(r_a), 4))

# Maße Beine
r_B = np.genfromtxt('r_beine.txt', unpack=True)
r_b = np.round(r_B, 4)
print('\n r_b: ', r_b, '\n Mittelwert: ', np.round(np.mean(r_b), 4), '\n Abweichung: ', np.round(np.std(r_b), 4))