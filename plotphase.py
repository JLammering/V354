import matplotlib.pyplot as plt
import numpy as np

R = 67.2
L = 16.78e-3
C = 2.066e-9

x = np.linspace(0, 45000*2*np.pi, 900000)
plt.plot(x, np.arctan((-x*R*C)/(1-L*C*x**2)), 'b-', label = r'Theoriekurve')

plt.xlim(0,45100*2*np.pi)
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$\phi$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/plotphase.pdf')
