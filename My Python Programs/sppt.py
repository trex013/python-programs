import matplotlib.pyplot as plt
import numpy as np

def theta(t, b=4):
     a= b*b
     r = []
     O = +(a/b) + a*np.cos(b*t) -  5* np.cos(b*t)
     r.append(O)
     return O
r = []
for t in range (0,20):
     m = t/10
     print (theta(t),"            |             ", theta(m))
     r.append(theta(m))

print(r)
t = np.linspace(0,10, 100)
y= theta(t)

plt.plot(t, y)
plt.xlabel("time")
plt.grid()
plt.ylabel('y(t)')
plt.show()
