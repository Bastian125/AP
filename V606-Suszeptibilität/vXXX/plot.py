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

# Ermittlung der Suszeptibilitäten

# Konstanten der Spule / Schaltung

n = 250  # Windungen
A_s = 86.6*1e-6  # Fläche in m^2
l_s = 0.135  # Länge in m
R_s = 0.7  # Widerstand der Spule in Ohm
R_3 = 998  # Widerstand 3 in Ohm

##################################################
# Indexkonvention:
# d: Dy_2 O_3 (Dysprosium(3)oxid)
# g: Gd_2 O_3 (Gadolinium(3)oxid)
# c: N d_2 O_3 (Neodym(3)oxid)
#
# b: Brückenspannung
# 0: Vor der Messung
# 2: Nach der Justierung
##################################################

# Berechnung der realen Querschnitte

m_d = 14.38*1e-3
l_d = 0.152
rho_d = 7800
Q_d = m_d/(l_d*rho_d)     # effektiver Querschnitt der Probe in m^2

m_g = 10.2*1e-3
l_g = 0.151
rho_g = 7400
Q_g = m_g/(l_g*rho_g)

m_n = 7.66*1e-3
l_n = 0.155
rho_n = 7240
Q_n = m_n/(l_n*rho_n)         
print("Querschnittsflächen der Proben D,G,N ", Q_d, Q_g, Q_n)

# Messdaten

R_0d, R_2d, U_bd, U_0d, U_2d = np.genfromtxt("messwerte/Probe3.txt", unpack=True) * 10 **(-3)    # Widerstände noch mit 5 multiplizieren
R_0g, R_2g, U_bg, U_0g, U_2g = np.genfromtxt("messwerte/Probe2.txt", unpack=True) * 10 **(-3)
R_0n, R_2n, U_bn, U_0n, U_2n = np.genfromtxt("messwerte/Probe1.txt", unpack=True) * 10 **(-3)

R_0d = R_0d * 5
R_2d = R_2d * 5
R_0g = R_0g * 5
R_2g = R_2g * 5
R_0n = R_0n * 5
R_2n = R_2n * 5

# Funktionen zur Berechnung der Suszeptibilität

def chi_R(
    delta_R, Q
):  # delta_R: Differenz der Widerstände vor und nach Abgleich, Q: Querschnitt der Probe
    return 2 * A_s * delta_R / (R_3 * Q)

def chi_U(
    U_0, U_b, Q
):  # Über Spannungsmessung: U_0 Generatorspannung, U_b: Brückenspannung
    return 4 * A_s * U_b / (Q * U_0)


chi_Rd = chi_R(R_0d - R_2d, Q_d)
chi_Rg = chi_R(R_0g - R_2g, Q_g)
chi_Rn = chi_R(R_0n - R_2n, Q_n)

chi_Ud = chi_U(8.5, np.abs(U_bd - U_0d), Q_d)
chi_Ug = chi_U(8.5, np.abs(U_bg - U_0g), Q_g)
chi_Un = chi_U(8.5, np.abs(U_bn - U_0n), Q_n)

# d: Dy_2 O_3 (Dysprosium(3)oxid)
# g: Gd_2 O_3 (Gadolinium(3)oxid)
# n: N d_2 O_3 (Neodym(3)oxid)

# Mittelwerte (und Fehler): 
chi_Rdm = ufloat(np.mean(chi_Rd), np.std(chi_Rd))
chi_Rgm = ufloat(np.mean(chi_Rg), np.std(chi_Rg))
chi_Rnm = ufloat(np.mean(chi_Rn), np.std(chi_Rn))

chi_Udm = ufloat(np.mean(chi_Ud), np.std(chi_Ud))
chi_Ugm = ufloat(np.mean(chi_Ug), np.std(chi_Ug))
chi_Unm = ufloat(np.mean(chi_Un), np.std(chi_Un))

# Übersichtliche Ausgabe der Werte
print("------------------------------------------------")
print("Suszeptibilität aus Widerständen: (Dy, Gd, Nd)")
print(chi_Rd, chi_Rg, chi_Rn)
print(chi_Rdm, "\t\t   ", chi_Rgm, "\t\t   ",chi_Rnm)
print("------------------------------------------------")
print("Suszeptibilität aus Spannungen: (Dy, Gd, Nd)")
print(chi_Ud, chi_Ug, chi_Un)
print(chi_Udm, "\t\t   ", chi_Ugm, "\t\t   ", chi_Unm)
print("------------------------------------------------")


#theoretische Suszeptibilität
def g_j(J,S,L):
    return (3*J*(J+1) + S*(S+1) - L*(L+1))/(2*J*(J+1))

mu_b = (const.e*const.h)/(4*const.pi*const.m_e)

def N(rho,M):
    return (2*const.N_A*rho)/M
T = 293.15 #K == Raumtemperatur

def chi_theo(J,S,L,rho,M):
    return const.mu_0 * mu_b**2 * g_j(J,S,L)**2 * N(rho,M)*J*(J+1)/(3*const.k*T)

#Probe 1
chi_d = chi_theo(7.5, 2.5, 5, rho_d, 372.998*(10**-3))
print("------------------------------------------------")
print("Theoriewerte:")
print("magnetische Suszeptibilität von Dy ", chi_d)

#Probe 2
chi_g = chi_theo(3.5, 3.5, 0, rho_g, 362.4982*1e-3)
print("------------------------------------------------")
print("magnetische Suszeptibilität von Gd ", chi_g)
print("------------------------------------------------")

#Probe 3
chi_n = chi_theo(4.5, 1.5, 6, rho_n, 336.48*1e-3)
print("magnetische Suszeptibilität von n ", chi_n)

#Abweichungen

chi_abw1 = np.abs(unp.nominal_values(chi_Udm) - chi_d)/chi_d
chi_abw2 = np.abs(unp.nominal_values(chi_Ugm) - chi_g)/chi_g
chi_abw3 = np.abs(unp.nominal_values(chi_Unm) - chi_n)/chi_n

print("Abweichungen mit Spannung: ", chi_abw1*100, chi_abw2*100, chi_abw3*100)

chi_abw1 = np.abs(unp.nominal_values(chi_Rdm) - chi_d)/chi_d
chi_abw2 = np.abs(unp.nominal_values(chi_Rgm) - chi_g)/chi_g
chi_abw3 = np.abs(unp.nominal_values(chi_Rnm) - chi_n)/chi_n

print("Abweichungen mit Spannung: ", chi_abw1*100, chi_abw2*100, chi_abw3*100)

