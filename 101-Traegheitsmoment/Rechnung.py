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
T_Zyl = np.genfromtxt('Messdaten_Zylinder.txt', unpack=True)
print('\n T_Zyl: ', T_Zyl, '\n Mittelwert: ', np.round(np.mean(T_Zyl), 2), '\n Abweichung: ', np.round(np.std(T_Zyl), 2))
