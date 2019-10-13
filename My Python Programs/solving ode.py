import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model (y,t):
     #k = 0.3
     dydt = -k*y
     return dydt

#y0 = 0.1

def pend(y, t):
     b= 4
     theta, omega = y
     dydt = [omega, -b*omega + b*b]
     return dydt

t = np.linspace(0,10, 100)
y0 = [10, 10]

y = odeint(pend, y0, t)

plt.plot(t,y)
plt.xlabel("time")
plt.grid()
plt.ylabel('y(t)')
plt.show()
