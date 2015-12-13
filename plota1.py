import matplotlib.pyplot as plt
import numpy as np

x, y = np.genfromtxt('Datena1.txt', unpack = True)

x = x * 10**(-6)
y = y * 10**(-5) - 96.9

plt.plot(x, y, 'k-', label = r'Messwerte')

plt.xlim(0, 470)
plt.grid()
plt.legend(loc = 'best')
plt.xlabel(r'$t/\si{\micro\second}$')
plt.ylabel(r'$U/\si{\V}$')

plt.savefig('build/plota1.pdf')
