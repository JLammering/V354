import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

R1 = ufloat(67.2, 0.2)
R2 = ufloat(682, 1)
L = ufloat(16.78 * 10**(-3), 0.09 * 10**(-3))
C = ufloat(2.066 * 10**(-9), 0.006 * 10**(-9))

b = (4*L/C)**(0.5)
d = R1/(2*np.pi*L)

print('Wert für b:',b,'Wert für d:',d)
