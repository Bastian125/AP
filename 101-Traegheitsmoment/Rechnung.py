import numpy as np
import matplotlib.pyplot as plt

# D durch mitteln bestimmen
F, phi, r = np.genfromtxt('Messdaten_D.txt', unpack=True)

def D(F, phi, r):
    return (F*r)/(phi)

D = D(F, phi, r)
D_r = np.round(D, 6)
print('D: ', np.round(D_r, 6),'\n Mittelwert: ', np.round(np.mean(D_r), 6),'\n Abweichung: ', np.round(np.std(D_r), 6))

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
