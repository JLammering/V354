import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from uncertainties import ufloat

#links:
a,m,b = np.genfromtxt('Datencr.txt', unpack = True)

#Rects:
u,m,v = np.genfromtxt('Datencl.txt', unpack = True)

# m unwichtig

x = np.linspace(20000,35000)
slope, intercept, p_value, r_value, std_err = linregress(a, b)
sl = ufloat(slope, std_err)
il = intercept
plt.plot(x, slope*x+il, 'r-', label=r'linke Regression')

slope, intercept, p_value, r_value, std_err = linregress(u, v)
sr = ufloat(slope, std_err)
ir = intercept
plt.plot(x, slope*x+ir, 'b-', label=r'rechte Regression')

res = (ir-il)/(sl-sr)
peak = sl*res+il
hohe = peak/np.sqrt(2)
l = (hohe-il)/sl
r = (hohe-ir)/sr
br = r-l
good = res/(r-l)
np.savetxt('build/mist.txt', np.column_stack([good.n,good.s,res.n, res.s,peak.n, peak.s, hohe.n, hohe.s,
l.n, l.s, r.n, r.s, br.n, br.s]), header =
"Güte,Gütefehler,Reso,Resofehler,Peak,Peakfehler,Höhe,Höhenfehler,Links,Linksfehler,Rechts,Rechtsfehler,Breite,Breitenfehler")

plt.plot(a, b, 'k.', label = r'Messwerte')
plt.plot(u, v, 'k.')

plt.legend(loc='best')
plt.xlabel(r'$\nu/\si{\hertz}$')
plt.ylabel(r'$U/\si{\V}$')
plt.xlim(24900,27800)
plt.ylim(50,250)
plt.grid()
plt.savefig('build/plotc3.pdf')
