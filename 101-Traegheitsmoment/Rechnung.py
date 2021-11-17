import numpy as np
import matplotlib.pyplot as plt

# D durch mitteln bestimmen
F, phi, r = np.genfromtxt('Messdaten_D.txt', unpack=True)

def D(F, phi, r):
    return (F*r)/(phi)

D = D(F, phi, r)
print('D: ', np.round(D, 6),' Mittelwert: ', np.mean(D),' , Abweichung: ', np.std(D))
