import matplotlib.pyplot as plt
import numpy as np

f, t, U = np.genfromtxt('Datencd.txt', unpack = True)
f = f/1000
t = t * f * 1000 * 10**(-6) * 2 * np.pi

plt.polar(t, f)
plt.grid()

plt.savefig('build/plotd.pdf')
