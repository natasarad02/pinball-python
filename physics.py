import numpy as np


def ojler(x0,xn,y0,h,odj):
    x = np.arange(x0,xn+h,h)
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(1,n):
        y[i] = y[i-1] + h * odj(x[i-1], y[i-1])
    return y

ode=lambda x,y: 2 - np.exp(-4*x) - 2*y
fun=lambda x: 1 + 1/2 * np.exp(-4*x) - 1/2*np.exp(-2*x) #analiticko resenje ode
x0=0
y0=1
xn=1
h=0.1
y=ojler(x0,xn,y0,h,ode)
print(y)
