import matplotlib.pyplot as plt 
import numpy as np

# a)
# R14 bestimmen
R2, R3, R4, Rx = np.genfromtxt('Ma1).txt', unpack=True)
R14 = R2*R3/R4
print('R14: ', np.mean(R14))

# R13 bestimmen
R2, R3, R4, Rt = np.genfromtxt('Ma2).txt', unpack=True)
R13 = R2*R3/R4
print('R13: ', np.mean(R13))

# b)
# Cx und Rx
C2 = 597*10**(-9)
R2, R3, R4, Ct, Rt1 = np.genfromtxt('Mb).txt', unpack=True)
Cx = C2*R4/R3
Rx = R2*R3/R4
print('Cx: ', np.mean(Cx))
print('Rx: ', np.mean(Rx))

