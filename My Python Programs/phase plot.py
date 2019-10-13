from pylab import *
xvalues, yvalues = meshgrid(arange(-3, 3, 0.1), arange(-3, 3, 0.1))
xdot = -2*xvalues - yvalues
ydot = xvalues - 2*yvalues
streamplot(xvalues, yvalues, xdot, ydot)
show()
