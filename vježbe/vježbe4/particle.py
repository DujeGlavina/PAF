import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, x0, y0, v0, angle, dt):
        self.x0=x0
        self.y0=y0
        self.v0=v0
        self.angle=angle*np.pi/180
        self.dt=dt
        self.x=[]
        self.y=[]
        self.x.append(x0)
        self.y.append(y0)
        self.vx=[]
        self.vy=[]
        self.vx.append(v0*np.cos(self.angle))
        self.vy.append(v0*np.sin(self.angle))

    def reset(self):
        self.x0=0
        self.y0=0
        self.v0=0
        self.angle=0

    def __move(self):
        pozicija=len(self.vx)
        self.x.append(self.x[pozicija-1] + self.vx[pozicija-1]*self.dt)
        self.y.append(self.y[pozicija-1] + self.vy[pozicija-1]*self.dt - (9.81/2)*self.dt**2)
        self.vx.append(self.v0*np.cos(self.angle))
        self.vy.append(self.vy[pozicija-1] - 9.81*self.dt)

    def range(self):
        for yi in self.y:
            if yi >= 0:
                self.__move()
        pozicija=len(self.x)
        return self.x[pozicija-1]

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('Domet projektila')
        plt.show()
