import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

################################################################################
##TEIL 1 Absorptionskoeffizient und N_0 der Gammastrahlung für Blei und Eisen ##
################################################################################
Nulleffekt = 567/900 
print('Nulleffekt',Nulleffekt)
######BLEI

# Werte einlesen
d_Pb, t_Pb, counts_Pb = np.genfromtxt('Messwerte/gamma-strahler(Blei).txt').T

d_Pb *= 1e-3

# Auswertung

ln_Pb = np.log(counts_Pb/t_Pb-Nulleffekt)

def f(x, m, b):
    return m*x+b
    
params_Pb, cov_Pb = curve_fit(f, d_Pb, ln_Pb)
m_Pb  = params_Pb[0]
b_Pb  = params_Pb[1]
Δm_Pb = np.sqrt(cov_Pb[0][0])
Δb_Pb = np.sqrt(cov_Pb[1][1])
print('counts_Pb/t_Pb-Nulleffekt',counts_Pb/t_Pb-Nulleffekt)
print('ln_Pb',ln_Pb)
print('Geradensteigung Blei:')
print('{}+-{}'.format(m_Pb,Δm_Pb))
print('y-Achsenabschnit Blei:')
print('{}+-{}'.format(b_Pb,Δb_Pb))

x = np.linspace(0, 0.025, 2000)
plt.errorbar(d_Pb*1e3, (counts_Pb/t_Pb-Nulleffekt), np.sqrt(counts_Pb/t_Pb-Nulleffekt), fmt='gx', label='Messwerte')
plt.plot(x*1e3, np.exp(f(x, m_Pb, b_Pb)), 'k-', label='Ausgleichsfunktion')
plt.yscale('log')
plt.xlim(0, 22)
plt.ylim(10, 170)
plt.xlabel(r'$\mathrm{Dicke}\; d/\mathrm{mm}$')
plt.ylabel(r'$\mathrm{Impulsrate}\; N-N_{\mathrm{u}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("Bilder/Blei.pdf")
#plt.show()
plt.close()

#EISEN

# Werte einlesen 
d_Fe, t_Fe, counts_Fe = np.genfromtxt('Messwerte/gamma-strahler(Eisen).txt').T


# Auswertung
ln_Fe = np.log(counts_Fe/t_Fe-Nulleffekt)

def f(x, m, b):
    return m*x+b
    
params_Fe, cov_Fe = curve_fit(f, d_Fe, ln_Fe)
m_Fe  = params_Fe[0]
b_Fe  = params_Fe[1]
Δm_Fe = np.sqrt(cov_Fe[0][0])
Δb_Fe = np.sqrt(cov_Fe[1][1])

print('counts_Fe/t_Fe-Nulleffekt',counts_Fe/t_Fe-Nulleffekt)
print('ln_Fe',ln_Fe)

print('Geradensteigung Eisen:')
print('{}+-{}'.format(m_Fe,Δm_Fe))
print('y-Achsenabschnit Eisen:')
print('{}+-{}'.format(b_Fe,Δb_Fe))

x = np.linspace(0, 0.025, 2000)
plt.errorbar(d_Fe*1e3, (counts_Fe/t_Fe-Nulleffekt), np.sqrt(counts_Fe/t_Fe-Nulleffekt), fmt='gx', label='Messwerte')
plt.plot(x*1e3, np.exp(f(x, m_Fe, b_Fe)), 'k-', label='Ausgleichsfunktion')
plt.yscale('log')
plt.xlim(0, 22)
plt.ylim(50, 150)
plt.xlabel(r'$\mathrm{Dicke}\; d/\mathrm{mm}$')
plt.ylabel(r'$\mathrm{Impulsrate}\; N-N_{\mathrm{u}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("Bilder/Eisen.pdf")
#plt.show()
plt.close()



############################################
##TEIL 2 Maximalenergie vom beta-Strahler ##
############################################
Nulleffekt = 567/900 
print(Nulleffekt)
d_A, Δd_A, t_A, N_A = np.loadtxt('Messwerte/beta-strahler.txt', unpack = True)

ln_A = np.log(N_A/t_A-Nulleffekt)
print(ln_A)
def f(x, m, b):
    return m*x+b
    
params_A1, cov_A1 = curve_fit(f, d_A[0:5], ln_A[0:5])
m_A1  = params_A1[0]
b_A1  = params_A1[1]
Δm_A1 = np.sqrt(cov_A1[0][0])
Δb_A1 = np.sqrt(cov_A1[1][1])

def g(x, b):
    return b

params_A2, cov_A2 = curve_fit(g, d_A[5:10], ln_A[5:10])
#m_A2  = params_A2[0]
b_A2  = params_A2[0]
#Δm_A2 = np.sqrt(cov_A2[0][0])
Δb_A2 = np.sqrt(cov_A2[0][0])

m_A2 = 0
#b_A2 = np.log(0.1876967839)
Δm_A2 = 0
#Δb_A2 = print('Geradensteigung 1 Alu:')
print('{}+-{}'.format(m_A1,Δm_A1))
print('y-Achsenabschnit 1 Alu:')
print('{}+-{}'.format(b_A1,Δb_A1))

print('Geradensteigung 2 Alu:')
print('{}+-{}'.format(m_A2,Δm_A2))
print('y-Achsenabschnit 2 Alu:')
print('{}+-{}'.format(b_A2,Δb_A2))

R = (b_A2-b_A1)/(m_A1-m_A2)
ΔR = np.sqrt((1/(m_A1-m_A2)*Δb_A2)**2+(1/(m_A1-m_A2)*Δb_A1)**2+((b_A1-b_A2)/(m_A2-m_A1)**2*Δm_A1)**2+((b_A2-b_A1)/(m_A1-m_A2**2)*Δm_A2)**2)

rho=2.7 # g/cm^3
E = 1.92*np.sqrt((rho*R*1e2)**2+0.22*(rho*R*1e2))
ΔE = 1.92*np.sqrt((rho*ΔR*1e2)**2+0.22*(rho*ΔR*1e2))

print('R',R)
print('ΔR',ΔR)
print('E',E)
print('ΔE',ΔE)


x = np.linspace(90e-6, 500e-6, 2000)
#plt.plot(d_A*1e6, N_A/t_A-Nulleffekt, 'gx')
plt.errorbar(d_A*1e6, N_A/t_A-Nulleffekt, np.sqrt(N_A/t_A-Nulleffekt), fmt='gx', label='Messwerte')
plt.plot(x*1e6, np.exp(f(x, m_A1, b_A1)), 'k-', label='Gerade 1')
plt.plot(x*1e6, np.exp(f(x, m_A2, b_A2)), 'k--', label='Gerade 2')
plt.yscale('log', nonposy='clip')

plt.xlim(90, 460)
plt.ylim(0.009, 100)
plt.xlabel(r'$\mathrm{Dicke}\; d/\mathrm{\mu m}$')
plt.ylabel(r'$\mathrm{Impulsrate}\; N-N_{\mathrm{u}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("Bilder/beta.pdf")
#plt.show()
plt.close()