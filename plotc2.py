import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat


#Messwerte:

f, t, U = np.genfromtxt('Datencd.txt', unpack = True)
plt.plot(f, U,'k.', label = r'Messwerte')

#gemessene Resonanzfrequenz:

plt.plot((26200, 26200), (1, 1000), 'k',
label = r'Resonanzfrequenz')

R = 67.2
L = 16.78 * 10**(-3)
C = 2.066 * 10**(-9)

#Theoriekurve:

v = np.linspace(0, 350000, 1000)
plt.plot(v/(2*np.pi), 10/np.sqrt(((1-L*C*v**2)**2) +
(v**2 * R**2 * C**2)), 'r', label = r'Theoriekurve')

#Grundwerte:

#R = ufloat(67.2, 0.2)
#L = ufloat(16.78 * 10**(-3), 0.09 * 10**(-3))
#C = ufloat(2.066 * 10**(-9), 0.006 * 10**(-9))

#Theorie-Frequenz-Wert:

l = (np.sqrt(1/(L*C) - R**2/(2*L**2))/(2*np.pi))
plt.plot((l, l), (1, 1000), 'r')

#Theorie Peak-Grenzen

h = 10/(np.sqrt(((1-L*C*(l*2*np.pi)**2)**2) + ((l*2*np.pi)**2 * R**2 * C**2)))

k = h/np.sqrt(2)

i = np.sqrt((1/(L*C)-R**2/(2*L**2))-np.sqrt(((R**2/(L**2)-2/(L*C))**2)/4 +
(100/(k**2)-1)/(L**2*C**2)))*(1/(2*np.pi))

j = np.sqrt((1/(L*C)-R**2/(2*L**2))+np.sqrt(((R**2/(L**2)-2/(L*C))**2)/4 +
(100/(k**2)-1)/(L**2*C**2)))*(1/(2*np.pi))

print('Theoriespannungen:', h, k)
print('Theoriefrequenzen:', l, j, i)
print('Theoriegüte:', l/(j-i))

#Rest:

plt.xlim(0,45100)
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$U/\si{\V}$')
plt.yscale('log')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/plotc2.pdf')
