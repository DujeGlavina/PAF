import numpy as np
import matplotlib.pyplot as plt
def jednoliko_gibanje(f,m):
    a=f/m
    plt.subplot(1,3,1)
    plt.xlabel('t/s')
    plt.ylabel('a/ms^-2')
    plt.plot((0,10),(a,a))
    t=np.arange(0,10,0.1)
    v=a*t
    plt.subplot(1,3,2)
    plt.xlabel('t/s')
    plt.ylabel('v/ms^-1')
    plt.plot(t,v)
    x=1/2*a*t*t
    plt.subplot(1,3,3)
    plt.xlabel('t/s')
    plt.ylabel('x/m')
    plt.plot(t,x)
    plt.show()
    
def kosi_hitac(v0,kut0):
    kut=np.pi/180*kut0
    vx=v0*np.cos(kut)
    vy=v0*np.sin(kut)
    v_x=np.zeros(100)
    v_x+=vx
    v_y=[]
    v_y.append(vy)
    t=0.1
    for i in range(1,100):
        v_y.append(v_y[i-1]-9.81*t)

    x = []
    x.append(vx*t)
    y = []
    y.append(vy*t)
    for i in range(1,100):
        x.append(x[i-1]+v_x[i]*t)
        y.append(y[i-1]+v_y[i]*t)

    plt.subplot(1,3,1)
    plt.xlabel('x/m')
    plt.ylabel('y/m')
    plt.plot(x,y)

    plt.subplot(1,3,2)
    plt.xlabel('t/s')
    t=np.arange(0,10,0.1)
    plt.ylabel('x/m')
    plt.plot(t,x)

    plt.subplot(1,3,3)
    plt.xlabel('t/s')
    plt.ylabel('y/m')
    plt.plot(t,y)
    plt.show()
    