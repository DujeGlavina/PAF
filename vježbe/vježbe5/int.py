import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

def cubic(x):
    return 3*x**3 + x**2 + x + 1

int1 = []
int2 = []
int3 = []
steps = np.arange(200, 2000, 100)
for n in steps:
    int1.append(calc.integral_pravokutnik(0, 1, n, cubic)[0])
    int2.append(calc.integral_pravokutnik(0, 1, n, cubic)[1])
    int3.append(calc.integral_trapez(0, 1, n, cubic))

plt.title('Integral')
plt.xlabel('n')
plt.ylabel('integral')
plt.scatter(steps, int1, label = 'gornja integralna suma')
plt.scatter(steps, int2, label = 'donja integralna suma')
plt.scatter(steps, int3, label = 'metoda trapeza')
plt.legend()
plt.show()
