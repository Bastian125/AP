import numpy as np
import matplotlib.pyplot as plt

# D durch mitteln bestimmen
F, phi, r = np.genfromtxt('Messdaten_D.txt', unpack=True)

def D(F, phi, r):
    return (F*r)/(phi)

D = D(F, phi, r)
print('Mittelwert: ', np.mean(D),' , Abweichung: ', np.std(D))

# I_d durch Lineare Regression bestimmen
T, a = np.genfromtxt('Messdaten_I_d.txt', unpack=True)