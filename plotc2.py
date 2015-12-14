import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#Messwerte:

f, t, U = np.genfromtxt('Datencd.txt', unpack = True)
plt.plot(f, U,'k.', label = r'Messwerte')

#gemessene Resonanzfrequenz:

plt.plot((26200, 26200), (1, 1000), 'k',
label = r'Resonanzfrequenz')

#Grundwerte:

R = 67.2
L = 16.78 * 10**(-3)
C = 2.066 * 10**(-9)

#Theoriekurve:

v = np.linspace(0, 350000, 1000)
plt.plot(v/(2*np.pi), 10/np.sqrt(((1-L*C*v**2)**2) +
(v**2 * R**2 * C**2)), 'r', label = r'Theoriekurve')

#Theorie-Frequenz-Wert:

l = (np.sqrt(1/(L*C) - R**2/(2*L**2))/(2*np.pi))
plt.plot((l, l), (1, 1000), 'r')

print(l)

#Theorie Peak-Grenzen

h = 10/(np.sqrt(((1-L*C*(l*2*np.pi)**2)**2) + ((l*2*np.pi)**2 * R**2 * C**2)))

k = h/np.sqrt(2)

i = 1/(2*np.pi)*np.sqrt((2*L*C-R**2*C**2)/(2*L**2*C**2)  +  np.sqrt( ((-2*L*C+R**2*C**2)/(2*L**2*C**2))**2 +
400 * (np.pi)**2/(k**2*L**2*C**2) - 1/(L**2*C**2) ))

j = 1/(2*np.pi)*np.sqrt((2*L*C-R**2*C**2)/(2*L**2*C**2)  -  np.sqrt( ((-2*L*C+R**2*C**2)/(2*L**2*C**2))**2 +
400 * (np.pi)**2/(k**2*L**2*C**2) - 1/(L**2*C**2) ) )

print(h, i, j)

#Rest:

plt.xlim(0,45100)
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$U/\si{\V}$')
plt.yscale('log')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/plotc2.pdf')
