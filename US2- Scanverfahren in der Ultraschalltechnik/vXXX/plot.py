import matplotlib.pyplot as plt
import numpy as np

# Bestimmung der Schallgeschwindigkeit in Acryl mit dem A-Scan
t_A_micro = np.array([41.6, 40.5, 34.9, 29.4, 24.1, 18.2, 12.0])
t_A = (t_A_micro - 1.6/2) * 10**(-6)
s_A_cm = np.array([1.945, 2.385, 3.220, 3.980, 4.880, 5.595, 6.390])
s_A = 2*(8.025 - s_A_cm) * 10**(-2)

# Lineare Regression
params, covariance_matrix = np.polyfit(t_A, s_A, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
x_plot = np.linspace(0, 45)

plt.plot( t_A*10**(6), s_A*10**(2), 'x', label='Messwerte der Laufzeiten')
plt.plot(x_plot*10**(6),
        (params[0] * x_plot + params[1])*10**(2),
        label='Lineare Regression',
        linewidth=3)
plt.xlabel(r'$t/\unit{\micro\second}$')
plt.ylabel(r'$s/\unit{\centi\meter}$')
plt.xlim(0, 45)
plt.ylim(0, 13)
plt.legend()
plt.grid()

# Output
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
plt.close()

# Abstände und Dicken der Störstellen
t_unten = np.array([14.1, 15.3, 49.9, 40.5, 34.9, 29.4, 24.1, 18.2, 12.0, 6.2, 41.6])
t_u = (t_unten - 1.6)*10**(-6)
t_oben = np.array([48.8, 44.6, 10.8, 17.2, 23.3, 29.5, 35.4, 41.1, 46.9, 53.0, 12.6])
t_o = (t_oben - 1.6)*10**(-6)
c_Acryl = 2730
h = 8.025e-2

s_u = 0.5 * c_Acryl * t_u
s_o = 0.5 * c_Acryl * t_o
d = h- s_u - s_o

print('Abstand zur Stoerstelle unten: ', np.round(s_u*10**2, 3))
print('Abstand zur Stoerstelle oben: ', np.round(s_o*10**2, 3))
print('Dicke: ', d)