import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const

# Bestimmung der Filterkurve

f, U = np.genfromtxt("messwerte/a.txt", unpack=True)

U = U/8.5

def Gauss(x, b, a):
    return np.exp(-(x-b)**2*a)

params, pcov = op.curve_fit(Gauss, f, U, p0 = [22.10, 1])            
err = np.sqrt(np.diag(pcov))

b = ufloat(params[0], err[0])
a = ufloat(params[1], err[1])

print("Parameter des Fits: ", a, "\t", b)


#plt.axvline(21.6, ymin=0, ymax=0.8333, color="forestgreen", linestyle="dotted")
plt.axhline(1/np.sqrt(2), color="gray", linestyle="dotted", label = r"$1 / \sqrt{2}$")
plt.plot(22.10, 1, marker=".", markeredgecolor="red", markersize=8, linewidth=0, label="Maximale Spannung")

x = np.linspace(10, 31, 10000)

plt.plot(x, Gauss(x, *params), color = "blue", label = "Glockenkurven Fit")
plt.plot(20.9736, 1/np.sqrt(2), marker = ".", markersize = 8, color = "green", markeredgecolor = "k", markeredgewidth = 0.65, linewidth=0, label = r"$\nu_{-} / \nu_{+}$")
plt.plot(22.6064, 1/np.sqrt(2), marker = ".", markersize = 8, color = "green", markeredgecolor = "k", markeredgewidth = 0.65, linewidth=0)
plt.plot(f, U, color="black", marker="x", label="Messwerte", linewidth=0)

#plt.text(22, 8.5, r"$\qty{8.5}{\volt}$")
plt.xlabel(r'$f$ / kHz')
#plt.yticks(ticks = [0, 0.2, 0.4, 0.6, 1/np.sqrt(2), 0.8, 1], labels = [0, 0.2, 0.4, 0.6, r"$\frac{1}{\sqrt{2}}$", 0.8, 1])
plt.ylabel(r'$U / U_\mathrm{max}$')
plt.ylim(0, 1.2)
plt.legend()
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.savefig("build/plot.pdf")
#plt.show()
plt.close()

G = b/(22.60-20.97)
print("------------------------------------------------")
print("nu_-: ", 20.97)
print("nu_0: ", b)
print("nu_+: ", 22.60)
print("Güte der Glockenkurve: ", G)
print("------------------------------------------------")

