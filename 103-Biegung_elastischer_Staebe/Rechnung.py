import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import scipy.optimize as opt
#Masse rund

Masse_rund = np.genfromtxt('Messwerte/Massen_rund.txt', unpack=True)
print('\n Masse rund: ', Masse_rund, '\n Mittelwert: ', np.round(np.mean(Masse_rund), 4), '\n Abweichung: ', np.round(np.std(Masse_rund), 4))

#Masse eckig

Masse_eckig = np.genfromtxt('Messwerte/Massen_eckig.txt', unpack=True)
print('\n Masse eckig: ', Masse_eckig, '\n Mittelwert: ', np.round(np.mean(Masse_eckig), 4), '\n Abweichung: ', np.round(np.std(Masse_eckig), 4))

#Durchmesser rund

Durchmesser_rund = np.genfromtxt('Messwerte/Durchmesser_rund.txt', unpack=True)
print('\n Durchmesser rund: ', Durchmesser_rund, '\n Mittelwert: ', np.round(np.mean(Durchmesser_rund), 4), '\n Abweichung: ', np.round(np.std(Durchmesser_rund), 4))

#Durchmesser eckig

Durchmesser_eckig = np.genfromtxt('Messwerte/Durchmesser_eckig.txt', unpack=True)
print('\n Durchmesser eckig: ', Durchmesser_eckig, '\n Mittelwert: ', np.round(np.mean(Durchmesser_eckig), 4), '\n Abweichung: ', np.round(np.std(Durchmesser_eckig), 4))

#Länge rund

Laenge_rund = np.genfromtxt('Messwerte/Laenge_rund.txt', unpack=True)
print('\n Länge rund: ', Laenge_rund, '\n Mittelwert: ', np.round(np.mean(Laenge_rund), 4), '\n Abweichung: ', np.round(np.std(Laenge_rund), 4))

#Länge eckig

Laenge_eckig = np.genfromtxt('Messwerte/Laenge_eckig.txt', unpack=True)
print('\n Länge eckig: ', Laenge_eckig, '\n Mittelwert: ', np.round(np.mean(Laenge_eckig), 4), '\n Abweichung: ', np.round(np.std(Laenge_eckig), 4))

#Dichte Zylinder rund

r_r = ufloat(np.round(np.mean(Durchmesser_rund), 4), np.round(np.std(Durchmesser_rund), 4))
l_r = ufloat(np.round(np.mean(Laenge_rund), 4), np.round(np.std(Laenge_rund), 4))
m_r = ufloat(np.round(np.mean(Masse_rund), 4), np.round(np.std(Masse_rund), 4))

print('Dichte rund: ', m_r/ (np.pi * (r_r)**2 * l_r))

#Dichte Zylinder eckig

d_e = ufloat(np.round(np.mean(Durchmesser_eckig), 4), np.round(np.std(Durchmesser_eckig), 4))
l_e = ufloat(np.round(np.mean(Laenge_eckig), 4), np.round(np.std(Laenge_eckig), 4))
m_e = ufloat(np.round(np.mean(Masse_eckig), 4), np.round(np.std(Masse_eckig), 4))

print('Dichte eckig: ', m_e/ ((d_e)**2 * l_e))

#Flächenträgheitsmoment rund

print('\n Flächenträgheitsmoment rund: ', (((Durchmesser_rund))**4 * np.pi) / 4 , '\n Mittelwert: ', np.round(np.mean((((Durchmesser_rund))**4 * np.pi) / 4), 20), '\n Abweichung: ', np.round(np.std((((Durchmesser_rund))**4 * np.pi) / 4), 40))

#Flächenträgheitsmoment eckig

print('Flächenträgheitsmoment eckig: ', (Durchmesser_eckig)**4 / 12 , '\n Mittelwert: ', np.round(np.mean((Durchmesser_eckig)**4 / 12), 20), '\n Abweichung: ', np.round(np.std((Durchmesser_eckig)**4 / 12), 40))

#Restliche Länge einseitig rund

L_ER = np.genfromtxt('Messwerte/Restliche_Laenge_einseitig_rund.txt', unpack=True)
print('\n Restliche Länge einseitiges Einspannen rund: ', L_ER, '\n Mittelwert: ', np.round(np.mean(L_ER), 4), '\n Abweichung: ', np.round(np.std(L_ER), 4))

#Restliche Länge einseitig eckig

L_EE = np.genfromtxt('Messwerte/Restliche_Laenge_einseitig_eckig.txt', unpack=True)
print('\n Restliche Länge einseitiges Einspannen eckig: ', L_EE, '\n Mittelwert: ', np.round(np.mean(L_EE), 4), '\n Abweichung: ', np.round(np.std(L_EE), 4))

#Restliche Länge beidseitig rund

L_BR = np.genfromtxt('Messwerte/Restliche_Laenge_beidseitig_rund.txt', unpack=True)
print('\n Restliche Länge beidseitiges Einspannen rund: ', L_BR, '\n Mittelwert: ', np.round(np.mean(L_BR), 4), '\n Abweichung: ', np.round(np.std(L_BR), 4))

#Restliche Länge beidseitig eckig

L_BE = np.genfromtxt('Messwerte/Restliche_Laenge_beidseitig_eckig.txt', unpack=True)
print('\n Restliche Länge beidseitiges Einspannen eckig: ', L_BE, '\n Mittelwert: ', np.round(np.mean(L_BE), 4), '\n Abweichung: ', np.round(np.std(L_BE), 4))

#Gewicht1

m_ER = np.genfromtxt('Messwerte/Gewicht1.txt', unpack=True)
print('\n Gewicht Nummer 1: ', m_ER, '\n Mittelwert: ', np.round(np.mean(m_ER), 4), '\n Abweichung: ', np.round(np.std(m_ER), 4))

#Gewicht2

m_EE = np.genfromtxt('Messwerte/Gewicht2.txt', unpack=True)
print('\n Gewicht Nummer 2: ', m_EE, '\n Mittelwert: ', np.round(np.mean(m_EE), 4), '\n Abweichung: ', np.round(np.std(m_EE), 4))

#Gewicht3

m_BR = np.genfromtxt('Messwerte/Gewicht3.txt', unpack=True)
print('\n Gewicht Nummer 3: ', m_BR, '\n Mittelwert: ', np.round(np.mean(m_BR), 4), '\n Abweichung: ', np.round(np.std(m_BR), 4))

m_BE = np.genfromtxt('Messwerte/Gewicht4.txt', unpack=True)
print('\n Gewicht Nummer 4: ', m_BE, '\n Mittelwert: ', np.round(np.mean(m_BE), 4), '\n Abweichung: ', np.round(np.std(m_BE), 4))


# beidseitig
def D_mit(x, E):
    r = 0.005 # radius der staebe in meter
    m = 1.4534 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.4797 # hebelarm in metern
    return F / (48 * E * I) * (3 * L**2 * x - 4 * x**3)

def D_mit_left(x,E):
    r = 0.005 # radius der staebe in meter
    m = 0.4513 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.4797 # hebelarm in metern
    return F / (48 * E * I) * (4 * x**3 - 12 * L * x**2 + 9 * L**2 * x - L**3)
