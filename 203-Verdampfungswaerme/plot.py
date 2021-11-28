import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy

T,P=np.genfromtxt('daten/bis1bar.txt', unpack=True)

T+=273.15
T*=0.001
P/=994

params, _fehler = np.polyfit(1/T,np.log(P), deg=1, cov=True)
L1=-1*params[0]*const.gas_constant
fehler = np.sqrt(np.diag(_fehler))
print("\nParams=",params)
print("fehler=", fehler)
print(f"L1={L1:.8f} \n")

uparams=unp.uarray(params,fehler)
uL1=-1*uparams[0]*const.gas_constant
La=const.gas_constant * 373 * 0.001
uLa=unc.ufloat(La,0)
uLi=uL1-uLa
uLimol=uLi*1000/(const.Avogadro*const.elementary_charge)
print(f'\n \n L1= {uL1:.4f} J/mol \n La={uLa:.4f} J/mol \n Li= {uLi:.4f} J/mol\n Li pro Molekül in eV: {uLimol:.4f} eV\n')

x=np.linspace(1/T[-1],1/T[0],1000)
plt.figure()
plt.plot(1/T,np.log(P),'.', color='gold',  label='Messwerte')
plt.plot(x, params[0]*x + params[1], color='navy',  label='Ausgleichsgerade')
plt.xlabel(r'$\frac{1}{T} \:/\: \frac{1}{10^3 \cdot K}$')
plt.ylabel(r'$ln\left(\frac{p}{p_0}\right) $')
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
###################

T,P=np.genfromtxt('daten/bis15bar.txt', unpack=True)

T+=273
P*=1e5
params2, _f = np.polyfit(T,P, deg=3, cov=True)
err = np.sqrt(np.diag(_f))
uparam=unp.uarray(params2,err)
print('\n\n15 bar')
print("\nPolynomwerte /T^3, /T^2, /T und :\n", uparam,'\n')


plt.figure()
plt.plot(T,P,'.',label="Messwerte")
plt.plot(T, params2[0]*T**3 + params2[1]*T**2+params2[2]*T+params2[3], label="Ausgleichskurve")
plt.xlabel("T [K]")
plt.ylabel("p [Pa] $\cdot 10^5$")
plt.tight_layout()
plt.legend()
plt.savefig('build/plot2.pdf')



R=const.gas_constant
C=0.9
def L(x,a,b,c,d):
    return ((((R*x)/2)+np.sqrt(((R**2*x**2)/2)-C*(a*x**3+b*x**2+c*x+d)))*((3*a*x**3+2*b*x**2+c*x)/(a*x**3+b*x**2+c*x+d)))

x= np.linspace(T[-1],T[0],1000)


plt.figure()
plt.plot(x, L(x, *params2), label='Genäherte Funktion für L')
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.savefig('build/plot3.pdf')


R=const.gas_constant
def K(x,a,b,c,d):
    return ((((R*x)/2)-np.sqrt(((R**2*x**2)/2)-C*(a*x**3+b*x**2+c*x+d)))*((3*a*x**3+2*b*x**2+c*x)/(a*x**3+b*x**2+c*x+d)))

x= np.linspace(T[-1],T[0],1000)


plt.figure()
plt.plot(x, K(x, *params2), label='Genäherte Funktion für L')
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.savefig('build/plot4.pdf')