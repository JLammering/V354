import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Messwerte:

f, t, U = np.genfromtxt('Datencd.txt', unpack = True)
plt.plot(f, U, 'k.', label = r'Messdaten')

#Resonanzfrequenz:

plt.plot((26200, 26200), (1, 1000), 'k-',
label = r'Resonanzfrequenz')

#Breitenfrequenzen:

x = np.linspace(0, 46000, 10)
plt.plot(x, 0*x + 186/np.sqrt(2), 'b', label = r'Kurvenbreite')

print(186/np.sqrt(2))

#Rest:

plt.xlim(0,45100)
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$U/\si{\V}$')
plt.yscale('log')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/plotc1.pdf')
