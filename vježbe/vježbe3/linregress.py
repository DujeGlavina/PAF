import numpy as np
import matplotlib.pyplot as plt
M=[0.052,0.124,0.168,0.236,0.284,0.336]
fi=[0.1745,0.3491,0.5236,0.6981,0.8727,1.0472] 
suma_xy=0
for i in range(6):
    suma_xy+=M[i]*fi[i]
suma_x2=0
for i in range(6):
    suma_x2+=fi[i]*fi[i]
suma_y2=0
for i in range(6):
    suma_y2+=M[i]*M[i]
a=suma_xy/suma_x2
print(a)
plt.plot(fi,M,"o")
plt.xlabel("fi/rad")
plt.ylabel("M/Nm")
M=[]
for i in range(6):
    M.append(a*fi[i])
plt.plot(fi,M)
plt.show()
dev_a=np.sqrt(1/6*(suma_y2/suma_x2-a**2))
print("Modul torzije {} +- {}".format(a,dev_a))
