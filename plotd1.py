import matplotlib.pyplot as plt
import numpy as np

f, t, U = np.genfromtxt('Datencd.txt', unpack = True)
f = f / 1000
t = t * f * 10**(-3) * 2 * np.pi

plt.polar(t, f, 'r')
plt.savefig('build/plotd1.pdf')
