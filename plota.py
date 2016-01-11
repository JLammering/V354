import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Alle Messwerte:

x, y = np.genfromtxt('Datena1.txt', unpack = True)
x = x * 10**(-12)
y = y * 10**(-5) - 96.9

plt.plot(x, y, 'k-', label = r'Messwerte')


# Plot der Maxima:

m, n = np.genfromtxt('Datena2.txt', unpack = True)
n = n - 96.9

plt.plot(m, n, 'b.', label = r'Maxima und Minima')

# Plot der Minima:

o, p = np.genfromtxt('Datena3.txt', unpack = True)
p = p - 96.9

plt.plot(o, p, 'b.')

# Ausgleichsfunktion:

k, l = np.genfromtxt('Datena4.txt', unpack = True)
l = np.abs(l-96.9)

def f(k, a, b):
    return a * np.exp(-2*np.pi*b * k)

params, cov = curve_fit(f, k, l)

errors = np.sqrt(np.diag(cov))
print('Parameter der Ausgleichsfkt:', *params)
print('Fehler der Ausgleichsfkt:', errors)

k = np.linspace(0, 0.0005, 500)
plt.plot(k, f(k, *params), 'r', label=r'Einhüllende')
plt.plot(k, -f(k, *params), 'r')

#Grundwerte:

L = 16.78 * 10**(-3)
C = 2.066 * 10**(-9)

#Theoriewert:

print('Theoriewert:',np.sqrt(4*L/C))

# Rest:

plt.xlim(0, 0.00046)
plt.grid()
plt.legend(loc = 'best')
plt.xlabel(r'$t/\si{\second}$')
plt.ylabel(r'$U/\si{\V}$')

plt.savefig('build/plota.pdf')
