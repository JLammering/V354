import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

u = ufloat(630, 40)
L = ufloat(16.78/1000, 0.09/1000)

r = 4*np.pi*u*L

print('effektivDämpfwiderstand:', r)

T = 1/(2*np.pi*u)

print('Abklingdauer:', T)
