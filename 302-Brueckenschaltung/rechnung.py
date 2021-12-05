import matplotlib.pyplot as plt 
import numpy as np

# a)
# R14 bestimmen
R2, R3, R4, Rx = np.genfromtxt('Ma1).txt', unpack=True)
R14 = R2*R3/R4
print('R14: ', np.mean(R14), '+- ', np.std(R14))

# R13 bestimmen
R2, R3, R4, Rt = np.genfromtxt('Ma2).txt', unpack=True)
R13 = R2*R3/R4
print('R13: ', np.mean(R13), '+- ', np.std(R13))

# b)
# C8 und R8
C2 = 597e-09
R2, R3, R4, Ct, Rt1 = np.genfromtxt('Mb).txt', unpack=True)
C8 = C2*R4/R3
R8 = R2*R3/R4
print('C8: ', np.mean(C8), '+- ', np.std(C8))
print('R8: ', np.mean(R8), '+- ', np.std(R8))

# c)
# R16 und L16
L2 = 14.6e-3
R2, R3, R4, Rt2, Lt = np.genfromtxt('Mc).txt', unpack=True)
R16 = R2*R3/R4
L16 = L2*R3/R4
print('R16: ', np.mean(R16), '+- ', np.std(R16))
print('L16: ', np.mean(L16), '+- ', np.std(L16))

# d)
# R16 und L16
R2 = 1e3
R3, R4, Rt2, Lt = np.genfromtxt('Md).txt', unpack=True)
R16 = R2*R3/R4
L16 = R2*R3*C2
print('R16: ', np.mean(R16), '+- ', np.std(R16))
print('L16: ', np.mean(L16), '+- ', np.std(L16))