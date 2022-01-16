import numpy as np

x = np.genfromtxt('messdaten/x.txt', unpack=True)

print('x: ', np.mean(x), ' +- ', np.std(x))

t, T7, T2, T1, T3, T4, T5, T6, T8 = np.genfromtxt('messdaten/statischeMethode.txt', encoding="UTF-16", unpack=True)

t, Mb, Ms, Alu, ES = np.genfromtxt('messdaten/tempdiff.txt', unpack=True)

