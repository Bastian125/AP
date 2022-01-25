import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.optimize as opt

####################SPULE#################

def curvefit(x):

    R = 0.00042025
    I = 0.00018855*10**(3)
    return I*R/( ( R + ((x-7.5)*0.01)**2 )**(3/2))

def curvefit2(x):

    R = 0.00042025
    I = 0.00004855*10**(3)
    return I*R/( ( R + ((x-7.5)*0.01)**2 )**(3/2))

B, x1 = np.genfromtxt('langeSpule.txt', unpack=True)

plt.plot(x1, B, 'rx', label='Messwerte')
plt.axis([0, 10.5, 0, 10])
plt.xlabel(r'$x \:/\: \unit{\cm}$')
plt.ylabel(r'$|B| \:/\: \unit{\tesla} \cdot 10^{-3}$')


# plot der Theoriekurve
x = np.linspace(0,10)
plt.plot(x, curvefit(x), color='blue', label='Theoriekurve zu den gegebenen Werten')

plt.plot(x, curvefit2(x), color='grey', linestyle='--', label='Optimierte Kurve')

plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich)
plt.savefig('build/plot.pdf')

################HELMHOLTZ12#################

plt.close()

def Helmholtz12(x):
    I = 2.512*10**(-3)
    R = 0.00390625
    n = 100
    return (I*R*n/((R+(x-6*10**(-2))**2)**(3/2))) + (I*R*n/((R+(x+6*10**(-2))**2)**(3/2)))
B12, x12 = np.genfromtxt('Helmholtz12.txt', unpack=True)

plt.plot(x12, B12, 'rx', label='Messwerte')
plt.axis([-12, 12, 0, 6])
plt.xlabel(r'$x \:/\: \unit{\cm}$')
plt.ylabel(r'$|B| \:/\: \unit{\tesla} \cdot 10^{-3}$')


# plot der Theoriekurve
x = np.linspace(-12,12)
plt.plot(x, Helmholtz12(x*10**(-2)), color='blue', label='Theoriekurve zu den gegebenen Werten')

plt.legend(loc='best')

print(f'12: \t{Helmholtz12(0)}')

plt.savefig('build/plot2.pdf')

############HELMHOLTZ14#############

plt.close()

def Helmholtz14(x):
    I = 2.512*10**(-3)
    R = 0.00390625
    n = 100
    return (I*R*n/((R+((x-7)*10**(-2))**2)**(3/2))) + (I*R*n/((R+((x+7)*10**(-2))**2)**(3/2)))
B14, x14 = np.genfromtxt('Helmholtz14.txt', unpack=True)

plt.plot(x14, B14, 'rx', label='Messwerte')
plt.axis([-13, 13, 0, 5])
plt.xlabel(r'$x \:/\: \unit{\cm}$')
plt.ylabel(r'$|B| \:/\: \unit{\tesla} \cdot 10^{-3}$')


# plot der Theoriekurve
x = np.linspace(-13,13)
plt.plot(x, Helmholtz14(x), color='blue', label='Theoriekurve zu den gegebenen Werten')

plt.legend(loc='best')
print(f'14: \t{Helmholtz14(0)}')
plt.savefig('build/plot3.pdf')

############HELMHOLTZ16###############

plt.close()

def Helmholtz16(x):
    I = 2.512*10**(-3)
    R = 0.00390625
    n = 100
    return (I*R*n/((R+((x-8)*10**(-2))**2)**(3/2))) + (I*R*n/((R+((x+8)*10**(-2))**2)**(3/2)))
B16, x16 = np.genfromtxt('Helmholtz16.txt', unpack=True)

plt.plot(x16, B16, 'rx', label='Messwerte')
plt.axis([-14, 14, 0, 5])
plt.xlabel(r'$x \:/\: \unit{\cm}$')
plt.ylabel(r'$|B| \:/\: \unit{\tesla} \cdot 10^{-3}$')


# plot der Theoriekurve
x = np.linspace(-14,14)
plt.plot(x, Helmholtz16(x), color='blue', label='Theoriekurve zu den gegebenen Werten')

plt.legend(loc='best')
print(f'16: \t{Helmholtz16(0)}')
plt.savefig('build/plot4.pdf')

#########Hysteresekurve###########
plt.close()

BH1, IH1, H1, M1 = np.genfromtxt('Hysterese1.txt', unpack=True)
BH2, IH2, H2, M2 = np.genfromtxt('Hysterese2.txt', unpack=True)
BH3, IH3, H3, M3 = np.genfromtxt('Hysterese3.txt', unpack=True)
plt.plot(H1, BH1, 'r-', label='erste Kurve')
plt.plot(H1, BH1, 'rx')
plt.plot(H2, BH2, 'b-', label='zweite Kurve')
plt.plot(H2, BH2, 'bx')
plt.plot(H3, BH3, 'g-', label='dritte Kurve')
plt.plot(H3, BH3, 'gx')
plt.grid(True)
plt.plot([0,0], [129.0, -123.6], 'm*', label='Remanenz')
plt.plot([370,-370], [0,0], 'c*', label='Koerzitivkraft')
plt.plot([-7018.2,7018.2], [-713.2,718], 'y*', label='Sättigung')

plt.axis([-8000, 8000, -800, 800])
plt.xlabel(r'$H \:/\: \unit{\ampere}\:/\: \unit{\m}$')
plt.ylabel(r'$B \:/\: \unit{\tesla} \cdot 10^{-3}$')
plt.legend(loc='best')
plt.savefig('build/plot5.pdf')

#def H(k):
#    r=0.135
#    n=595
#    return  (n*k)/(2*3.14*r)
#
#def M(B,H):
#    return B/(1.257*10**(-6)) - H
#
#print(f'M1: \t{M(BH1*10**(-3), H1)}, M2: \t{M(BH2*10**(-3), H2)} , M3: \t{M(BH3*10**(-3), H3)}')