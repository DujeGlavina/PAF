import numpy as np
import matplotlib.pyplot as plt

def derivacija_tocka(x, h, f, point=3):
    if (point == 2):
        der = (f(x+h) - f(x))/h
    if (point == 3):
        der = 0.5*(f(x+h) - f(x-h))/h
    return der

def derivacija_interval(a, b, h, f, point=3):
    ab = np.linspace(a,b,1000)
    der_ab = [derivacija_tocka(x, h, f, point) for x in ab]
    return ab, der_ab

def integral_pravokutnik(a, b, n, f):
    dx = np.abs(b-a)/n
    gornja_suma, donja_suma = 0, 0
    ab = np.linspace(a,b,n)
    gornja_suma = sum([f(x)*dx for x in ab if x != a])
    donja_suma = sum([f(x)*dx for x in ab if x != b])
    return gornja_suma, donja_suma

def integral_trapez(a, b, n, f):
    dx = np.abs(b-a)/n
    suma = 0
    ab = np.linspace(a,b,n)
    suma = sum([f(ab[i-1]) + f(ab[i]) for i in range(1, n)])
    integral = suma*dx/2
    return integral

