import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Alle Messwerte:

x, y = np.genfromtxt('Datena1.txt', unpack = True)
x = x * 10**(-12)
y = y * 10**(-5) - 96.9

plt.plot(x, y, 'k-', label = r'Messwerte')


# Plot der Maxima und Ausgleichsfunktion:

m, n = np.genfromtxt('Datena2.txt', unpack = True)
n = n - 96.9

def f(m, a, b):
    return a * np.exp(-2*np.pi*b * m)

params, cov = curve_fit(f, m, n)

print(*params)

plt.plot(m, n, 'b.', label = r'Maxima und Minima')
m = np.linspace(0, 0.0005, 500)
plt.plot(m, f(m, *params), 'r', label = r'Einhüllene Funktionen')


# Plot der Minima und Ausgleichsfunktion:

o, p = np.genfromtxt('Datena3.txt', unpack = True)
p = p - 96.9

def f(o, a, b):
    return a * np.exp(-2*np.pi*b * o)

params, cov = curve_fit(f, o, p)

print(*params)

plt.plot(o, p, 'b.')
o = np.linspace(0, 0.0005, 500)
plt.plot(o, f(o, *params), 'r')

#Grundwerte:

L = 16.78 * 10**(-3)
C = 2.066 * 10**(-9)

#Theoriewert:

print(np.sqrt(4*L/C))

# Rest:

plt.xlim(0, 0.00046)
plt.grid()
plt.legend(loc = 'best')
plt.xlabel(r'$t/\si{\second}$')
plt.ylabel(r'$U/\si{\V}$')

plt.savefig('build/plota.pdf')
