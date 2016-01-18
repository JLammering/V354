import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from uncertainties import ufloat

f, t, U  = np.genfromtxt('Datencdh2.txt', unpack = True)
t = t * f * 360 * 10**(-6)
plt.plot(f, t, 'kx', label = 'Messwerte')

# Lineare Regression:
slope, intercept, r_value, p_value, std_err = linregress(f, t)
x = np.linspace(25700,26800)
plt.plot(x, slope*x + intercept, 'r-', label = 'Ausgleichsgerade')

s = ufloat(slope, std_err)
res = (90-intercept)/s
left = (45-intercept)/s
right = (135-intercept)/s

print('Resonanzfrequenz:', res)
print('links:', left)
print('rechts:', right)

Güte = res/(right-left)

print('Güte:', Güte)

plt.xlim(25700,26800)
plt.legend(loc = 'best')
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$\varphi$')
plt.savefig('build/plotd3')
