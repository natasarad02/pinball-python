import numpy as np



ode=lambda x,y: 2 - np.exp(-4*x) - 2*y
fun=lambda x: 1 + 1/2 * np.exp(-4*x) - 1/2*np.exp(-2*x) #analiticko resenje ode
x0=0
y0=1
xn=1
h=0.1
y=ojler(x0,xn,y0,h,ode)
print(y)
