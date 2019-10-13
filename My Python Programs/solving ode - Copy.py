import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model (y,t):
     k = 0.3
     dydx = ((x*x) + 2)/y
     return dydx

y0 = 0.1

#def pend(y, x):
#     b= 4
 #    theta, omega = y
#     dydx = [omega, -b*omega + b*b]
 #    return dydt

x = np.linspace(0,10, 100)
#y0 = [10, 10]

y = odeint(model, y0, x)

plt.plot(x,y)
plt.xlabel("x")
plt.grid()
plt.ylabel('y(x)')
plt.show()
