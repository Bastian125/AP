import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op

c_L = 1800
c_P = 2700
nu_0 = 2*10**6
theta = [np.pi/12, np.pi/6, np.pi/4]
alpha = (np.pi/2)-np.arcsin(np.sin(theta)*(c_L/c_P))

#Messaufgabe 1

# mittleres Rohr
rpm, f_diff15, f_diff30, f_diff45 = np.genfromtxt("Messwerte/Teil1.txt", unpack = True)

v_Str15 = f_diff15*c_L/(2*nu_0*np.cos(alpha[0]))
v_Str30 = f_diff30*c_L/(2*nu_0*np.cos(alpha[1]))
v_Str45 = f_diff45*c_L/(2*nu_0*np.cos(alpha[2]))


plt.xlabel(r'$v_{\mathrm{Str}} / \mathrm{m s}^{-1}$')
plt.ylabel(r'$\frac{\Delta f}{\cos{\alpha}}/ \mathrm{Hz}$')
plt.grid()
plt.plot(v_Str15,f_diff15/np.cos(alpha[0]), marker = '.', color = 'b', linewidth = 0, label = r'$\theta = 15 ^\circ$') 

plt.plot(v_Str30,f_diff30/np.cos(alpha[1]), marker = '.', color = 'g', linewidth = 0, label = r'$\theta = 30 ^\circ$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.plot(v_Str45,f_diff45/np.cos(alpha[2]), marker = '.', color = 'r', linewidth = 0,  label = r'$\theta = 45 ^\circ$') 

plt.legend() 

plt.savefig('build/plot1_2.pdf')
plt.close()


# Messaufgabe 2

t, f_diff, v, I = np.genfromtxt("Messwerte/Teil2_45.txt", unpack = True)

#FIT


plt.subplot(1,2,1)
plt.plot(t, I, marker = "x" ,color = "firebrick", linewidth = 0, label = "Messwerte")

plt.legend()
plt.xlabel(r'Messtiefe / µs')
plt.ylabel(r'$I / \mathrm{kV}^2\mathrm{s}^{-1}$')
plt.xlim(13, 17.5)

plt.grid()
plt.title("Streuintensität")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.subplot(1,2,2)
plt.plot(t, v, marker = "x" ,color = "firebrick", linewidth = 0)

plt.xlabel(r'Messtiefe in $...$')
plt.ylabel(r'$v / \mathrm{cms}^{-1}$')
plt.xlim(13, 17.5)

plt.grid()
plt.title("Momentangeschwindigkeit")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

#plt.show()

plt.savefig('build/plot2_1.pdf')
plt.close()

t, f_diff, v, I = np.genfromtxt("Messwerte/Teil2_70.txt", unpack = True)

plt.subplot(1,2,1)
plt.plot(t, I, marker = "x" ,color = "firebrick", linewidth = 0, label = "Messwerte")

plt.legend()
plt.xlabel(r'Messtiefe / µs')
plt.ylabel(r'$I / \mathrm{kV}^2\mathrm{s}^{-1}$')
plt.xlim(11.5, 20)
plt.ylim(0)
plt.grid()
plt.title("Streuintensität")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.subplot(1,2,2)
plt.plot(t[2:13], v[2:13], marker = "x" ,color = "firebrick", linewidth = 0)

plt.xlabel(r'Messtiefe in $...$')
plt.ylabel(r'$v / \mathrm{cms}^{-1}$')
plt.xlim(12.5, 18.5)
plt.ylim(0)
plt.grid()
plt.title("Momentangeschwindigkeit")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.show()
plt.savefig('build/plot2_2.pdf')
plt.close()