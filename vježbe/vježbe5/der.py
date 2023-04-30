import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

def cubic(x):
    return 3*x**3 + x**2 + x + 1

h_01 = calc.derivacija_interval(-2, 2, 0.01, cubic)
h_1 = calc.derivacija_interval(-2, 2, 0.1, cubic)
ab = np.linspace(-2, 2, 1000)
h_0 = [9*x**2 + 2*x +1 for x in ab]

plt.title('Derivacija')
plt.xlabel('x')
plt.ylabel('f`(x)')
plt.plot(ab, h_0, label = 'analitička derivacija')
plt.plot(h_01[0], h_01[1], label = 'h = 0.01')
plt.plot(h_1[0], h_1[1], label = 'h = 0.1')
plt.legend()
plt.show()

