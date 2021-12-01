import matplotlib.pyplot as plt 
import numpy as np

# R14 bestimmen
R2, R3, R4, Rx = np.genfromtxt('Ma1).txt', unpack=True)
R14 = R2*R3/R4
print('R14: ', R14)

# R13 bestimmen
R2, R3, R4, Rx = np.genfromtxt('Ma2).txt', unpack=True)
R13 = R2*R3/R4
print('R13: ', R13)
