import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#def model (y,t):
     #dydt = y
     #return dydt

y0 = 1

t = np.linspace(-10,20, 50)

#y = odeint(model, y0, t)
y = t/3
plt.plot(t,y)
plt.xlabel("time")
plt.ylabel('y(t)')
plt.show()
