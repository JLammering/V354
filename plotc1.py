import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import linregress

#Messwerte:

f, t, U = np.genfromtxt('Datencd.txt', unpack = True)
plt.plot(f, U, 'k.', label = r'Messdaten')

R = 67.2
L = 16.78 * 10**(-3)
C = 2.066 * 10**(-9)

#Ausgleichsfunktion:
def g(f, l, c, r):
    w = 2*np.pi*f
    return 10/(np.sqrt((1-l*c*w**2)**2 + w**2*r**2*c**2))

params, cov = curve_fit(g, f, U)

f = np.linspace(0, 30000, 10000)
plt.plot(f, g(f, *params), 'r-')

#Breitenfrequenzen:
x = np.linspace(0, 46000, 10)
plt.plot(x, 0*x + 186/np.sqrt(2), 'b', label = r'Kurvenbreite')

print(186/np.sqrt(2))

#Rest:
plt.xlim(0,30000)
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$U/\si{\V}$')
plt.yscale('log')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/plotc1.pdf')
