"""A programme to solve Dr Bazuaye's assignment"""

# Variables to be Collected for computation
h = float(input("Enter Value For the one step size, h: "))
n = int(input("Enter the number of iterations: "))
x0 = int(input ("Enter initial value of x: "))
y0 = int(input ("Enter initial values for y: "))

#The differential equation
def model (x,y):
     dydx = 2*x*y
     return dydx

#Exact Solution(Analytical)
def soln(x):
     from math import e
     y_e = e**(x**2)
     return y_e

#create the list
y = []
x = []
y_e = []
y.insert(0,y0)
x.insert(0,x0)

for cnt in range(n+1):
     yn = y[cnt] + h* model(x[cnt],y[cnt])
     y.insert(cnt +1 ,yn)
     y_e.insert(cnt +1 ,soln(x[cnt]))
     x.insert(cnt + 1, x[cnt] + h)

#Output for the computation
print("{0} \t {1} \t\t {2} \t\t {3} \t\t {4}".format(" n", " x", " y", "y(exact)","Error e"))
print("-"*120)
for m in range(n+1):
     print("{0} \t {1:.2f} \t\t {2:.2f} \t\t {3:.2f} \t\t {4:.2f} " .format(m, x[m],y[m],y_e[m], y_e[m]-y[m]))

