import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x, y = np.genfromtxt('Datena2.txt', unpack = True)
y = y - 96.9

def f(x, a, b):
    return a * np.exp(b * x)

params, cov = curve_fit(f, x, y)

print(*params)

plt.plot(f(x, *params))
plt.plot(x, y, 'k.')
plt.xlim(0, 2)

plt.savefig('build/plota2.pdf')
