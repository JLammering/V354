import matplotlib.pyplot as plt
import numpy as np

R = 67.2
L = 16.78 * 10**(-3)
C = 2.066 * 10**(-9)

f, t, U = np.genfromtxt('Datencd.txt', unpack = True)
plt.plot(f, U, 'k.', label = r'Messdaten')
plt.plot((26200, 26200), (1, 1000), 'k-',
label = r'Resonanzfrequenz')

v = np.linspace(0, 350000, 1000)
plt.plot(v/(2*np.pi), 10/np.sqrt(((1-L*C*v**2)**2) +
(v**2 * R**2 * C**2)), 'r-', label = r'Theoriekurve')

print(np.sqrt(1/(L*C) - R**2/(2*L**2))/(2*np.pi), np.sqrt(4*L/C))

plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$U/\si{\V}$')
plt.yscale('log')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/plotc.pdf')
