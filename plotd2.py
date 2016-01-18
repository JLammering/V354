import matplotlib.pyplot as plt
import numpy as np

f, t, U  = np.genfromtxt('Datencdh.txt', unpack = True)
t = t * f * 360 * 10**(-6)

plt.plot(f, t, 'kx', label = 'Messwerte')

plt.xlim(24900,28100)
plt.legend(loc = 'best')
plt.yscale('log')
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$\varphi$')
plt.savefig('build/plotd2')
