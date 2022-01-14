import numpy as np

x = np.genfromtxt('messdaten/x.txt', unpack=True)

print('x: ', np.mean(x), ' +- ', np.std(x))