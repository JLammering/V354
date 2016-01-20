import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.optimize import fmin
from scipy.stats import linregress
from uncertainties import unumpy as unp


#Messwerte:

f, t, U = np.genfromtxt('Datencd.txt', unpack = True)
plt.plot(f, U, 'k.', label = r'Messdaten')

R = 67.2
L = 16.78 * 10**(-3)
C = 2.066 * 10**(-9)

#Ausgleichsfunktion:
def g(f, r, l, c):
    w = 2*np.pi*f
    return 10/(np.sqrt((1-l*c*w**2)**2 + w**2*r**2*c**2))

params, cov = curve_fit(g, f, U, p0=(1e2, 10e-3,1e-9))

print(params)
errors = np.sqrt(np.diag(cov))
print(errors)

f = np.linspace(0, 41000, 10000)
plt.plot(f, g(f, *params), 'r-', label = r'Ausgleichsfunktion')

#Breitenfrequenzen:
x = np.linspace(0, 46000, 10)
plt.plot(x, 0*x + 186/np.sqrt(2), 'b', label = r'Kurvenbreite')

a = 1.90325764e+02
b = 2.13496513e-02
c = 1.71397082e-09
v = np.sqrt((b-c*a**2)/(b**2*4*np.pi**2*c))

peak = g(v, *params)

m = peak/np.sqrt(2)

links = np.sqrt((1/(b*c)-a**2/(2*b**2))-np.sqrt(((a**2/(b**2)-2/(b*c))**2)/4 +
(100/(m**2)-1)/(b**2*c**2)))*(1/(2*np.pi))
rechts = np.sqrt((1/(b*c)-a**2/(2*b**2))+np.sqrt(((a**2/(b**2)-2/(b*c))**2)/4 +
(100/(m**2)-1)/(b**2*c**2)))*(1/(2*np.pi))

print('Güte:', 1/(a*c*v*2*np.pi))

#print('ResonanzpeakWert:' ,peak)
#print('Resonanzpeakfrequenz:' ,v)
#print('linke Frequenz:' ,links)
#print('rechte Frequenz:' ,rechts)
#print('Güte:', v/(rechts-links))


#Rest:
plt.xlim(0,40000)
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$U/\si{\V}$')
plt.yscale('log')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/plotc1.pdf')
