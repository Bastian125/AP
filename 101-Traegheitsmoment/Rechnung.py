import numpy as np
import matplotlib.pyplot as plt

# D durch mitteln bestimmen
F, phi, r = np.genfromtxt('Messdaten_D.txt', unpack=True)

def D(F, phi, r):
    return (F*r)/(phi)

D = D(F, phi, r)
D_r = np.round(D, 6)
print('D: ', np.round(D_r, 6),' Mittelwert: ', np.round(np.mean(D_r), 6),' , Abweichung: ', np.round(np.std(D_r), 6))
